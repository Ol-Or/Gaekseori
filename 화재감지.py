import RPi.GPIO as GPIO
import time

FLAME = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(FLAME, GPIO.IN)

try:
    while True:
        if GPIO.input(FLAME) == 1 : # 평소 1을 전송함
            print("안전")
            
        else :                      # 불꽃 감지시 0을 전송함
            print("화재 경보")
           
            
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
