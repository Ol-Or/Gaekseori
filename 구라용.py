import RPi.GPIO as GPIO
import time

fire_channel = 18
pump2_channel =20      #fire detected

# GPIO 초기화
GPIO.setmode(GPIO.BCM)
GPIO.setup(fire_channel, GPIO.IN)

GPIO.setup(pump2_channel, GPIO.OUT)
GPIO.output(pump2_channel, GPIO.LOW)

if GPIO.input(fire_channel) == 0:
    print('good!')
    time.sleep(10)
    print('fire is detected')
    GPIO.output(pump2_channel,GPIO.HIGH)
    time.sleep(7)
    GPIO.output(pump2_channel, GPIO.LOW)  

else :                      
    print('NOTHING')
    GPIO.output(pump2_channel, GPIO.LOW)  
    time.sleep(5)

while True:
    time.sleep(1)