import RPi.GPIO as GPIO
import time
import Adafruit_DHT
import smbus

sensor = Adafruit_DHT.DHT11
pump1_channel =23     #heatwave
ht_pin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(pump1_channel, GPIO.OUT)
GPIO.output(pump1_channel, GPIO.LOW)

humidity,temperature= Adafruit_DHT.read_retry(sensor,ht_pin)

while True:
        if temperature >= 30: 
            print('temperature = {0:0.1f}*C ,water pump on!',format(temperature))
            GPIO.output(pump1_channel, GPIO.HIGH)
            time.sleep(7)
            GPIO.output(pump1_channel, GPIO.LOW)
            
        else:
            GPIO.output(pump1_channel, GPIO.LOW)
        time.sleep(1)
