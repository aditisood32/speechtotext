
from gtts import gTTS, lang
import os
from tkinter import *
from tkinter import messagebox
import speech_recognition as sr
def text_to_speech():
       
       text = text_entry.get("1.0","end-1c")
       language = accent_entry.get()
       
       if (len(text)<=1) | (len(language)<=0):
               messagebox.showerror(message="Enter required details")
               return     
    
       speech = gTTS(text = text, lang = language, slow = False)
       
       speech.save("text.mp3")
       
       os.system("start "+"text.mp3")
def list_languages():
       
       messagebox.showinfo(message=list(lang.tts_langs().items()))

def speech_to_text(): 
      
       
       recorder = sr.Recognizer()
       try:
               duration =int(duration_entry.get())
       except:
               messagebox.showerror(message="Enter the duration")
               return
       
       messagebox.showinfo(message="Speak into the microphone and wait after finishing the recording")  
       with sr.Microphone() as mic: 
               
               
               recorder.adjust_for_ambient_noise(mic)
               audio_input = recorder.listen(mic, duration=duration)   
               try:                        
                       text_output =recorder.recognize_google(audio_input)
                    
                       messagebox.showinfo(message="You said:\n "+text_output)       
               except:
                        messagebox.showerror(message="Couldn't process the audio input.")       
window = Tk()

window.geometry("700x500")
window.title("Text to speech and speech to text")
title_label = Label(window, text="Convert Speech to text and text to Speech").pack()

text_label = Label(window, text="Text:",bg="lightblue",fg="red",font=("Arial Black",13,"bold")).place(x=130,y=120)
text_entry = Text(window, width=30,height=5)
text_entry.place(x=200,y=100)

accent_label = Label(window, text="Language:",bg="lightblue",fg="red").place(x=100,y=300)
accent_entry = Entry(window,  width=26)
accent_entry.place(x=180,y=300)
duration_label = Label(window, text="Duration:",bg="lightblue",fg="red").place(x=100,y=340)
duration_entry = Entry(window,  width=26)
duration_entry.place(x=180,y=340)
 

button1 = Button(window,text='List languages', bg = 'Turquoise',fg='Red',command=list_languages).place(x=10,y=390)
button2 = Button(window,text='Convert Text to Speech', bg = 'Turquoise',fg='Red',command=text_to_speech).place(x=130,y=390)
button3 = Button(window,text='Convert Speech to Text', bg = 'Turquoise',fg='Red',command=speech_to_text).place(x=305,y=390)
window.mainloop()                               