import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
StepPins = [11, 13, 15, 16]

for pin in StepPins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

StepCounter = 0
StepCount = 4
SeqClockwise = [
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [1, 0, 0, 0]
]
SeqCounterClockwise = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]
direction = True
start_time = time.time()

try:
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time < 10:
            Seq = SeqClockwise if direction else SeqCounterClockwise
        else:
            direction = not direction
            start_time = time.time()
            Seq = SeqCounterClockwise if direction else SeqClockwise

        for pin in range(0, 4):
            xpin = StepPins[pin]
            if Seq[StepCounter][pin] != 0:
                GPIO.output(xpin, True)
            else:
                GPIO.output(xpin, False)

        StepCounter += 1
        if StepCounter == StepCount:
            StepCounter = 0
        if StepCounter < 0:
            StepCounter = StepCount

        time.sleep(0.01)

except KeyboardInterrupt:
    GPIO.cleanup()
