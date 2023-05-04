import RPi.GPIO as GPIO
import time

# GPIO 핀 번호 설정
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# 모터 드라이버 핀 설정
ENA = 15
IN1 = 11
IN2 = 13

# GPIO 핀 설정
GPIO.setup(ENA,GPIO.OUT)
GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)

# PWM 객체 생성
pwm = GPIO.PWM(ENA, 100) # PWM 주파수는 100Hz

# 모터 앞으로 이동
GPIO.output(IN1, True)
GPIO.output(IN2, False)
pwm.start(50) # 50%의 속도로 이동

# 5초 대기 후 정지
time.sleep(5)
GPIO.output(IN1, False)
GPIO.output(IN2, False)
pwm.stop()

# 모터 뒤로 이동
GPIO.output(IN1, False)
GPIO.output(IN2, True)
pwm.start(50) # 50%의 속도로 이동

# 5초 대기 후 정지
time.sleep(5)
GPIO.output(IN1, False)
GPIO.output(IN2, False)
pwm.stop()

# GPIO 핀 해제
GPIO.cleanup()
