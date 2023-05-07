import RPi.GPIO as GPIO
import time
from time import sleep
from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

####### 차수판#########
# variables

# 스텝모터 차수판
IN1 = 11  # Input Pin
IN2 = 13  # Input Pin
ENA = 15  # Enable Pin
# 워터펌프 지붕
A1A = 23
# LED 핀들을 딕셔너리 변수로 선언
pin_dict = {'IN1': 11, 'IN2': 13, 'ENA': 15, 'A1A': 23}
GPIO.setup(pin_dict['IN1'], GPIO.OUT)   # 각각의 LED 핀들을 출력으로 설정
GPIO.setup(pin_dict['IN2'], GPIO.OUT)
GPIO.setup(pin_dict['ENA'], GPIO.OUT)   # 각각 LED의 현재 상태를 나타내는 변수
GPIO.setup(pin_dict['A1A'], GPIO.OUT)   # 각각 LED의 현재 상태를 나타내는 변수
state_dict = {'IN1': 0, 'IN2': 0, 'ENA': 0, 'A1A': 0}


@app.route('/')                     # 기본 주소
def hello():                         # 여기서 index.html을 화면에 보여주며, LED 현황을 전달
    return render_template('main.html', state_dict=state_dict)


@app.route('/<pin>/<int:state>')  # 각각의 pin을 켜고 끄기 위한 주소
def control(pin, state):      # 각각의 pin을 켜고 끄기 위한 뷰함수
    state_dict[pin] = state   # pin과 state를 전달받아 현황을 갱신함
    # 참고: color와 state를 전달받는 부분은 index.html 부분에 코드가 있음
    GPIO.output(pin_dict['IN1'], state_dict['IN1'])
    GPIO.output(pin_dict['IN2'], state_dict['IN2'])
    GPIO.output(pin_dict['A1A'], state_dict['A1A'])
    return redirect(url_for('hello'))    # 제어가 끝나면 기본주소로 돌아감


# 스텝모터 차수판


if __name__ == "__main__":
    app.run(host="192.168.207.211", port="9090")
