
import threading
from flask import Flask, Response

video_frame = ''

app = Flask(__name__)
@app.route("/")

def helloworld() :
    str = "Hello World!"
    return str


# need install for opencv on raspbi :
# ~$ sudo apt-get install -y libatlas-base-dev
# ~$ python -m pip install -U pip
# ~$ python -m pip install -U numpy 



import cv2 as cv

def encodeframe() :
    global video_frame
    while True :
        ret, encoded_image = cv.imencode('.jpg', video_frame, )
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encoded_image) + b'\r\n')
    return 


@app.route('/streaming')
def streamframe() : 
    return Response(encodeframe(), mimetype="multipart/x-mixed-replace; boundary=frame")


def captureframe() :
    global video_frame
    cap = cv.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        cv.imshow('webcam', frame)
        ##################
        #화면이 뒤집혔다면 두번째 파라미터가 각도
        #frame = cv.rotate(frame, cv.ROTATE_180)
        video_frame = frame.copy()
        cv.waitKey(15)
        pass

if __name__ == '__main__' : 
    
    # /dev/video0  /dev/video1
    cap_thread = threading.Thread(target=captureframe)
    cap_thread.daemon = True    
    cap_thread.start()

    app.run(host='0.0.0.0', port='8080')
    pass