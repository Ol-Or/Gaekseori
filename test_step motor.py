import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
StepPins=[11,13,15,16]

for pin in StepPins:
    GPIO.stepup(pin,GPIO.OUT)
    GPIO.output(pin,False)

StepCounter = 0

StepCount=4


for pin in range(0,4):
    Seq = [[0, 0, 0, 1],  #정방향
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [1, 0, 0, 0]]
    xpin = StepPins[pin]
    if Seq[StepCounter][pin] !=0:
        GPIO.output(xpin, True)
    else:
        GPIO.output(xpin,False)
 
        StepCounter += 1

        if (StepCounter ==StepCount):
            StepCounter =0
        if (StepCounter<0):
            StepCounter = StepCount

        time.sleep(0.01)
        
    time.sleep(5)  #5초간 대기

for pin in range(0,4):
    Seq = [[0, 0, 0, 1],    #역방향
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [1, 0, 0, 0]]
    xpin = StepPins[pin]
    if Seq[StepCounter][pin] !=0:
        GPIO.output(xpin, True)
    else:
        GPIO.output(xpin,False)
 
        StepCounter += 1

        if (StepCounter ==StepCount):
            StepCounter =0
        if (StepCounter<0):
            StepCounter = StepCount

        time.sleep(0.01)  



except KeyboardInterrupt:
    GPIO.cleanup()
