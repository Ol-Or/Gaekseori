import Adafruit_DHT
import RPi.GPIO as GPIO

sensor = Adafruit_DHT.DHT11  # 습도 센서 모델 선택
pin = 21  # 습도 센서 신호선을 연결한 GPIO 핀

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
    print('Temperature={0:0.1f}*C Humidity ={1:0.1f}%'.format(temperature, humidity))
else:
    print('Unable to output.')
