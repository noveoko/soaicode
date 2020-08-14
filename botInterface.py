import config
import openai
import ipywidgets as widgets
from IPython.display import display
import pyttsx3

r = sr.Recognizer()
engine= pyttsx3.init()

layout = widgets.Layout(width='auto', height='40px') #set width and height

openai.api_key = config.key

ai_start = "I am a chat bot based on GPT-3"
human_start = "Hi"
conversation_partner = "an AI.The AI is helpful and friendly." #who/what are we going to chat with? 
history = f"The following is a conversation with {conversation_partner}\n\nHuman:{human_start}\nAI:{ai_start}"

def createInterface():
    ai = widgets.Text(value=ai_start, disabled=True,description='AI says:', layout = layout)
    human = widgets.Text(value=human_start, disabled=False,description='You say:',layout = layout)
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

    historyText = widgets.Textarea(
    value=history,
    placeholder=history,
    description='History',
    disabled=True
    )
    display(historyText,ai,temperatureInput,aiVoiceToggle,human,submit, resetButton)

    submit.on_click(submitButton)
    temperatureInput.observe(updateTemp, names='value')
    resetButton.on_click(resetChat)

def updateTemp(change):
    temperatureInput.value = change.new
    
def submitButton(btn_object):
    ask_question()

def resetChat(resetButton):
    """reset chat to initial state"""
    try:
        human.value = human_start
        ai.value = ai_start
        historyText.value = history
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
    top_p=1,
    n=1,
    stream = None,
    logprobs=None,
    stop = ["\n","Human:"])
    return (response, human_says)

def ask_question():
    response = call_api()
    result = response[0].choices[0].text
    updatedHistory= f"{historyText.value}{response[1]}{result}"
    historyText.value = updatedHistory
    speak(response[1])
    speak(result)
    ai.value = result
    human.value = ""

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
    createInterface()
    