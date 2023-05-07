import RPi.GPIO as GPIO  # RPi.GPIO 라이브러리를 GPIO로 사용
import Adafruit_DHT  # 라이브러리 불러오기(습도센서 라이브러리)
from time import sleep  # time 라이브러리의 sleep함수 사용

sensor = Adafruit_DHT.DHT11  # sensor 객체 생성
ht_pin = 21  # 습도 핀
servo_pin = 12   # 서보 핀
humidity,temperature= Adafruit_DHT.read_retry(sensor,ht_pin)

GPIO.setmode(GPIO.BOARD)        # GPIO 설정
GPIO.setup(servo_pin, GPIO.OUT)  # 서보핀 출력으로 설정

servo = GPIO.PWM(servo_pin, 50)  # 서보핀을 PWM 모드 50Hz로 사용하기 (50Hz > 20ms)
servo.start(0)  # 서보 PWM 시작 duty = 0, duty가 0이면 서보는 동작하지 않는다.


def set_angle(angle):
    duty = angle / 18 + 2  # duty = 각도 / 18 + 2
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(0)


if humidity >= 58: 
    set_angle(90)
    print('')
    sleep(1)  # 1초 대기

    # 180도에 위치
    set_angle(180)
    sleep(100) 

    # 서보 PWM 정지
    servo.stop()
    # GPIO 모드 초기화
    GPIO.cleanup()

else:
    set_angle(90)    # 서보 0도에 위치
    sleep(100)  # 1초 대기

    # 서보 PWM 정지
    servo.stop()
    # GPIO 모드 초기화
    GPIO.cleanup()
