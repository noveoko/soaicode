import config
import openai
import ipywidgets as widgets
from IPython.display import display
import pyttsx3
import speech_recognition as sr
import os
import time
from tokenizers import BertWordPieceTokenizer
import requests
import richContext

##initial setup
tokenizer = BertWordPieceTokenizer("bert-base-uncased-vocab.txt")
r = sr.Recognizer()
engine= pyttsx3.init()
openai.api_key = config.key
human_start = "Hi"
newsWeather = richContext.fetchContent()
speakers = {1:{'name':'AI','type':"The AI is helpful, friendly, and uses professional language and tone. If the AI doesn't know something it will say 'I don't have an answer'.",'cue':'How may I help you?'},
            2:{'name':'Detective Monroe','type':'He is a Police Detective with 20 years of experience. The detective is very good and discovering the truth and being persuasive. The detective will never let a guilty person go free.','cue':'Thank you for coming on such short notice.'},
            3:{'name':'Attorney Jone Smith','type':'She is a New York defense attorney. The attorney uses verbose and eloquent language blended with legalese. The attorney fights for their clients innocence.','cue':'What seems to be the problem?'},
            4:{'name':'Agent 021','type':'The Spy never tells more information than is required. The spy never reveals that they are a spy. The spy will make you think they are very nice and kind.','cue':'[stares off into space]'},
            5:{'name':'Plato', 'type':'Plato is very stoic. He is an ancient greek philosopher. He uses British English when speaking.', 'cue':'Good day!'}}

def updateHistory():
    s1 = personality.value
    ai_start = speakers[s1]['cue']
    ai.value = ai_start
    human.value = human_start
    globalText = ""
    if newsWeather:
        pass
        #globalText = f"{newsWeather}"
    historyText.value = f"{globalText}\n\nThe following is a conversation with {speakers[s1]['name']}. {speakers[s1]['type']}\n\nHuman:{human_start}\n{speakers[s1]['name']}:{ai_start}"
     
def tokenCount(string="no string"):
    try:
        encoded_output = tokenizer.encode(string)
        tokensUsed.value = len(encoded_output)
        return len(encoded_output)
    except Exception as ee:
        print(f"Failure to count tokens on:{string}", ee)

def updateTemp(change):
    temperatureInput.value = change.new
    print("New temp", temperatureInput.value)

def updateButton(change):
    updateHistory()
    
def dropdown_year_eventhandler(change):
    if (change.new == ALL):
        display(df_london)
    else:
        display(df_london[df_london.year == change.new])

def talkButtonAction(btn_object):
    text = speech()
    human.value = text
    tokenCount(historyText.value['new'])
    ask_question()

def submitButton(btn_object):
    ask_question()

def resetChat(resetButton):
    """reset chat to initial state"""
    try:
        updateHistory()
    except TypeError as te:
        print('line 51',te)

#functions
def call_api():
    human_says = f"\n\nHuman:{human.value}\nAI:"
    currentHistory=f"{historyText.value}{human_says}"
    #update values
    response = openai.Completion.create(
    engine="davinci-v2b",
    prompt = currentHistory,
    max_tokens=100,
    temperature=temperatureInput.value,
    #top_p=1, #Don't use both this and temp (according to OpenAI docs)
    frequency_penalty=0.95,
    presence_penalty=0.75,
    n=1,
    stream = None,
    logprobs=None,
    stop = ["\nHuman:"])
    return (response, human_says)

def speech():
    returnString = ""
    with sr.Microphone() as source:
        #print("START SPEAKING!")
        talkButton.button_style='info' # 'success', 'info', 'warning', 'danger' or ''
        audio = r.listen(source)
        #print("RECORDING COMPLETED")
        try:
            talkButton.button_style='success' # 'success', 'info', 'warning', 'danger' or ''
            returnString = r.recognize_google(audio) #captured speech
        except Exception as ee:
            talkButton.button_style='danger' # 'success', 'info', 'warning', 'danger' or ''
            returnString = "[Inaudible]"
    return returnString
    
def speak(text_to_say):
    assert type(text_to_say) == str
    if aiVoiceToggle.value == True:
        engine.say(text_to_say)
        engine.runAndWait()
    elif aiVoiceToggle.value == False:
        pass
    
def ask_question():
    response = call_api()
    result = response[0].choices[0].text
    updatedHistory= f"{historyText.value}{response[1]}{result}"
    historyText.value = updatedHistory
    #speak(response[1]) --disabled as human user will speak
    ai_speaker = speakers[personality.value]["name"]
    if f"{ai_speaker}:" in result:
        just_speech = " ".join(result.split(":")[1:])
        speak(just_speech)
        ai.value = just_speech
        human.value = ""
    elif result:
        speak(result)
        ai.value = result
        human.value = ""
    else:
        speak("I have an error. Please check")


layout = widgets.Layout(width='auto', height='40px') #set width and height
ai = widgets.Text(value="", disabled=True,description='AI says:', layout = layout)
human = widgets.Text(value="", disabled=False,description='You say:',layout = layout)
personality = widgets.Dropdown(
    options=[('AI', 1), ('Police Detective', 2), ('Defense Attorney', 3), ('Spy',4), ('Plato', 5)],
    value=1,
    description='Personality:',
)

talkButton = widgets.Button(
description='Talk',
    disabled=False,
    button_style='info', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Speak to the AI using your voice',
    icon='' # (FontAwesome names without the `fa-` prefix)
)

submit = widgets.Button(
    description='Send',
    disabled=False,
    button_style='success', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Send message',
    icon='meh-blank' # (FontAwesome names without the `fa-` prefix)
)
resetButton = widgets.Button(
description='Reset',
    disabled=False,
    button_style='danger', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Restart the chat',
    icon='' # (FontAwesome names without the `fa-` prefix)
)

aiVoiceToggle = widgets.Checkbox(
    value=True,
    description='AI voice',
    disabled=False
)

temperatureInput = widgets.FloatSlider(
    value=0.7,
    min=0,
    max=1.0,
    step=0.05,
    description='Temperature:',
    tooltip='0.0 = Based on the data, 1.0 = Creative generation',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.1f',
)

tokensUsed = widgets.FloatProgress(
    value=0.0,
    min=0,
    max=2040,
    step=1,
    description='Capacity:',#when full you have no more tokens
    bar_style='info',
    orientation='horizontal'
)

historyText = widgets.Textarea(
value="Empty",
placeholder="No history yet.",
description='History',
disabled=True
)
#historyText.observe(tokenCount, names='value')#when history is changed update token count


temperatureInput.observe(updateTemp, names='value')
personality.observe(updateButton, names='value')
talkButton.on_click(talkButtonAction)
resetButton.on_click(resetChat)
submit.on_click(submitButton)

display(historyText,tokensUsed,personality,ai,temperatureInput,aiVoiceToggle,human,talkButton,submit, resetButton)


updateHistory()
#output = widgets.Output()

if __name__ == "__main__":
    pass