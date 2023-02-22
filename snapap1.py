from flask import Flask, request
import cv2
import os

app = Flask(__name__)
@app.route('/capture_images', methods=['POST'])
def capture_images():
    # initialize the video capture object
    cap = cv2.VideoCapture(0)
    # define the directory for storing the captured images
    image_dir =  'image' #'C:/Users/NAVIN K S/sdsd'
    # loop through 5 frames and save them as images
    for i in range(5):
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(os.path.join(image_dir, f'image_{i}.jpg'), frame)
    # release the video capture object
    cap.release()
    return 'Images captured successfully'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

#  for run open cmd curl -X POST http://localhost:5000/capture_images