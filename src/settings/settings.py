import yaml
import os
import subprocess

class Settings: 
  def __init__(self, path = "../settings/settings.yaml"):
    with open(path, 'r') as fh:
         self.settings = yaml.load(fh)

  def get(self):
    return self.settings
 
class MotorSettings(Settings):
  def __init__(self, path = "../settings/motorSettings.yaml"):
    Settings.__init__(self, path)

 
class ModelSettings(Settings):
  def __init__(self, path = "../settings/modelSettings.yaml"):
    Settings.__init__(self, path)

class ArduinoSettings(Settings):
  def __init__(self, path = "../settings/arduinoSettings.yaml"):
    Settings.__init__(self, path)


