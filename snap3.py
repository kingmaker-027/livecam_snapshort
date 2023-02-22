#capture n ON.of picture while cam is open each img b/w n fps gap

import cv2
import time 

cv2.namedWindow("Live Capture", cv2.WINDOW_NORMAL)
cap = cv2.VideoCapture(0)
i = 0
frame_skip = 10
counter = 1
store_path = "image/"
# while True:
#     ret, frame = cap.read()
#     cv2.imshow("Live Capture", frame)
#     if i > frame_skip - 1:
#         timestamp = time.strftime("%Y-%m-%d_%H-%M-%S", time.gmtime())
#         save_path = store_path+"img_{}_{}.png".format(counter,timestamp)
#         cv2.imwrite(save_path, frame)
#         i = 0
#         counter += 1
#         continue
#     i += 1
#     if counter > 10:
#         break
while counter <= 5 :
    ret, frame = cap.read()
    cv2.imshow("Live Capture", frame)
    if i > frame_skip - 1:
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S", time.gmtime())
        save_path = store_path+"img_{}_{}.png".format(counter,timestamp)
        cv2.imwrite(save_path, frame)
        i = 0
        counter += 1
        continue
    i += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()                                                                                     
cv2.destroyAllWindows()