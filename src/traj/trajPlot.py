import numpy as np
import pylab as pl
from matplotlib import animation
import time


class PlotTraj:

  def __init__(self):
    self.x     = []
    self.acc   = []
    self.speed = []
    self.pos   = []

  def addNewVal(self,value,time):
    self.x     += [time]
    self.acc   += [value[0]]
    self.speed += [value[1]]
    self.pos   += [value[2]]


  def plot(self):
    self.plot1  = pl.plot(self.x,self.acc,'r', label = 'acc')
    self.plot2, = pl.plot(self.x,self.speed,'b', label = 'speed')
    self.plot3, = pl.plot(self.x,self.pos,'g', label = 'pos')
    pl.title('Plot trajectory move')
    pl.xlabel('Plot by sequence')
    pl.ylabel('?')
    pl.legend(loc = 'upper left' , numpoints = 1)
    pl.show()


