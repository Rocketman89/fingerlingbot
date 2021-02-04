import RPi.GPIO as GPIO
import time
import sys
from datetime import datetime

#Pin Position Definition
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

def botName(name):
    return name;
def logFileClose():
    f.close()
def logFileAppend(Status,out):
    now=datetime.now()
    time=now.strftime("%Y/%m/%d_%H:%M:%S")
    f.write(time+"\t"+bname+"\tStatus: "+Status+"\n")
    if out==1:
        print(time+"\t"+bname+"\tStatus: "+Status+"")
def logFileOpen():
    f=open("./"+str(bname)+".log","a")
    return f;
def motorPins(leftNeckPin,rightNeckPin,blinkClosePin,blinkOpenPin):
    pwmfreq=50
    pinA=leftNeckPin
    pinB=rightNeckPin
    pinC=blinkClosePin
    pinD=blinkOpenPin
    GPIO.setup(pinA,GPIO.OUT)
    GPIO.setup(pinB,GPIO.OUT)
    GPIO.setup(pinC,GPIO.OUT)
    GPIO.setup(pinD,GPIO.OUT)
    return pinA, pinB, pinC, pinD;
def motorPinPriming():
    inidutycycle=0
    A=GPIO.PWM(pinA,pwmfreq)
    A.start(inidutycycle)
    B=GPIO.PWM(pinB,pwmfreq)
    B.start(inidutycycle)
    C=GPIO.PWM(pinC,pwmfreq)
    C.start(inidutycycle)
    D=GPIO.PWM(pinD,pwmfreq)
    D.start(inidutycycle)
    briefPause()
    return A, B, C, D;
def turnhead(pwm,duration,direction):
    if direction.lower()=="left" or direction.lower()=="l" :
        A.ChangeDutyCycle(pwm)
        timedPause(duration)
        A.ChangeDutyCycle(0)
    if direction.lower()=="right" or direction.lower()=="r" :
        B.ChangeDutyCycle(pwm)
        timedPause(duration)
        B.ChangeDutyCycle(0)
    briefPause()
def blink():
    C.ChangeDutyCycle(20)
    timedPause(.07)
    C.ChangeDutyCycle(0)
    briefPause()
def sitIdle(sec):
    blinkpersec=4
    loop=int(sec/blinkpersec)
    for i in range(loop):
        timedPause(blinkpersec)
        blink()
def pause(sec):
    time.sleep(sec)
def briefPause():
    pause(.1)
def timedPause(sec):
    pause(sec)

#Initializing Variables
pinA=pinB=pinC=pinD=0
pwmfreq=20
bname="bot1"
printOut=1

#Initializing Information
bname=botName("Kingsley")

#Initializing GPIO
pinA,pinB,pinC,pinD=motorPins(37,38,36,35)

#Create null GPIO class objects
A=B=C=D=GPIO.PWM(pinA,pwmfreq)
A=B=C=D=None

#Priming GPIO Pin Objects
A,B,C,D=motorPinPriming()

#Mainloop
try:
    f=logFileOpen()
    logFileAppend("Bot - "+bname+" Online",printOut)
    logFileAppend("Mainloop Begin",printOut)
    while 1:
        turnhead(15,.08,"L")
        sitIdle(10)
        turnhead(20,.07,"R")
        sitIdle(10)
        turnhead(15,.1,"L")
        sitIdle(8)
        turnhead(20,.07,"R")
        sitIdle(10)
        turnhead(15,.1,"L")
        sitIdle(8)
        turnhead(15,.08,"L")
        sitIdle(10)
        turnhead(20,.07,"R")
        sitIdle(10)
        turnhead(15,.08,"L")
        sitIdle(10)
        turnhead(20,.07,"R")
        sitIdle(10)
        turnhead(20,.07,"R")
        sitIdle(10)
        turnhead(15,.1,"L")
        sitIdle(8)
        turnhead(15,.08,"L")
        sitIdle(10)
        turnhead(14,.07,"R")
        sitIdle(10)
        logFileAppend("Mainloop Completion",printOut)
except KeyboardInterrupt:
    logFileAppend("Ending Mainloop",printOut)
    logFileAppend("Cleaning up GPIO",printOut)
    GPIO.cleanup()
    logFileAppend("Exiting Program",printOut)
    logFileClose()
    sys.exit()
