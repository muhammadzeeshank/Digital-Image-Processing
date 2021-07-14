import cv2
import numpy as np
from collections import deque
cv2.namedWindow('Color detectors')
# project


def nothing(x):
    print('')


colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255),
          (0, 165, 255), (0, 0, 0), (255, 255, 255)]
bpoints = [deque(maxlen=512)]
gpoints = [deque(maxlen=512)]
rpoints = [deque(maxlen=512)]
opoints = [deque(maxlen=512)]
bkpoints = [deque(maxlen=512)]
bkpoints = [deque(maxlen=512)]
wpoints = [deque(maxlen=512)]
bindex = 0
gindex = 0
rindex = 0
oindex = 0
bkindex = 0
windex = 0
colorindex = 0
# creating Trackbars for choosing the color that has to be tracked
# upper bound
cv2.createTrackbar('upper hue', 'Color detectors', 118, 255, nothing)
cv2.createTrackbar('upper sat', 'Color detectors', 223, 255, nothing)
cv2.createTrackbar('upper val', 'Color detectors', 137, 255, nothing)
# lower bound
cv2.createTrackbar('lower hue', 'Color detectors', 84, 255, nothing)
cv2.createTrackbar('lower sat', 'Color detectors', 127, 255, nothing)
cv2.createTrackbar('lower val', 'Color detectors', 73, 255, nothing)


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
    # fliping arround x-axis
    frame = cv2.flip(frame, 1)

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
    y_and_r = 25
    bcenter = (200, y_and_r)
    gcenter = (275, y_and_r)
    rcenter = (350, y_and_r)
    ocenter = (425, y_and_r)
    bkcenter = (500, y_and_r)
    wcenter = (575, y_and_r)
    cv2.circle(frame, bcenter, y_and_r, colors[0], -1)
    cv2.circle(frame, gcenter, y_and_r, colors[1], -1)
    cv2.circle(frame, rcenter, y_and_r, colors[2], -1)
    cv2.circle(frame, ocenter, y_and_r, colors[3], -1)
    cv2.circle(frame, bkcenter, y_and_r, colors[4], -1)
    cv2.circle(frame, wcenter, y_and_r, colors[5], -1)
    frame = cv2.rectangle(frame, (40, 0), (140, 65), (122, 122, 122), -1)
    cv2.putText(frame, "CLEAR ALL", (49, 33),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    # finding contours
    contours = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    # finding contour with max area
    if len(contours) > 0:
        cont_max_area = max(contours, key=cv2.contourArea)
        center, radius = cv2.minEnclosingCircle(cont_max_area)
        center = (int(center[0]), int(center[1]))
        # drawing circle with center at the center of contour
        cv2.circle(frame, (center[0],
                           center[1]), int(radius), (0, 255, 0), 3)
        if (center[1] < 2*(y_and_r)):
            if (center[0] > 40 and center[0] < 140):
                bpoints = [deque(maxlen=512)]
                gpoints = [deque(maxlen=512)]
                rpoints = [deque(maxlen=512)]
                opoints = [deque(maxlen=512)]
                bkpoints = [deque(maxlen=512)]
                bkpoints = [deque(maxlen=512)]
                wpoints = [deque(maxlen=512)]
                bindex = 0
                gindex = 0
                rindex = 0
                oindex = 0
                bkindex = 0
                windex = 0

            elif (abs(center[0] - bcenter[0]) < radius):
                colorindex = 0
            elif (abs(center[0] - gcenter[0]) < radius):
                colorindex = 1
            elif (abs(center[0] - rcenter[0]) < radius):
                colorindex = 2
            elif (abs(center[0] - ocenter[0]) < radius):
                colorindex = 3
            elif (abs(center[0] - bkcenter[0]) < radius):
                colorindex = 4
            elif (abs(center[0] - wcenter[0]) < radius):
                colorindex = 5

        else:
            if colorindex == 0:
                bpoints[bindex].appendleft(center)
            elif colorindex == 1:
                gpoints[gindex].appendleft(center)
            elif colorindex == 2:
                rpoints[rindex].appendleft(center)
            elif colorindex == 3:
                opoints[oindex].appendleft(center)
            elif colorindex == 4:
                bkpoints[bkindex].appendleft(center)
            elif colorindex == 5:
                wpoints[windex].appendleft(center)

    else:
        bpoints.append(deque(maxlen=512))
        bindex += 1
        gpoints.append(deque(maxlen=512))
        gindex += 1
        rpoints.append(deque(maxlen=512))
        rindex += 1
        opoints.append(deque(maxlen=512))
        oindex += 1
        bkpoints.append(deque(maxlen=512))
        bkindex += 1
        wpoints.append(deque(maxlen=512))
        windex += 1

    allpoints = [bpoints, gpoints, rpoints, opoints, bkpoints, wpoints]
    for a in range(len(allpoints)):
        for i in range(len(allpoints[a])):
            for j in range(len(allpoints[a][i])):
                if allpoints[a][i][j] is None or allpoints[a][i][j-1] is None or j == 0:
                    continue
                cv2.line(frame, allpoints[a][i][j-1], allpoints[a][i]
                         [j], colors[a], 2)
    cv2.imshow('Tracking', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)

    # when Esc key is pressed loop will break and it will turn off
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
cap.release()
