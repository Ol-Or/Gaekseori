import RPi.GPIO as GPIO
import time
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11

# GPIO 핀 번호 설정
fire_channel = 18
pump1_channel = 23     #heatwave
pump2_channel =20      #fire detected
ht_pin = 21

# GPIO 초기화
GPIO.setmode(GPIO.BCM)
GPIO.setup(fire_channel, GPIO.IN)

humidity,temperature= Adafruit_DHT.read_retry(sensor,ht_pin)

#water pump
GPIO.setup(pump1_channel, GPIO.OUT)
GPIO.output(pump1_channel, GPIO.LOW)
GPIO.setup(pump2_channel, GPIO.OUT)
GPIO.output(pump2_channel, GPIO.LOW)

# if fire is detected
if GPIO.input(fire_channel) == 1 : # fire is not detected
    print('good')
    GPIO.output(pump2_channel, GPIO.LOW)   #water pump off
            
else :                      # fire is detected
    print(fire is detected!)
    GPIO.output(pump2_channel, GPIO.HIGH)   #water pump on
    time.sleep(5)

# 폭염 시 워터펌프 작동(온도가 일정 이상 올라가면)
if temperature >= 30: # !!!!!!!!!!!온도 어느 정도로 설정할건지!!!!!!!
    GPIO.output(pump1_channel, GPIO.LOW)  
else:
    GPIO.output(pump1_channel, GPIO.HIGH) 

# 무한 반복
while True:
    time.sleep(1)
