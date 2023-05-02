import RPi.GPIO as GPIO
import time
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11

# GPIO 핀 번호 설정
fire_channel = 18
pump_channel = 23
temp_pin = 2

# GPIO 초기화
GPIO.setmode(GPIO.BCM)
GPIO.setup(fire_channel, GPIO.IN)
GPIO.setup(pump_channel, GPIO.OUT)

temperature = Adafruit_DHT.read_retry(sensor, pin)

# 워터펌프를 작동시키는 함수


def turn_on_pump():
    GPIO.output(PUMP_PIN, GPIO.HIGH)
    print("워터펌프가 작동합니다.")


# 워터펌프를 중지시키는 함수

def turn_off_pump():
    GPIO.output(PUMP_PIN, GPIO.LOW)
    print("워터펌프가 중지됩니다.")

# 불꽃감지 워터펌프 작동 함수


def callback(channel):
    if GPIO.input(channel):
        turn_on_pump()  # 워터펌프 on
        time.sleep(5)  # 워터펌프 5초동안 작동
        turn_off_pump()  # 워터펌프 off

# 폭염 시 워터펌프 작동(온도가 일정 이상 올라가면)


if temperature >= :  # !!!!!!!!!!!온도 어느 정도로 설정할건지!!!!!!!
    turn_on_pump()
else:
    turn_off_pump()


# GPIO 핀 값 변경 감지 이벤트 등록
GPIO.add_event_detect(fire_channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(fire_channel, callback)

# 무한 반복
while True:
    time.sleep(1)
