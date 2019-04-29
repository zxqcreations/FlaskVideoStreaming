from flask import Flask, render_template, Response
import threading
import numpy
import cv2
from camera import camera

app = Flask(__name__)
mainFrame = numpy.zeros([244,244,3])

@app.route('/')
def index():
    print('request received')
    return render_template('index.html')

def getStream():
    global mainFrame
    while True:
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n'+mainFrame+b'\r\n\r\n')

def getFrame(camera):
    global mainFrame
    while True:
        mainFrame, img = camera.getFrame()

@app.route('/getimg')
def getimg():
    return Response(getStream(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=='__main__':
    cmr = camera(0)
    frameGenerator = threading.Thread(target=getFrame, args=(cmr,))
    frameGenerator.start()
    app.run(host='0.0.0.0', debug=True, port=5000)
    #app_run = threading.Thread(target=runapp, args=())
    #app_run.start()


