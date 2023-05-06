import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# 스텝모터의 핀 번호
StepPins = [11, 13, 15, 16]

# 스텝모터 시퀀스
Seq = [
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
]

# 스텝모터 한 바퀴당 스텝 수
StepCount = len(Seq)

# 초기 스텝모터 상태
StepCounter = 0

# 스텝모터 초기화
for pin in StepPins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

try:
    # 정방향으로 회전
    for i in range(512):
        for pin in range(4):
            xpin = StepPins[pin]
            if Seq[StepCounter][pin]!=0:
                GPIO.output(xpin, True)
            else:
                GPIO.output(xpin, False)

        StepCounter += 1

        if StepCounter == StepCount:
            StepCounter = 0
        if StepCounter < 0:
            StepCounter = StepCount

        time.sleep(0.002)

    # 5초간 대기
    time.sleep(5)

    # 역방향으로 회전
    for i in range(512):
        for pin in range(4):
            xpin = StepPins[pin]
            if Seq[StepCount - StepCounter - 1][pin]!=0:
                GPIO.output(xpin, True)
            else:
                GPIO.output(xpin, False)

        StepCounter -= 1

        if StepCounter == StepCount:
            StepCounter = 0
        if StepCounter < 0:
            StepCounter = StepCount - 1

        time.sleep(0.002)

except KeyboardInterrupt:
    GPIO.cleanup()
