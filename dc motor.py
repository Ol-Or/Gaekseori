import smbus
import time
import RPi.GPIO as GPIO

#GPIO 핀 번호 설정
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# 모터 드라이버 모듈 핀번호
ENA = 15
IN1 = 11
IN2 = 13

# GPIO 핀 설정
GPIO.setup(ENA,GPIO.OUT)
GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)

#pwm 객체 생성
pwm = GPIO.PWM(enable_pin, 100) # PWM 주파수 100Hz로 설정

#PCF주소
address = 0x48
AIN2 = 0x42

bus=smbus.SMBus(1)

try:
    while True:
        bus.write_byte(adress,AIN2)  #수위측정 후 모터가 돌아가는 함수
        value = bus.read_byte(address)
        if value > 5 :
            GPIO.output(IN1, True)  #forward
            GPIO.output(IN2, False)
            pwm.start(50) # 50%의 속도로 이동
            time.sleep(5)     #시간 측정 해보고 설정할거임
            GPIO.output(IN1, False)
            GPIO.output(IN2, False)
            pwm.stop()
        
except KeyboardInterrupt:
    GPIO.cleanup()
    
    ## 모터 뒤로 이동
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    pwm.start(50) # 50%의 속도로 이동
