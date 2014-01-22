import cv2
import cv

class VideoStream:
  def __init__(self, camId = 0, resWidth = 320, resHeight = 240):
    self.capture = cv2.VideoCapture(camId)  
    self.capture.set(cv.CV_CAP_PROP_FRAME_WIDTH, resWidth)  
    self.capture.set(cv.CV_CAP_PROP_FRAME_HEIGHT, resHeight)
    self.frame = []

  def getFrame(self):
    """ Get the current frame """
    return self.frame

  def nextFrame(self):
    """ Read the next frame from the video capture """
    for i in range(5):
      ret, self.frame = self.capture.read()
  
  def display(self):
    """ Display current frame """ 
    cv2.imshow('VideoStream',self.frame)

  def getRes(self):
    """ """
    x = self.capture.get(cv.CV_CAP_PROP_FRAME_WIDTH)
    y = self.capture.get(cv.CV_CAP_PROP_FRAME_HEIGHT)
    return (x,y)
