import config
import openai
import ipywidgets as widgets
from IPython.display import display
import pyttsx3
import speech_recognition as sr

r = sr.Recognizer()
engine= pyttsx3.init()

layout = widgets.Layout(width='auto', height='40px') #set width and height

openai.api_key = config.key


human_start = "Hi"
personality = widgets.Dropdown(
    options=[('AI', 1), ('Police Detective', 2), ('Defense Attorney', 3), ('Spy',4)],
    value=1,
    description='Personality:',
)

speakers = {1:{'name':'AI','type':"The AI is helpful, friendly, and uses professional language and tone. If the AI doesn't know something it will say 'I don't have an answer'.",'cue':'How may I help you?'},
                 2:{'name':'Detective Monroe','type':'He is a Police Detective with 20 years of experience. The detective is very good and discovering the truth and being persuasive. The detective will never let a guilty person go free.','cue':'Thank you for coming on such short notice.'},
                 3:{'name':'Attorney Jone Smith','type':'She is a New York defense attorney. The attorney uses verbose and eloquent language blended with legalese. The attorney fights for their clients innocence.','cue':'What seems to be the problem?'},
                 4:{'name':'Agent 021','type':'The Spy never tells more information than is required. The spy never reveals that they are a spy. The spy will make you think they are very nice and kind.','cue':'[stares off into space]'}}
ai = widgets.Text(value="", disabled=True,description='AI says:', layout = layout)
human = widgets.Text(value="", disabled=False,description='You say:',layout = layout)

def updateHistory():
    s1 = personality.value
    ai_start = speakers[s1]['cue']
    ai.value = ai_start
    human.value = human_start
    historyText.value = f"The following is a conversation with {speakers[s1]['name']}. {speakers[s1]['type']}\n\nHuman:{human_start}\n{speakers[s1]['name']}:{ai_start}"

historyText = widgets.Textarea(
value="",
placeholder="No history yet.",
description='History',
disabled=True
)

updateHistory()
output = widgets.Output()

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
    value=False,
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
def updateTemp(change):
    temperatureInput.value = change.new
    
temperatureInput.observe(updateTemp, names='value')



display(historyText,personality,ai,temperatureInput,aiVoiceToggle,human,talkButton,submit, resetButton)
###########################
def updateButton(change):
    updateHistory()
    
personality.observe(updateButton, names='value')

def dropdown_year_eventhandler(change):
    if (change.new == ALL):
        display(df_london)
    else:
        display(df_london[df_london.year == change.new])
###########################
def talkButtonAction(btn_object):
    text = speech()
    human.value = text
    ask_question()
    
talkButton.on_click(talkButtonAction)

def submitButton(btn_object):
    ask_question()
    
submit.on_click(submitButton)

def resetChat(resetButton):
    """reset chat to initial state"""
    try:
        updateHistory()
    except TypeError as te:
        print('line 51',te)
resetButton.on_click(resetChat)

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
    top_p=1,
    n=1,
    stream = None,
    logprobs=None,
    stop = ["\nHuman:"])
    return (response, human_says)

def ask_question():
    response = call_api()
    result = response[0].choices[0].text
    updatedHistory= f"{historyText.value}{response[1]}{result}"
    historyText.value = updatedHistory
    #speak(response[1]) --disabled as human user will speak
    speak(result)
    ai.value = result
    human.value = ""

def speech():
    with sr.Microphone() as source:
        #print("START SPEAKING!")
        audio = r.listen(source)
        #print("RECORDING COMPLETED")
        try:
            return r.recognize_google(audio) #captured speech
        except Exception as ee:
            pass
    
    
def speak(text_to_say):
    try:
        if aiVoiceToggle.value == True:
            engine.say(text_to_say)
            engine.runAndWait()
        elif aiVoiceToggle.value == False:
            pass
    except Exception as ee:
        print(ee)
    
if __name__ == "__main__":
    pass
    