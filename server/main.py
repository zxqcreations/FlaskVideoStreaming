from flask import Flask, render_template, Response
import threading
import numpy
from server.camera import camera

app = Flask(__name__)
mainFrame = numpy.zeros([244,244,3])

@app.route('/')
def index():
    return render_template('index.html')

def getFrame(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type:image/jpeg\r\n\r\n'+frame+b'\r\n\r\n')

def getFrame(camera):
    global mainFrame
    mainFrame = camera.getFrame()

@app.route('/getimg')
def getimg():
    return Response(getFrame(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=='__main__':
    cmr = camera(0)
    frameGenerator = threading.Thread(target=getFrame, args=(cmr))
    frameGenerator.run()
    app.run(host='0.0.0.0', debug=True)
