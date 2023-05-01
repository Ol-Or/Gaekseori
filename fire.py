import RPi.GPIO as GPIO
import time

# GPIO 핀 번호 설정
channel = 18
# water_pump 핀 번호 설정
A1A = 4
GPIO.setup(A1A, GPIO.OUT)
GPIO.output(A1A, GPIO.LOW)

# GPIO 초기화
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)


def callback(channel):
    if GPIO.input(channel):
        print("Fire detected!")
        GPIO.output(A1A, GPIO.HIGH)  # 워터펌프 On
        sleep(30)  # !!!!!!!!!!!!!30초 대기??!!!!!!!!!!!!!!!!!!1
        GPIO.output(A1A, GPIO.LOW)  # 워터 펌프 30초 뒤 off


# GPIO 핀 값 변경 감지 이벤트 등록
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)

# 무한 반복
while True:
    time.sleep(1)
