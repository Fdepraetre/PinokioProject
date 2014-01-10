#import rotation
from math import *
import numpy as np
import sympy as sp

# Class for denavit-hartenberg model
# This class calculate the transformation between two referentials
class dh_model:

  # Initialise the denavit-Hartenberg Model
  def __init__(self):
     self.theta = 0.0
     self.a = 0.0
     self.d = 0.0
     self.alpha = 0.0
     self.rotx = np.zeros(4)
     self.rotz = np.zeros(4)
     self.trans = np.zeros(4)
     self._0Ti = np.zeros(4)

  # Set the model's value
  def set(self,new_theta,new_a,new_d,new_alpha):
     self.theta = new_theta * pi/180.0
     self.a = new_a
     self.d = new_d
     self.alpha = new_alpha * pi/180.0


  # Calculate the transform matrix with this dh-model
  def applyDH(self):
    # Appli the model and calculate the change matrix
    self.rotX()
    self.rotZ()
    self.Trans()
    self._0Ti = np.mat(self.rotz)*np.mat(self.trans)*np.mat(self.rotx)

  def getPi(self):
    _0OT = np.zeros(3)
    tmp = [[self._0Ti[0,3]],[self._0Ti[1,3]],[self._0Ti[2,3]]]
    _0OT = np.mat(tmp)
    return _0OT
     
  def rotZ(self):
    tmp = [[sp.cos(self.theta) , -sp.sin(self.theta) , 0 , 0]   ,
           [sp.sin(self.theta) , sp.cos(self.theta)  , 0 , 0]   ,
           [0                  , 0                   , 1 , 0]   ,
           [0                  , 0                   , 0 , 1] ]
    self.rotz = np.mat(tmp)
  def rotX(self):
    tmp = [[1 , 0                  , 0                   , 0]   ,
           [0 , sp.cos(self.alpha) , -sp.sin(self.alpha) , 0]   ,
           [0 , sp.sin(self.alpha) , sp.cos(self.alpha)  , 0]   ,
           [0 , 0                  , 0                   , 1] ]
    self.rotx = np.mat(tmp)
  def Trans(self):
    tmp = [[1 , 0 , 0 , self.a ] ,
           [0 , 1 , 0 , 0      ] ,
           [0 , 0 , 1 , self.d ] ,
           [0 , 0 , 0 , 1      ]]
    self.trans = np.mat(tmp)



def ComputeJOT(q,OT,n):
  [row,col] = OT.shape
  i = 0
  JOT = np.zeros((3,2))
  for j in range(len(q)):
      for i in range(row):
        JOT[i,j] = sp.diff(OT[i,0],q[j])

  return JOT

#def Compute_a_qd(JOT):
#  [row,col] = JOT.shape
#
#  try:
#     row == col
#  except:
#    print( "La matrice JOT n'est pas inversible")
  
