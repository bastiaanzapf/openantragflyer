
from scribus import *

obj=getSelectedObject()

propList = getPropertyNames(obj)
props=""
for p in propList:
  try:
     props = props + p + " (" + str(getPropertyCType(obj, p)) + "): "
     props = props + str(getProperty(obj, p))+"\n"
  except:
     nothing = "nothing"
     props = props + "\n"
     messageBox("Property Info for " + obj, "Below is a property list for the selected object named " + obj + "\n" + props, ICON_INFORMATION)

