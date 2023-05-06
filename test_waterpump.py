import RPi.GPIO as GPIO
import time

A1A = 23
GPIO.setup(A1A, GPIO.OUT)
GPIO.output(A1A, GPIO.LOW)

GPIO.setmode(GPIO.BCM)

while True:
    GPIO.output(A1A, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(A1A, GPIO.LOW)

GPIO.cleanup

