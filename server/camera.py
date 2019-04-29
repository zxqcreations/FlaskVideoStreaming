import cv2

class camera:
    def __init__(self, cameraId=0):
        self.cameraId=cameraId
        self.camera = cv2.VideoCapture(self.cameraId + cv2.CAP_DSHOW)

    def getFrame(self):
        if not self.camera.isOpened():
            return b'cannot open camera'
        ret, img = self.camera.read()
        if ret:
            #cv2.imshow('img', img)
            ret, jpeg = cv2.imencode('.jpg', img)
            return jpeg.tobytes()
        return b'noData'
