import RPi.GPIO as GPIO
import time
from time import sleep
from flask import Flask, render_template
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

# 스텝모터 & 워터펌프 셋업
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(A1A, GPIO.OUT)


# 스텝모터 & 워터펌프 초기화

GPIO.output(IN1, GPIO.LOW)
GPIO.output(IN2, GPIO.LOW)
GPIO.output(ENA, GPIO.LOW)
GPIO.output(A1A, GPIO.LOW)


# def
# 스텝모터 차수판

# 모터 앞으로 이동
def motorOn():
	print("forward motion")
	GPIO.output(IN1, True)  # forward
    GPIO.output(IN2, False)
    time.sleep(5)     #시간 측정 해보고 설정할거임
#모터 뒤로 이동
def motorOff():
	print ("backward motion")
	GPIO.output(IN1, GPIO.LOW)
	GPIO.output(IN2, GPIO.HIGH)
	time.sleep(5)  #시간 측정 해보고 설정할거임
#모터 정지


#워터펌프 동작
def waterPumpOn(duration):
    GPIO.output(A1A, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(A1A, GPIO.LOW)

def waterPumpOn():
	GPIO.output(A1A, GPIO.LOW)

@app.route('/')
def hello():
	return render_template('main.html')

#차수판의 스텝모터 동작
@app.route('/motoron')
def motor_on():
	motorOn()
	return ('OK'), 204

@app.route('/motoroff')
def motor_off():
	motorOff()
	return ('OK'), 204


@app.route('/pumpon')
def pump_on():
	waterPumpOn()
	return ('OK'), 204

@app.route('/pumpoff')
def pump_off():
	waterPumpOn()
	return ('OK'), 204

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')