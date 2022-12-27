import numpy as np
import cv2

vid = cv2.VideoCapture(0)#the number is the webcam number and it captures the video from the webcam

#haarcascades#
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

while True:
    ret, frame = vid.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#graying images
    faces = face_cascade.detectMultiScale(gray, 1.05, 3)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 5)#drawing rectangles on image
        
        roi_gray = gray[y:y+w, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.05, 3)
        
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) == ord("q"):
        break

vid.release()#release the video
cv2.destroyAllWindows()