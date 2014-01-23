import VideoStream
import numpy
import cv2
import cv

class FaceDetection:
  def __init__(self, path='../xml/haarcascade_frontalface_default.xml'):
    self.face_cascade = cv2.CascadeClassifier(path)
    self.faces = []

  def display(self,frame):
    """ Display the last faces detected on the frame given in parameter """
    for (x,y,r) in self.faces:
      cv2.circle(frame,(x,y),r,(0,0,255),2)

  def computeFace(self,frame):
    """ Detecte the faces on the frame given in paramter"""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    facesOutput = self.face_cascade.detectMultiScale(gray, 1.3, 5)
    self.faces = []
    for (x,y,w,h) in facesOutput:
      position = (x+w/2,y+h/2,int(numpy.floor(numpy.sqrt((h/2)*(h/2)+(w/2)*(w/2)))))
      self.faces += [position]

  def isFaceDetected(self):
    """ Is a face detected ?"""
    return self.faces != []

class FaceStream(VideoStream.VideoStream):
  def __init__(self, camId = 0, resWidth = 320, resHeight = 240):
    VideoStream.VideoStream.__init__(self,camId,resWidth,resHeight)
    self.faceDetection = FaceDetection()

  def nextFrame(self):
    """ Read the next frame from the video capture and compute face """
    VideoStream.VideoStream.nextFrame(self)
    self.faceDetection.computeFace(self.frame)

  def isFaceDetected(self):
    """ Is a face detected ? """
    return self.faceDetection.isFaceDetected()

  def getFacePosition(self):
    """ """
    print self.faceDetection.faces[0][:2]    
    return self.faceDetection.faces[0][:2]    

  def display(self):
    """ Display current frame with circle around face """ 
    self.faceDetection.display(self.frame)
    cv2.imshow('FaceDetection',self.frame)

