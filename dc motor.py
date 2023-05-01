import smbus
import time
import RPi.GPIO as GPIO

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

#PCF주소
address = 0x48
AIN2 = 0x42

bus=smbus.SMBus(1)

try:
    while True:
        bus.write_byte(adress,AIN2)  #수위측정 후 모터가 돌아가는 함수
        value = bus.read_byte(address)
        if value > 5 :
            motor_control(True,50)
            time.sleep(5)
            pwm.stop()
        
except KeyboardInterrupt:
    GPIO.cleanup()