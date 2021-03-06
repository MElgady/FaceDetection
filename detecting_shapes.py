# Rewritten code due to accidental deletion
# from Source Control

# This lecture shows how to detect moving
# objects using OpenCV.

import cv2
import time

first_frame = None

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()

    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grey = cv2.GaussianBlur(grey, (21, 21), 0)

    if first_frame is None:
        first_frame = grey
        continue

    delta_frame = cv2.absdiff(first_frame, grey)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    (cnts, _) = cv2.findContours(thresh_frame.copy(),
                                 cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue

        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    cv2.imshow("Grey Frame", grey)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Colour Frame", frame)

    key = cv2.waitKey(1)
    print(grey)
    print(delta_frame)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
