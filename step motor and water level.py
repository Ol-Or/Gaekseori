import smbus
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
StepPins=[11,13,15,16]  #step motor GPIO

for pin in StepPins:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,False)

SeqClockwise = [   #시계방향
    [0,0,0,1],
    [0,0,1,0],
    [0,1,0,0],
    [1,0,0,0]
]
SeqCounterClockwise = [  #반시계방향
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]
]

direction = True

#PCF module address
address = 0x48
AIN2 = 0x42

bus=smbus.SMBus(1)

StepCounter = 0

StepCount=4

try:
    while True:
    bus.write_byte(address,AIN2)
    value = bus.read_byte(address)
    if value > 256: # 수위 측정한 값 쓰기!
        Seq = SeqCounterClockwise if direction else SeqClockwise
    #else :
       # Seq = SeqClockwise if direction else SeqCounterClockwise

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
