import sys
import wx
import time
import threading
sys.path.insert(0, "../settings/")
import settings
sys.path.insert(0, "../control/")
import motorControl
sys.path.insert(0,"../traj/")
import trajectoryController

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, (800, 600))
        #panel = wx.Panel(self, -1, style=wx.SIMPLE_BORDER)

        vbox = wx.BoxSizer(wx.VERTICAL)
        hboxcontrols = wx.BoxSizer(wx.HORIZONTAL)
        hboxlist = wx.BoxSizer(wx.HORIZONTAL)

        vbox.Add(hboxcontrols)
        vbox.Add(hboxlist, 1, wx.EXPAND)

        motorSettings = settings.MotorSettings().get()
        self.motorController = motorControl.MotorControl(motorSettings)
        self.motorController.setAllSpeed(100)
        #parse motor setting to get min and max angle, store result in hash motors
        motors = {}
        motorsConfig=motorSettings["motorConfig"]
        for motor in motorsConfig:
            motors[motor[3]] = [motor[1], motor[2]]


        
        #visual element

        #bowl button
        pnlBowl = wx.Panel(self, -1, style=wx.SIMPLE_BORDER)
        hboxcontrols.Add(pnlBowl, 1, wx.ALL |wx.EXPAND, 1)
        self.sldBowl = wx.Slider(pnlBowl, -1, motors["bowl"][0], motors["bowl"][0], motors["bowl"][1], wx.DefaultPosition, (-1, -1), wx.SL_VERTICAL | wx.SL_LABELS)
        textBowl = wx.StaticText(pnlBowl, -1, 'Bowl')
        vboxBowl = wx.BoxSizer(wx.VERTICAL)
        vboxBowl.Add(self.sldBowl, 1, wx.CENTER, 0)
        vboxBowl.Add(textBowl, 1, wx.CENTER)
        pnlBowl.SetSizer(vboxBowl)

        #bottom button
        pnlBottom = wx.Panel(self, -1, style=wx.SIMPLE_BORDER)
        hboxcontrols.Add(pnlBottom, 1, wx.ALL | wx.EXPAND, 1)
        self.sldBottom = wx.Slider(pnlBottom, -1, motors["bottom"][1], motors["bottom"][0], motors["bottom"][1], wx.DefaultPosition, (-1, -1), wx.SL_VERTICAL | wx.SL_LABELS)
        textBottom = wx.StaticText(pnlBottom, -1, 'Bottom')
        vboxBottom = wx.BoxSizer(wx.VERTICAL)
        vboxBottom.Add(self.sldBottom, 1, wx.CENTER)
        vboxBottom.Add(textBottom, 1, wx.CENTER)
        pnlBottom.SetSizer(vboxBottom)

        #middle button
        pnlMiddle = wx.Panel(self, -1, style=wx.SIMPLE_BORDER)
        hboxcontrols.Add(pnlMiddle, 1, wx.ALL | wx.EXPAND, 1)
        self.sldMiddle = wx.Slider(pnlMiddle, -1, motors["mid"][0], motors["mid"][0], motors["mid"][1], wx.DefaultPosition, (-1, -1), wx.SL_VERTICAL | wx.SL_LABELS)
        textMiddle = wx.StaticText(pnlMiddle, -1, 'Middle')
        vboxMiddle= wx.BoxSizer(wx.VERTICAL)
        vboxMiddle.Add(self.sldMiddle, 1, wx.CENTER)
        vboxMiddle.Add(textMiddle, 1, wx.CENTER)
        pnlMiddle.SetSizer(vboxMiddle)

        #top button
        pnlTop = wx.Panel(self, -1, style=wx.SIMPLE_BORDER)
        hboxcontrols.Add(pnlTop, 1, wx.ALL | wx.EXPAND, 1)
        self.sldTop = wx.Slider(pnlTop, -1, motors["top"][0], motors["top"][0], motors["top"][1], wx.DefaultPosition, (-1, -1), wx.SL_VERTICAL | wx.SL_LABELS)
        textTop = wx.StaticText(pnlTop, -1, 'Top')
        vboxTop = wx.BoxSizer(wx.VERTICAL)
        vboxTop.Add(self.sldTop, 1, wx.CENTER)
        vboxTop.Add(textTop, 1, wx.CENTER)
        pnlTop.SetSizer(vboxTop)

        #head button
        pnlHead = wx.Panel(self, -1, style=wx.SIMPLE_BORDER)
        hboxcontrols.Add(pnlHead, 1, wx.ALL | wx.EXPAND, 1)
        self.sldHead = wx.Slider(pnlHead, -1, motors["head"][0], motors["head"][0], motors["head"][1], wx.DefaultPosition, (-1, -1), wx.SL_VERTICAL | wx.SL_LABELS)
        textHead = wx.StaticText(pnlHead, -1, 'Head')
        vboxHead = wx.BoxSizer(wx.VERTICAL)
        vboxHead.Add(self.sldHead, 1, wx.CENTER)
        vboxHead.Add(textHead, 1, wx.CENTER)
        pnlHead.SetSizer(vboxHead)
        
        #buttons
        pnlButtons = wx.Panel(self, -1, style=wx.SIMPLE_BORDER)
        hboxcontrols.Add(pnlButtons, 1, wx.EXPAND | wx.ALL, 1)
        vboxButton = wx.BoxSizer(wx.VERTICAL)
        
        gotoButton = wx.Button(pnlButtons, 7, 'Go To')
        vboxButton.Add(gotoButton, 1, wx.ALIGN_CENTER | wx.TOP, 15)
        wx.EVT_BUTTON(self, 7, self.OnGoto)

        savePositionButton = wx.Button(pnlButtons, 8, 'Save position to list')
        vboxButton.Add(savePositionButton, 1, wx.ALIGN_CENTER | wx.TOP, 15)
        wx.EVT_BUTTON(self, 8, self.OnSavePosition)

        deletePositionButton = wx.Button(pnlButtons, 9, 'delete position from list')
        vboxButton.Add(deletePositionButton, 1, wx.ALIGN_CENTER | wx.TOP, 15)
        wx.EVT_BUTTON(self, 9, self.OnDeletePosition)

        playButton = wx.Button(pnlButtons, 10, 'Play')
        vboxButton.Add(playButton, 1, wx.ALIGN_CENTER | wx.TOP, 15)
        wx.EVT_BUTTON(self, 10, self.OnPlay)
        
        stopButton = wx.Button(pnlButtons, 11, 'Stop')
        vboxButton.Add(stopButton, 1, wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, 15)
        wx.EVT_BUTTON(self, 11, self.OnStop)
        
        pnlButtons.SetSizer(vboxButton)
        
        #list of position
        self.positionList = wx.ListCtrl(self, -1, style=wx.LC_REPORT)
        self.positionList.InsertColumn(0, 'bowl')
        self.positionList.InsertColumn(1, 'bottom')
        self.positionList.InsertColumn(3, 'middle')
        self.positionList.InsertColumn(4, 'top')
        self.positionList.InsertColumn(5, 'head')
        hboxlist.Add(self.positionList, 1, wx.EXPAND)


        #panel.SetSizer(vbox)
        self.SetSizer(vbox)

    def OnPlay(self, event):
        count = self.positionList.GetItemCount()
        list=[]
        for row in range(count):
            list2 =[]
            value = int(self.positionList.GetItem(row, 0).GetText())
            list2.append(["bowl", value])
            value = int(self.positionList.GetItem(row, 1).GetText())
            list2.append(["bottom", value])
            value = int(self.positionList.GetItem(row, 2).GetText())
            list2.append(["mid", value])
            value = int(self.positionList.GetItem(row, 3).GetText())
            list2.append(["top", value])
            value = int(self.positionList.GetItem(row, 4).GetText())
            list2.append(["head", value])
            list.append(list2)

        #thread for sequence of movement
        self.play = PlayMove(self.motorController)
        self.play.listMove(list)
        self.play.start()

    def OnStop(self, event):
        #print "caramel"
        self.play.stop()

    def OnGoto(self, event):
        list=[]
        list.append(["bowl", self.sldBowl.GetValue()])
        list.append(["bottom", self.sldBottom.GetValue()])
        list.append(["mid", self.sldMiddle.GetValue()])
        list.append(["top", self.sldTop.GetValue()])
        list.append(["head", self.sldHead.GetValue()])
        self.motorController.setAllSpeed(100)
        self.motorController.setMotorsByName(list)

    def OnSavePosition(self, event):
        print "biscuit"
        num_positions = self.positionList.GetItemCount()
        self.positionList.InsertStringItem(num_positions, str(self.sldBowl.GetValue()))
        self.positionList.SetStringItem(num_positions, 1, str(self.sldBottom.GetValue()))
        self.positionList.SetStringItem(num_positions, 2, str(self.sldMiddle.GetValue()))
        self.positionList.SetStringItem(num_positions, 3, str(self.sldTop.GetValue()))
        self.positionList.SetStringItem(num_positions, 4, str(self.sldHead.GetValue()))

    def OnDeletePosition(self, event):
        print "framboise"
        while self.positionList.GetSelectedItemCount() != 0 :
            index = self.positionList.GetFirstSelected()
            self.positionList.DeleteItem(index)

class MyApp(wx.App):
    def OnInit(self):
        #wx.App.__init__(self)
        #motorsConfig = [[0, 0, 100, "bowl"], [0, 9, 100, "bottom"], [1, 30, 100, "middle"], [2, 45, 1000, "top"], [3, 10, 400, "head"]]
        frame = MyFrame(None, -1, 'Pinokio alpha 0.1')
        frame.Show(True)
        frame.Centre()
        return True

def getValueList(l):
  res = []
  for move in l:
    res.append(move[1])
  return res

class PlayMove(threading.Thread):
    def __init__(self, motorController):
        threading.Thread.__init__(self)
        self.play = False
        self.stoplock = threading.Lock()
        self.motorController = motorController

    def run(self):
        self.play = True
        index = 0

        #Go to initial position
        print self.moves[0]
        self.motorController.setMotorsByName(self.moves[0])
        time.sleep(3)
        
        if len(self.moves) > 1 :

          traj = trajectoryController.TrajectoryController(100,40,len(self.moves[0]))
          traj.set(getValueList(self.moves[0]),getValueList(self.moves[1]))
          while self.play :
            if not traj.update():
              self.motorController.setAllSpeed(int(traj.speed))
              values = [["bowl",traj.position[0]],
                        ["bottom",traj.position[1]],
                        ["mid",traj.position[2]],
                        ["top",traj.position[3]],
                        ["head",traj.position[4]]]
              self.motorController.setMotorsByName(values)
            else :
              index = (index + 1) % len(self.moves)
              traj.set(getValueList(self.moves[index]),getValueList(self.moves[(index + 1)%len(self.moves)]))
              

    def stop(self):
        with self.stoplock:
            self.play = False
            print "caramel2"

    def listMove(self, list):
        with self.stoplock:
            self.moves = list

motorsConfig = [[0, 0, 100, "bowl"], [0, 9, 100, "bottom"], [1, 30, 100, "mid"], [2, 45, 1000, "top"], [3, 10, 400, "head"]]
app = MyApp(0)
app.MainLoop()
