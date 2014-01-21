class Robot:

  def __init__(self):
     self.dh   = []
     self._0Ti = np.zeros(4)
     self._0OT = np.zeros(3)

  def setModel(self,dh_model):
    for dh in dh_model:
      self.dh += dh

  def ComputeModel(self):
    for dh in self.dh:
      self._OTk *= dh._0Ti
      
  def getPi(self):
    tmp = [[self._0Ti[0,3]],[self._0Ti[1,3]],[self._0Ti[2,3]]]
    self._0OT = np.mat(tmp)
    return self._0OT
   

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
 
