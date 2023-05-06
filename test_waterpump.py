import RPi.GPIO as GPIO
import time

pump_channel = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(pump_channel, GPIO.OUT)

# 워터펌프를 작동시키는 함수
def turn_on_pump():
    GPIO.output(PUMP_PIN, GPIO.HIGH)
    print("turning on the water pump")

# 워터펌프를 중지시키는 함수


def turn_off_pump():
    GPIO.output(PUMP_PIN, GPIO.LOW)
    print("turning off the water pump")

while True:
    turn_on_pump()  # 워터펌프 on
    time.sleep(5)  # 워터펌프 5초동안 작동
    turn_off_pump()  # 워터펌프 off

