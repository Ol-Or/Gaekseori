import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

A1A = 23
GPIO.setup(A1A, GPIO.OUT)
GPIO.output(A1A, GPIO.LOW)


def run_motor(duration):
    GPIO.output(A1A, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(A1A, GPIO.LOW)


run_motor(10)

GPIO.cleanup()
