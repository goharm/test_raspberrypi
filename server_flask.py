
from flask import Flask


app = Flask(__name__)

@app.route("/")

def helloworld():
    str = "Hellow World!"
    return str

import cv2 as cv




if __name__ == '__main__' : 
    app.run(host='0.0.0.0', port='8080')

