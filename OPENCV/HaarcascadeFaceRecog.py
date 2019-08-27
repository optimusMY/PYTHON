

'''import cv2
import numpy as np

cap = cv2.VideoCapture(0)




while (True):
    ret, frame = cap.read()

    #img = cv2.imread("BritishActors.jpg")

    face_casc = cv2.CascadeClassifier("haarcascade_frontalcatface.xml")  #önce kaş sonra göz sonra burun sonra ağız tanıyıp yuzu algilama
    eye_casc = cv2.CascadeClassifier("haarcascade_eye.xml")   #sadece goz tanima


    imggray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    detected_faces = face_casc.detectMultiScale(imggray, 1.1, 3)  #1.1 is %10 scale increased, 4 is iteration count

    #print(detected_faces)

    for (x, y, w, h) in detected_faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)  #green rectangle around face area
        face = frame[y:y+h, x:x+w]
        grayface = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        detected_eyes = eye_casc.detectMultiScale(grayface, 1.1, 3)  # detect eyes from detected face
        for (xx, yy, ww, hh) in detected_eyes:
            cv2.rectangle(face, (xx, yy), (xx + ww, yy + hh), (0, 0, 255), 2)  # red rectangle around eyes area



    cv2.imshow("face detection", frame)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()


'''

import cv2
import numpy as np

#cap = cv2.VideoCapture(0)  #live cam video
#cap = cv2.VideoCapture("vtest.avi")
cap = cv2.VideoCapture("CarsOnTheRoad.mp4")


while (True):
    ret, frame = cap.read()

    # img = cv2.imread("BritishActors.jpg")

    body_casc = cv2.CascadeClassifier("haarcascade_fullbody.xml")  #
    cars_casc = cv2.CascadeClassifier("haarcascade_cars.xml")  #


    imggray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    detected_bodies = body_casc.detectMultiScale(imggray, 1.1, 3)  # 1.1 is %10 scale increased, 3 is iteration count
    detected_cars = cars_casc.detectMultiScale(imggray, 1.1, 3)  # 1.1 is %10 scale increased, 3 is iteration count

    # print(detected_bodies)

    for (x, y, w, h) in detected_bodies:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # green rectangle around bodies


    for (x, y, w, h) in detected_cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)  # green rectangle around cars

    cv2.imshow("body and car detection", frame)

    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()


