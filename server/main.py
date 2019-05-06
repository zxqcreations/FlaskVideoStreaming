from flask import Flask, render_template, Response
import threading
import numpy
import cv2, time
from camera import camera

app = Flask(__name__)
#mainFrame = b''
lock = threading.Lock()

@app.route('/')
def index():
    print('request received')
    return render_template('index.html')

def getStream(camera):
    #global mainFrame
    while True:
        #print(mainFrame)
        #lock.acquire()
        mainFrame = camera.getFrame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n'+mainFrame+b'\r\n\r\n')
        #time.sleep(0.05)
        #lock.release()

def getFrame(camera):
    global mainFrame
    while True:
        lock.acquire()
        mainFrame = camera.getFrame()
        lock.release()
        #print(mainFrame)

@app.route('/getimg')
def getimg():
    #print(mainFrame)
    #lock.acquire()
    return Response(getStream(camera()), mimetype='multipart/x-mixed-replace; boundary=frame')
    #lock.release()

if __name__=='__main__':
    #cmr = camera(0)
    #frameGenerator = threading.Thread(target=getFrame, args=(cmr,))
    #frameGenerator.start()
    app.run(host='0.0.0.0', debug=True, port=5000)
    #app_run = threading.Thread(target=runapp, args=())
    #app_run.start()


