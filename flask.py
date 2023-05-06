# 안드로이드 앱에서 GPIO 제어하기 위한 프레임워크

from flask import Flask, request
import RPi.GPIO as GPIO


app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(5, GPIO.OUT)  # 뚜껑 핀번호 바꾸기
GPIO.setup(6, GPIO.OUT)  # 차수판 핀번호 바꾸기
GPIO.setup(7, GPIO.OUT)  # 지붕 핀번호 바꾸기
GPIO.setup(8, GPIO.OUT)  # 천장 핀번호 바꾸기

GPIO.output(5, GPIO.LOW)  # 뚜껑 핀번호 바꾸기
GPIO.output(6, GPIO.LOW)  # 차수판 핀번호 바꾸기
GPIO.output(7, GPIO.LOW)  # 지붕 핀번호 바꾸기
GPIO.output(8, GPIO.LOW)  # 천장 핀번호 바꾸기


@app.route('/')
def index():
    return 'Hello world'


@app.route('/on')
def rid():
    if
    GPIO.output(5, GPIO.HIGH)  # 뚜껑 on
    return 'RID ON'


@app.route('/off')
def led_off():
    GPIO.output(5, GPIO.LOW)
    GPIO.output(6, GPIO.LOW)
    return 'LED OFF'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
