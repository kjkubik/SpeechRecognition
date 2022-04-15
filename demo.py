import speech_recognition as sr
import pyttsx3
import webbrowser as wb

# object to makes sure what we are saying into the microphone
recognizer = sr.Recognizer()

while True: 
    try: 
    
        with sr.Microphone() as mic:
            
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            
            #text = recognizer.recognize_google(audio, language = 'en-IN', show_all = True )
            text = recognizer.recognize_google(audio)
            text = text.lower()
            
            print(f"I think you said: {text}")
    except sr.UnknownValueError():
        
        recognizer = sr.Recognizer()
        continue
    
# Results: 
# TEST: Run code and say, "Can you here me now?"
# [Running] python -u "c:\Users\kkubi\Class Repo\SpeechRecognition\demo.py"
# I think you said: can you hear me now