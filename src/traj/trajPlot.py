import numpy as np
import pylab as pl
from matplotlib import animation
import time


class PlotTraj:

  def __init__(self):
    self.x      = []
    self.posx   = []
    self.posy   = []
    self.posz   = []
    self.posxTheo   = []
    self.posyTheo   = []
    self.poszTheo   = []

  def addNewVal(self,value,time,valueTheorical=[0,0,0]):
    self.x        += [time]
    self.posx     += [value[0]]
    self.posy     += [value[1]]
    self.posz     += [value[2]]
    self.posxTheo += [valueTheorical[0]]
    self.posyTheo += [valueTheorical[1]]
    self.poszTheo += [valueTheorical[2]]


  def plot(self):
    self.plot1  = pl.plot(self.x,self.posx,'r', label = 'real X')
    self.plot2, = pl.plot(self.x,self.posy,'b', label = 'real Y')
    self.plot3, = pl.plot(self.x,self.posz,'g', label = 'real Z')
    self.plot4  = pl.plot(self.x,self.posxTheo,'c', label = 'theorical X')
    self.plot5, = pl.plot(self.x,self.posyTheo,'m', label = 'theorical Y')
    self.plot6, = pl.plot(self.x,self.poszTheo,'y', label = 'theorical Z')
    pl.title('Plot trajectory move')
    pl.xlabel('Plot by sequence')
    pl.ylabel('value')
    pl.legend(loc = 'upper left' , numpoints = 1)
    pl.show()


