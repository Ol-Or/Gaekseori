#!!!!!!!!!!!!!!!!!!! 1 불꽃감지 test!!!!!!!!!!!!!!!!!!!

import bluetooth
import smbus
import Adafruit_DHT
import RPi.GPIO as GPIO
import time

sensor_pin = 18  # 불꽃 감지 센서 신호선을 연결한 GPIO 핀

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)

while True:
    if GPIO.input(sensor_pin):
        print('불꽃 감지!')
    time.sleep(0.1)


#!!!!!!!!!!!!!!! 2 온습도센서 test!!!!!!!!!!!!!!!!!!

sensor = Adafruit_DHT.DHT11  # 습도 센서 모델 선택
pin = 4  # 습도 센서 신호선을 연결한 GPIO 핀

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
    print('온도={0:0.1f}*C  습도={1:0.1f}%'.format(temperature, humidity))
else:
    print('센서에서 값을 읽어올 수 없습니다.')

#!!!!!!!!!!!!!!! 3 서보모터 test!!!!!!!!!!!!!!!!!!

servo_pin = 18  # 서보모터 신호선을 연결한 GPIO 핀

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50)  # PWM 주파수를 50Hz로 설정
pwm.start(0)


def set_angle(angle):
    duty = angle / 18 + 2  # duty = 각도 / 18 + 2
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(0)


try:
    while True:
        set_angle(0)  # 0도로 회전
        time.sleep(1)
        set_angle(90)  # 90도로 회전
        time.sleep(1)
        set_angle(180)  # 180도로 회전
        time.sleep(1)
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()

#!!!!!!!!!!!!!!! 4 수위센서 test!!!!!!!!!!!!!!!!!!

address = 0x48
AIN2 = 0x42

bus = smbus.SMBus(1)

try:
    while True:
        bus.write_byte(address, AIN2)
        value = bus.read_byte(address)
        print("Water value: %d" % value)
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

#!!!!!!!!!!!!!!! 5 블루투스 test!!!!!!!!!!!!!!!!!!
#import socket

server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
port = 1
server_socket.bind(("", port))
server_socket.listen(1)

client_socket, address = server_socket.accept()
print("Accepted connection from ", address)

while true:
    data = client_socket.recv(1024)  # 앱에서 받은 데이터 프린트 (버튼 마다 a~h로 설정함..)
    print("Received: %s" % data)

client_socket.close()
server_socket.close()
