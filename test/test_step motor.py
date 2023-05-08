import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
StepPins = [11, 13, 15, 16]

for pin in StepPins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

StepCounter = 0
StepCount = 4

for i in range(5):
    for pin in range(0, 4):
        Seq = [[1, 0, 0, 1],  # counter
               [1, 0, 1, 0],
               [0, 1, 1, 0],
               [0, 1, 0, 1]]
        xpin = StepPins[pin]
        if Seq[StepCounter][pin] != 0:
            GPIO.output(xpin, True)
        else:
            GPIO.output(xpin, False)
        StepCounter += 1
        if StepCounter == StepCount:
            StepCounter = 0
        elif StepCounter < 0:
            StepCounter = StepCount
    time.sleep(0.002)

for i in range(5):
    for pin in range(3, -1, -1):
        Seq = [[1, 0, 0, 1],  # stepcounter
               [1, 0, 1, 0],
               [0, 1, 1, 0],
               [0, 1, 0, 1]]
        xpin = StepPins[pin]
        if Seq[StepCounter][pin] != 0:
            GPIO.output(xpin, True)
        else:
            GPIO.output(xpin, False)
        StepCounter += 1
        if StepCounter == StepCount:
            StepCounter = 0
        elif StepCounter < 0:
            StepCounter = StepCount
    time.sleep(0.002)

GPIO.cleanup()
