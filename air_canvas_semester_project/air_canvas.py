import cv2

cv2.namedWindow('Color detectors')


colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)]


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

    # when Esc key is pressed loop will break and it will turn off
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
cap.release()
