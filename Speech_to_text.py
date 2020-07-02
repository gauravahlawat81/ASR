import speech_recognition as sr

r = sr.Recognizer()

with sr.AudioFile('male.wav') as source:
    audio_text = r.listen(source)

    try:
        text = r.recognize_google(audio_text)
        print("Converting audio to text")
        print(text)

    except Exception as e:
        print("Try again")