import cv2

class camera:
    def __init__(self, cameraId=0):
        self.cameraId=cameraId
        self.camera = cv2.VideoCapture(self.cameraId)

    def getFrame(self):
        if not self.camera.isOpened():
            return b'noData'
        ret, img = self.camera.read()
        ret, jpeg = cv2.imencode('.jpg', img)
        return jpeg.tobytes()
