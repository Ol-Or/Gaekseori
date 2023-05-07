import RPi.GPIO as GPIO
import time
import Adafruit_DHT
import smbus
from time import sleep  # time 라이브러리의 sleep함수 사용

sensor = Adafruit_DHT.DHT11

# GPIO 핀 번호 설정
fire_channel = 18
pump1_channel = 23     #fire detected
pump2_channel =20      #heatwave
ht_pin = 21
servo_pin = 12   # 서보 핀

# GPIO 초기화
GPIO.setmode(GPIO.BCM)
GPIO.setup(fire_channel, GPIO.IN)
GPIO.setmode(GPIO.BOARD)        # GPIO 설정
GPIO.setup(servo_pin, GPIO.OUT)  # 서보핀 출력으로 설정
#water pump
GPIO.setup(pump1_channel, GPIO.OUT)
GPIO.output(pump1_channel, GPIO.LOW)
GPIO.setup(pump2_channel, GPIO.OUT)
GPIO.output(pump2_channel, GPIO.LOW)

humidity,temperature= Adafruit_DHT.read_retry(sensor,ht_pin)

servo = GPIO.PWM(servo_pin, 50)  # 서보핀을 PWM 모드 50Hz로 사용하기 (50Hz > 20ms)
servo.start(0)  # 서보 PWM 시작 duty = 0, duty가 0이면 서보는 동작하지 않는다.

#steping motor
GPIO.setwarnings(False)
StepPins=[11,13,15,16]  #steping motor GPIO

#PCF module address
address = 0x48
AIN2 = 0x42

bus=smbus.SMBus(1)

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

StepCounter = 0

StepCount=4

bus.write_byte(address,AIN2)
value = bus.read_byte(address)


# if fire is detected
try:
    while True:
        if GPIO.input(FLAME) == 0 : # fire is detected
            print('fire is detected')
            GPIO.output(pump1_channel, GPIO.HIGH)   #water pump on
            time.sleep(5)    
        else :                      #fire is not detected
            GPIO.output(pump1_channel, GPIO.LOW)   #water pump off
            break


# 폭염 시 워터펌프 작동(온도가 일정 이상 올라가면)

    while True:
        if temperature >= 30: 
            print('temperature = {0:0.1f}*C ,water pump on!',format(temperature))
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
      
# Rainwater detection
def set_angle(angle):
    duty = angle / 18 + 2  # duty = 각도 / 18 + 2
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(0)

try:
    while True:
        if humidity >= 90:  # !!!!!!여기 빗물이 있을 때 습도 값을 몰라서 아직 작성안함!!!!!!!!!
            set_angle(0)    # 서보 0도에 위치
            time.sleep(1)  # 1초 대기

    # 180도에 위치
            set_angle(180)

    # 서보 PWM 정지
            servo.stop()
        else:
            set_angle(0)    # 서보 0도에 위치
            time.sleep(1)  # 1초 대기

        # 서보 PWM 정지
            servo.stop()

except KeyboardInterrupt:
    GPIO.cleanup()

