import numpy as np
import pylab as pl

class Ploting:

  def __init__(self):

    self.x  = []
    self.q1 = []
    self.q2 = []
    self.q3 = []
    self.q4 = []
    self.q5 = []

  def addNewVal(self,value,time):
    self.x  += [time]
    self.q1 += [value[0]]
    self.q2 += [value[1]]
    self.q3 += [value[2]]
    self.q4 += [value[3]]
    self.q5 += [value[4]]

  def plot(self):
    self.plot1 = pl.plot(self.x,self.q1,'r',animated = True)
    self.plot2 = pl.plot(self.x,self.q2,'b',animated = True)
    self.plot3 = pl.plot(self.x,self.q3,'g',animated = True)
    self.plot4 = pl.plot(self.x,self.q4,'c',animated = True)
    self.plot5 = pl.plot(self.x,self.q5,'m',animated = True)
    pl.title('Plot Different articulations angles')
    pl.xlabel('Plot by sequence')
    pl.ylabel('Angle in tick motor')
    pl.legend([plot1,plot2,plot3,plot4,plot5],('q1','q2','q3','q4','q5'), 'best' , numpoints=1)
    pl.show()

  def update(self):
    
    self.plot1.set_ydata(self.q1)
    self.plot2.set_ydata(self.q2)
    self.plot3.set_ydata(self.q3)
    self.plot4.set_ydata(self.q4)
    self.plot5.set_ydata(self.q5)

if (__name__) == '__main__':

  x =[1,2,3,4,5]
  y1 =[220,230,250,150,200]
  y2 =[200,160,150,100,300]
  y3 =[180,160,150,150,300]
  y4 =[220,230,250,150,200]
  y5 =[200,160,150,100,300]

  plotter = Ploting()

  plotter.addNewVal(y1) 
  plotter.addNewVal(y2) 
  plotter.addNewVal(y3)
  plotter.addNewVal(y4) 
  plotter.addNewVal(y5) 
  plotter.plot()
