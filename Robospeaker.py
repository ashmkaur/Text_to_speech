import pyttsx3
engine = pyttsx3.init()
while(True):
    command= input("Enter something I need to speak")
    if command== "q":
        engine.say("Bye bye friend")
        engine.runAndWait()
        break
    engine.say(command)
    engine.runAndWait()