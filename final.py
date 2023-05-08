import RPi.GPIO as GPIO
import time
import Adafruit_DHT
import smbus
from time import sleep  

sensor = Adafruit_DHT.DHT11   #for DHT11

# GPIO pin number
fire_channel = 18       #fire detect
pump1_channel = 23     #fire detected
pump2_channel =20      #heatwave
ht_pin = 21        #humidity and temperature sensor(DHT11)
servo_pin = 12   # servo motor

# GPIO Initialization
GPIO.setmode(GPIO.BCM)
GPIO.setup(fire_channel, GPIO.IN)
GPIO.setup(servo_pin, GPIO.OUT)  
#water pump
GPIO.setup(pump1_channel, GPIO.OUT)
GPIO.output(pump1_channel, GPIO.LOW)
GPIO.setup(pump2_channel, GPIO.OUT)
GPIO.output(pump2_channel, GPIO.LOW)

humidity,temperature= Adafruit_DHT.read_retry(sensor,ht_pin)

servo = GPIO.PWM(servo_pin, 50)  # Using the servo pin in PWM mode at 50 Hz (50Hz > 20ms)
servo.start(0)  # Servo PWM start duty = 0, when duty is 0, servo does not work

#stepping motor
GPIO.setwarnings(False)
StepPins=[11,13,15,16]  #stepping motor GPIO

#PCF module address
address = 0x48
AIN2 = 0x42

bus=smbus.SMBus(1)  #for PCF8591

for pin in StepPins:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,False)

SeqClockwise = [   #stepping motor clockwise
    [0,0,0,1],
    [0,0,1,0],
    [0,1,0,0],
    [1,0,0,0]
]
SeqCounterClockwise = [  #stepping motor counterclockwise
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]
]

direction = True

StepCounter = 0

StepCount=4

bus.write_byte(address,AIN2)    #water level sensor
value = bus.read_byte(address)

# Rainwater detection
def set_angle(angle):
    duty = angle / 18 + 2  # duty = angle / 18 + 2
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(0)

# Fire detection
try:
    while True:
        if GPIO.input(fire_channel) == 0 : # fire is detected
            print('fire is detected')
            GPIO.output(pump1_channel, GPIO.HIGH)   #water pump on
            time.sleep(5)    
        else :                      #fire is not detected
            GPIO.output(pump1_channel, GPIO.LOW)   #water pump off
            break


# Heat wave

    while True:
        if temperature >= 30: 
            print('temperature={0:0.1f}*C  humidity={1:0.1f}%, Water pump on!'.format(temperature, humidity))
            GPIO.output(pump2_channel, GPIO.LOW)
            time.sleep(10)
            break
        else:
            GPIO.output(pump2_channel, GPIO.HIGH)
        time.sleep(1)
 
#if flood occur
    while True:
        bus.write_byte(address,AIN2)
        value = bus.read_byte(address)
        if value > 256: # water level
            print('Flood is occur!')
            Seq = SeqClockwise if direction else SeqCounterClockwise
        else :
        # Seq = SeqCounterClockwise if direction else SeqClockwise   시계방향(앱으로 구현)
            break

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
      
    while True:
        if humidity >= 65:  
            print('temperature={0:0.1f}*C  humidity={1:0.1f}%, Water tank open!'.format(temperature, humidity))
            set_angle(90)    # 서보 0도에 위치
            time.sleep(1)  # 1초 대기

    # 180도에 위치
            set_angle(180)
            time.sleep(100)
            
    # 서보 PWM 정지
            servo.stop()
        else:
            print('temperature={0:0.1f}*C  humidity={1:0.1f}%, Water tank open!'.format(temperature, humidity))
            set_angle(90)    
            time.sleep(100)  

        # 서보 PWM 정지
            servo.stop()

except KeyboardInterrupt:
    GPIO.cleanup()
