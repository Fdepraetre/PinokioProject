import time 
import numpy as np
import trajPlot

class TrajectoryController:

  def __init__(self,speedMax,accMax):
    self.initPoint = np.zeros((3,1))
    self.endPoint  = np.zeros((3,1))
    self.speedMax  = speedMax
    self.accMax    = accMax
    self.speed     = 0
    self.D         = np.zeros((3,1))
    self.timef     = 0
    self.position  = np.zeros((3,1))

  def set(self,initPoint,endPoint):
    self.initPoint = initPoint
    self.endPoint  = endPoint
    self.timeInit  = time.time()
    
    self.D = np.subtract(endPoint,initPoint)

    Dj           = np.linalg.norm(self.D)
    Dj2          = 2 * np.sqrt(Dj/ self.accMax)
    Dj           = 2 * Dj / self.speedMax
    self.timef   = max(Dj,Dj2)
#    self.timef  += timeInit

    # q(t) = qi + A *D * t^2

    self.A = 2 / (self.timef * self.timef)
    self.B = 4 / self.timef 

  def update(self):

    currentTime = time.time() - self.timeInit

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
      pos   = 0
 

    self.position = np.multiply(self.D,pos)
    self.position += self.initPoint
    self.speed = speed

    return self.isEnded()

  def isEnded(self):
    if time.time() - self.timeInit > self.timef:
        return True
    else :
        return False


if (__name__) =='__main__' :

  trajectory = TrajectoryController(10,5)
  timeInit = time.time()
  posMesured = [[0]]
  trajectory.set([[0],[0],[0]],[[10],[15],[60]])
  print trajectory.timef
  plotter = trajPlot.PlotTraj()
  plotter2 = trajPlot.PlotTraj()
  pos = 0
  [acc,speed,pos] = trajectory.update()
  while  (time.time()-timeInit) < trajectory.timef:
    [acc,speed,pos] = trajectory.update()
    print "update"
    print pos
    print trajectory.position
    plotter.addNewVal([acc,speed,trajectory.position[0]],time.time()-timeInit)
    plotter2.addNewVal([trajectory.position[0],trajectory.position[1],trajectory.position[2]],time.time()-timeInit)
    
  plotter.plot()
  plotter2.plot()


