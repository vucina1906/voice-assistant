import speech_recognition as sr

r = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        r.energy_threshold =10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening")
        audio = r.listen(source)
        text2 = r.recognize_google(audio)
        return text2