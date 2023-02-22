import cv2
import time
cv2.namedWindow("Live Capture", cv2.WINDOW_NORMAL)
cap = cv2.VideoCapture(0)
frame_rate = 30
frame_interval = 1000/frame_rate
while True:
    ret, frame = cap.read()
    cv2.imshow("Live Capture", frame)
    key = cv2.waitKey(int(frame_interval)) & 0xFF
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
