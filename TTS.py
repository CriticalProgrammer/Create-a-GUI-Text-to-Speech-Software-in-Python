import pyttsx3
import tkinter as tk

def speak_text():
    engine = pyttsx3.init()
    engine.setProperty('rate',150)
    engine.say(text.get('1.0',tk.END))
    engine.runAndWait()

window = tk.Tk()
window.geometry("400x200")
window.title("CP TTS")

text = tk.Text(window,height=10, width=50)
text.pack()

button = tk.Button(window,text="Speak",command=speak_text)
button.pack()

window.mainloop()