

import speech_recognition as sr
import pyttsx3
import tkinter as tk

# Initialize the recognizer 
r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')

def getVoicesDetails():
    names = []
    for voice in voices:
        names.append(voice.id.replace("HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_",''))
    return names

def SpeakField():
    text = field.get("1.0", tk.END)
    engine.say(text)
    engine.runAndWait()

def SpeakCommand(command):
    engine.say(command)
    engine.runAndWait()

def recognise():
    try: 
        # use the microphone as source for input.
        with sr.Microphone() as source2:

            #listens for the user's input 
            audio2 = r.listen(source2)

            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            
            #setting text to field
            field.delete("1.0", tk.END)
            field.insert("1.0", MyText)

            SpeakCommand(MyText)
              
    except sr.RequestError:
        field.delete("1.0", tk.END)
        field.insert("1.0", "Connection To Server Failed")
        SpeakCommand("Connection To Server Failed")
          
    except sr.UnknownValueError:
        field.delete("1.0", tk.END)
        field.insert("1.0", "Couldn't Recognise what you said")
        SpeakCommand("Couldn't Recognise what you said")

voicesIDS = getVoicesDetails()

#GUI Creation
window = tk.Tk()
window.title("Speech to Text")

#---------------drop Down controller Start----------------#

voiceIDVar = tk.StringVar(window)
voiceIDVar.set(voicesIDS[0])
engine.setProperty('voice',voiceIDVar.get())

Selector = tk.OptionMenu(window, voiceIDVar, *voicesIDS)
Selector.grid(row = 1, column = 0, padx= 5 ,pady = 5,columnspan = 2, sticky = tk.N + tk.S + tk.E + tk.W)

def change_dropdown(*args):
    engine.setProperty('voice',"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_"+voiceIDVar.get())

voiceIDVar.trace('w', change_dropdown)

#-----------------drop Down controller END-----------------#

recognize_btn = tk.Button(
    text="Recognize",
    command=recognise,
    fg = "Green"
)
recognize_btn.grid(row = 2, column = 0, padx= 5 ,pady = 5, sticky = tk.N + tk.S + tk.E + tk.W)

speak = tk.Button(
    text="Speak",
    command=SpeakField,
    fg="Blue"
)
speak.grid(row = 2, column = 1, padx= 5 ,pady = 5, sticky = tk.N+tk.S+tk.E+tk.W)

field = tk.Text(width=100)
field.grid(row = 3, column = 0, padx= 5 ,pady = 5, columnspan = 2)

if __name__ == "__main__":
    window.mainloop()