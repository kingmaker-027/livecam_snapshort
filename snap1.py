#capture continuous picture while cam is open


import cv2
import time 
cv2.namedWindow("Live Capture", cv2.WINDOW_NORMAL)
cap = cv2.VideoCapture(0)
counter = 0
store_path = "image/"
while True:
    ret, frame = cap.read()
    cv2.imshow("Live Capture", frame)
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S", time.gmtime())
    save_path = store_path+"img_{}_{}.png".format(counter,timestamp)
    cv2.imwrite(save_path, frame)
    counter += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()