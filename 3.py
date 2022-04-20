import cv2
import time

video_name = input("Video name: ")

camera_number = int(input("Camera number: "))

minutes = int(input("minutes: "))

cap= cv2.VideoCapture(camera_number)

width= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

writer= cv2.VideoWriter(f'gesture_data_version2/{video_name}.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 20, (width,height))

start = time.time()

while True:
    ret,frame= cap.read()

    writer.write(frame)

    cv2.imshow(f'video_name:{video_name} cam:{camera_number} min:{minutes}', frame)

    end = time.time()
    print(end-start)
    print((end-start)>=60*minutes)
    stop_condition = (end-start) >= 60*minutes

    if cv2.waitKey(1) & 0xFF == 27 or stop_condition:
        break


cap.release()
writer.release()
cv2.destroyAllWindows()
