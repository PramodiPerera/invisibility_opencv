
# required libraries
import cv2
import time
import numpy as np


cap = cv2.VideoCapture(0)
cap.set(3, 1280) # width of window
cap.set(4, 720)  # height of window
time.sleep(2)  # for the capturing
bg = 0    # background


# background
for i in range(50):
    success, bg = cap.read()


# capture new elements which come to bg
while cap.isOpened():
    success, img = cap.read()
    #img = cv2.flip(img, 1)     # to remove the mirror effect

    if success:
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


                             # H  S   V
        lower_blue = np.array([90,70,50])
        upper_blue = np.array([128,255,255])

        # img lies between the blue range
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        part1 = cv2.bitwise_and(bg, bg, mask=mask)

        mask = cv2.bitwise_not(mask)
        
        part2 = cv2.bitwise_and(img, img, mask=mask)
        cv2.imshow("Output", part2 + part1)
        if cv2.waitKey(5) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
