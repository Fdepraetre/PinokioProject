from math import *
import numpy as np
import sympy as sp

def rotZ(theta):
  return np.mat( [[sp.cos(theta) , -sp.sin(theta) , 0 , 0],
                  [sp.sin(theta) , sp.cos(theta)  , 0 , 0],
                  [0             , 0              , 1 , 0],
                  [0             , 0              , 0 , 1]])

def rotX(alpha):
  return np.mat( [[1 , 0             , 0              , 0],
                 [0 , sp.cos(alpha) , -sp.sin(alpha) , 0],
                 [0 , sp.sin(alpha) , sp.cos(alpha)  , 0],
                 [0 , 0             , 0              , 1]])

def trans(x, y, z):
  return  np.mat( [[1 , 0 , 0 , x ],
                   [0 , 1 , 0 , y ],
                   [0 , 0 , 1 , z ],
                   [0 , 0 , 0 , 1 ]])
 
def dhMatrix(thetaDegree, a, d, alphaDegree):
  theta = thetaDegree * pi/180.0
  alpha = alphaDegree * pi/180.0
  # Calculate the transform matrix with this dh-model
  return rotZ(theta) * trans(a,0,d) * rotX(alpha)
     
 
