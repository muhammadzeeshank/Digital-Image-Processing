import cv2
import numpy as np
cv2.namedWindow('Color detectors')
# project


def nothing(x):
    print('')


colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)]
# creating Trackbars for choosing the color that has to be tracked
# upper bound
cv2.createTrackbar('upper hue', 'Color detectors', 153, 255, nothing)
cv2.createTrackbar('upper sat', 'Color detectors', 255, 255, nothing)
cv2.createTrackbar('upper val', 'Color detectors', 167, 255, nothing)
# lower bound
cv2.createTrackbar('lower hue', 'Color detectors', 64, 255, nothing)
cv2.createTrackbar('lower sat', 'Color detectors', 86, 255, nothing)
cv2.createTrackbar('lower val', 'Color detectors', 30, 255, nothing)


cap = cv2.VideoCapture(1)

# checking if camera is opened or not
if cap.isOpened():
    ret, frame = cap.read()
else:
    ret = False

# if camera is opened then remain in while loop otherwise break
while ret:
    # capturing video from camera
    ret, frame = cap.read()

    # converting BGR image to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Getting trackbar values
    u_hue = cv2.getTrackbarPos('upper hue', 'Color detectors')
    u_sat = cv2.getTrackbarPos('upper sat', 'Color detectors')
    u_val = cv2.getTrackbarPos('upper val', 'Color detectors')
    l_hue = cv2.getTrackbarPos('lower hue', 'Color detectors')
    l_sat = cv2.getTrackbarPos('lower sat', 'Color detectors')
    l_val = cv2.getTrackbarPos('lower val', 'Color detectors')
    upperb = np.array([u_hue, u_sat, u_val])
    lowerb = np.array([l_hue, l_sat, l_val])
    # making mask
    mask = cv2.inRange(hsv, lowerb, upperb)

    result = cv2.bitwise_and(frame, frame, mask=mask)
    # Adding the colour buttons to the live frame for colour access
    frame = cv2.rectangle(frame, (40, 0), (140, 65), (122, 122, 122), -1)
    y_and_r = 25
    cv2.circle(frame, (200, y_and_r), y_and_r, (255, 0, 0), -1)
    cv2.circle(frame, (275, y_and_r), y_and_r, (0, 255, 0), -1)
    cv2.circle(frame, (350, y_and_r), y_and_r, (0, 0, 255), -1)
    cv2.circle(frame, (425, y_and_r), y_and_r, (0, 165, 255), -1)
    cv2.circle(frame, (500, y_and_r), y_and_r, (0, 0, 0), -1)
    cv2.circle(frame, (575, y_and_r), y_and_r, (255, 255, 255), -1)

    cv2.putText(frame, "CLEAR ALL", (49, 33),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow('Tracking', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)

    # when Esc key is pressed loop will break and it will turn off
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
cap.release()
