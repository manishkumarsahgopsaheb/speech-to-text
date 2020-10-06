import speech_recognition as sr
r = sr.Recognizer()
audiofile = sr.AudioFile('manish.wav')

with audiofile as source:
    audio = r.record(source)


text = r.recognize_google(audio)
file1 = open("1.txt", "a")
file1.writelines(text)
file1.close()