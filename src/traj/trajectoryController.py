import time 
import numpy as np
import trajPlot

class TrajectoryController:

  def __init__(self,speedMax,accMax,size=3):
    self.initPoint = np.zeros((size,1))
    self.endPoint  = np.zeros((size,1))
    self.speedMax  = speedMax
    self.accMax    = accMax
    self.speed     = 0
    self.D         = np.zeros((size,1))
    self.timef     = 0
    self.position  = np.zeros((size,1))

  def set(self,initPoint,endPoint):
    self.initPoint = initPoint
    self.endPoint  = endPoint
    self.timeInit  = time.time()
    
    self.D = np.subtract(endPoint,initPoint)

    Dj           = np.linalg.norm(self.D)
    Dj2          = 2 * np.sqrt(Dj/ self.accMax)
    Dj           = 2 * Dj / self.speedMax
    self.timef   = max(Dj,Dj2)

    # q(t) = qi + A *D * t^2

    self.A = 2 / (self.timef * self.timef)
    self.B = 4 / self.timef 

  def update(self):

    # The +0.1 is to anticipate the next value
    currentTime = time.time() - self.timeInit +0.01

    if currentTime < self.timef/2:
      acc   = self.accMax
      speed = min(self.speedMax,self.accMax * currentTime)
      pos   = self.A * currentTime * currentTime
    elif currentTime < self.timef:
      acc   = - self.accMax
      speed = min(self.speedMax,- self.accMax * currentTime + self.accMax * self.timef)
      pos   = (-1 + self.B * currentTime - self.A * currentTime * currentTime )
    else :
      acc   = 0
      speed = 0
      pos   = (-1 + self.B * self.timef - self.A * self.timef * self.timef )
 

    self.position = np.multiply(self.D,pos)
    self.position += self.initPoint
    self.speed = speed

    return self.isEnded()

  def isEnded(self):
    if time.time() - self.timeInit > self.timef:
        return True
    else :
        return False
