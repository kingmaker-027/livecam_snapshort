#capture n ON.of picture while cam is openeach img has 2sec gap

import cv2
import time
cv2.namedWindow("Live Capture", cv2.WINDOW_NORMAL)
cap = cv2.VideoCapture(0)
counter = 1
store_path = "image/"
while counter <= 4 :
    ret, frame = cap.read()
    cv2.imshow("Live Capture", frame)
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S", time.gmtime())
    save_path = store_path+"img_{}_{}.png".format(counter,timestamp)
    cv2.imwrite(save_path, frame)  
    counter += 1
    time.sleep(2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
