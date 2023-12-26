import pyttsx3

if __name__ == "__main__":
    print("Welcome to RoboSpeaker 1.0. Created by Saransh Tyagi")
    engine = pyttsx3.init()
    while True:
        x = input("Enter what do you want me to speak: ")
        if x.lower() == "q":
            engine.say("bye bye friend")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()
