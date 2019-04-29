from flask import Flask, render_template, Response
import threading
import numpy
import cv2, time
from camera import camera

app = Flask(__name__)
mainFrame = b''

@app.route('/')
def index():
    print('request received')
    return render_template('index.html')

def getStream():
    global mainFrame
    while True:
        #print(mainFrame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n'+mainFrame+b'\r\n\r\n')
        time.sleep(0.05)

def getFrame(camera):
    global mainFrame
    while True:
        mainFrame = camera.getFrame()
        #print(mainFrame)

@app.route('/getimg')
def getimg():
    print(mainFrame)
    return Response(getStream(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=='__main__':
    cmr = camera(0)
    frameGenerator = threading.Thread(target=getFrame, args=(cmr,))
    frameGenerator.start()
    app.run(host='0.0.0.0', debug=True, port=5000)
    #app_run = threading.Thread(target=runapp, args=())
    #app_run.start()


