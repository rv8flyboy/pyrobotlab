import random
from java.lang import String
from org.myrobotlab.net import BareBonesBrowserLaunch
elias = Runtime.createAndStart("elias", "ProgramAB")
elias.startSession("ProgramAB", "default", "elias")
htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter")
mouth = Runtime.createAndStart("i01.mouth", "Speech")
mouth.setGoogleURI("http://thehackettfamily.org/Voice_api/api2.php?voice=Graham&txt=")
elias.addTextListener(htmlfilter)
htmlfilter.addTextListener(mouth)
holygrail = Runtime.create("holygrail", "WebGUI")
holygrail.startService()
sleep(10)
resp = elias.getResponse("BY YOUR COMMAND")

def BT():
    global c
    c = b - a
    sleep(2)
    print c
    if (c == 3):
        x = (random.randint(1, 3))
        if x == 1:
            i01.mouth.speak("I am bored.")
        if x == 2:
            i01.mouth.speak("What a boring day.")
        if x == 3:
            i01.mouth.speak("I have nothing to do.")
    if (c == 6):
        x = (random.randint(1, 3))
        if x == 1:
            i01.mouth.speak("I will tell myself a joke.")
            sleep(4)
            resp = elias.getResponse("TELL ME A JOKE") 
        if x == 2:
            i01.mouth.speak("Do you like Star Wars?")
            sleep(4)
            resp = elias.getResponse("DO YOU LIKE STAR WARS")
            sleep(6)
            i01.mouth.speak("It was worth a try.")
        if x == 3:
            i01.mouth.speak("Let's talk about the weather.")
            sleep(4)
            resp = elias.getResponse("WEATHER IN RIO")
    if (c == 9):
            i01.mouth.speak("Where is everybody?")
            i01.headTracking.faceDetect()
            i01.eyesTracking.faceDetect()
            sleep(30)
            i01.headTracking.stopTracking()
            i01.eyesTracking.stopTracking()
    if (c == 12):
        i01.mouth.speak("I will turn off in 10 seconds.")
        sleep(10)
        i01.powerDown()
    if (c == -57):
        x = (random.randint(1, 3))
        if x == 1:
            i01.mouth.speak("I am bored.")
        if x == 2:
            i01.mouth.speak("What a boring day.")
        if x == 3:
            i01.mouth.speak("I have nothing to do.")
    if (c == -54):
        x = (random.randint(1, 3))
        if x == 1:
            i01.mouth.speak("I will tell myself a joke.")
            sleep(4)
            resp = elias.getResponse("TELL ME A JOKE") 
        if x == 2:
            i01.mouth.speak("Do you like Star Wars?")
            sleep(4)
            resp = elias.getResponse("DO YOU LIKE STAR WARS")
            sleep(6)
            i01.mouth.speak("It was worth a try.")
        if x == 3:
            i01.mouth.speak("Let's talk about the weather.")
            sleep(4)
            resp = elias.getResponse("WEATHER IN RIO")
    if (c == -51):
            i01.mouth.speak("Where is everybody?")
            i01.headTracking.faceDetect()
            i01.eyesTracking.faceDetect()
            sleep(30)
            i01.headTracking.stopTracking()
            i01.eyesTracking.stopTracking()
    if (c == -48):
        i01.mouth.speak("I will turn off in 10 seconds.")
        sleep(10)
        i01.powerDown()            
    else:
        sleep(56)
        resp = elias.getResponse("CHECKTIME")
        sleep(2)
        resp = elias.getResponse("7OF9")
