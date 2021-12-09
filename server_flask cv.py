
from flask import Flask


app = Flask(__name__)

@app.route("/")

def helloworld():
    str = "Hello World!"
    return str

import cv2 as cv




if __name__ == '__main__' : 
    app.run(host='0.0.0.0', port='8081')



    # /dev/video0  /dev/video1
    cap = cv.VideoCapture(1)
    while cap.isOpened():
        ret, frame = cap.read()
        cv.imshow('webcam', frame)