import numpy as np
from ultralytics import YOLO
import cv2
import math
#from sort import*

cap = cv2.VideoCapture("")  # 동영상 파일 열기

# 동영상 파일 프레임 수 및 크기 확인
w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps_video = cap.get(cv2.CAP_PROP_FPS)  # 프레임 수

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
delay = round(1000/fps_video)

# 출력 동영상 파일 생성(프레임별로 이미지 저장, videowriter 함수 사용)
out = cv2.VideoWriter('output.avi', fourcc, fps_video, (w, h))

# YOLOv8n 모델을 YOLO함수 이용하여 불러옴
model = YOLO("../Yolo-Weights/yolov8n.pt")
classNames = ["pig"]

new_frame_time = 0

prev_box = None  # 이전 bounding box 좌표
prev_frame_time = None  # 이전 프레임 시간

while True:
    #new_frame_time = time.time()
    success, img = cap.read()

    if not success:
        break

    # bounding box 출력
    results = model(img, stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Bounding Box 출력
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            img = cv2.rectangle(img, (x1, y1), (x2, y2),
                                (0, 255, 0), 2)  # w,h =x2-x1,y2,y1

            # Confidence 출력
            conf = math.ceil((box.conf[0]*100))/100
            # Class Name
            cls = int(box.cls[0])

            cv2.putText(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            # bounding box 좌표 계산
            center_x = int(x1 + x2 / 2)
            center_y = int(y1 + y2 / 2)

            # 이전 bounding박스 좌표와 현재 bounding box 좌표 사이의 거리 계산
            if prev_box is not None:
                prev_center_x, prev_center_y = prev_box
                distance = np.sqrt((center_x - prev_center_x)
                                   ** 2 + (center_y - prev_center_y) ** 2)

            # 이전 프레임과 현재 프레임 사이의 시간 간격 계산
            new_frame_time = cv2.getTickCount()
            if prev_frame_time is not None:
                time_interval = (new_frame_time -
                                 prev_frame_time)/cv2.getTickFrequency()

                # 바운딩 박스 움직임 속도 계산
                speed = distance/time_interval
                print("bounding box spped:", speed)

            prev_frame_time = new_frame_time
        prev_box = (center_x, center_y)

    # 현재 시간을 변수에 저장하고 이전 프레임 시간과 비교하여 프레임 속도(FPS)계산
    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
    print(fps)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

    # 프레임 별로 이미지 저장
    out.write(img)

cap.release()
out.release()
