import Rpi.GPIO as GPIO
from picamera import PiCamera
switch = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN, GPIO.PUD_DOWN)
camera = PiCamera() camera.start_preview()
