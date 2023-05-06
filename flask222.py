from flask import Flask, request
import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(5, GPIO.OUT)  # GPIO5
GPIO.setup(6, GPIO.OUT)  # GPIO6
GPIO.setup(7, GPIO.OUT)  # GPIO7
GPIO.setup(8, GPIO.OUT)  # GPIO8

GPIO.output(5, GPIO.LOW)
GPIO.output(6, GPIO.LOW)
GPIO.output(7, GPIO.LOW)
GPIO.output(8, GPIO.LOW)


@app.route('/rid', methods=['POST'])
def rid():
    state = request.json['state']
    if state == 1:
        GPIO.output(5, GPIO.HIGH)
    else:
        GPIO.output(5, GPIO.LOW)
    return 'OK', 200


@app.route('/plate', methods=['POST'])
def plate():
    state = request.json['state']
    if state == 1:
        GPIO.output(6, GPIO.HIGH)
    else:
        GPIO.output(6, GPIO.LOW)
    return 'OK', 200


@app.route('/roof', methods=['POST'])
def roof():
    state = request.json['state']
    if state == 1:
        GPIO.output(7, GPIO.HIGH)
    else:
        GPIO.output(7, GPIO.LOW)
    return 'OK', 200


@app.route('/ceiling', methods=['POST'])
def ceiling():
    state = request.json['state']
    if state == 1:
        GPIO.output(8, GPIO.HIGH)
    else:
        GPIO.output(8, GPIO.LOW)
    return 'OK', 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
