import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# 모터 드라이버 모듈 핀번호
motor_pin1 = 11 # IN1
motor_pin2 = 13 # IN2
enable_pin = 15 # ENA

# GPIO 핀 설정
GPIO.setup(motor_pin1, GPIO.OUT)
GPIO.setup(motor_pin2, GPIO.OUT)
GPIO.setup(enable_pin, GPIO.OUT)
pwm = GPIO.PWM(enable_pin, 100) # PWM 주파수 100Hz로 설정

# DC모터를 제어하는 함수
def motor_control(direction, speed):
    GPIO.output(motor_pin1, direction)
    GPIO.output(motor_pin2, not direction)
    pwm.start(speed)

# DC모터를 테스트하기 위한 코드
motor_control(True, 50) # 전진
time.sleep(3)
motor_control(False, 50) # 후진
time.sleep(3)

# PWM 객체와 GPIO 리소스를 해제
pwm.stop()
GPIO.cleanup()
