
# coding=utf8

from ueberschrift import *

dialogheader='Piraten OpenAntrag Flyer';

col = valueDialog(dialogheader,'Spalte')
y = valueDialog(dialogheader,'y-Koordinate (pt)')

ideo = valueDialog(dialogheader,
"""
Ideogramm:
Copy&Paste ODER
1 für "Personen/Parlament"
2 für "Home"
3 für "Balkendiagramm"
4 für "Lupe"
5 für "Schildchen"
6 für "RSS/Rundfunk"
7 für "Netzwerk/Weltkugel"
8 für "Fragezeichen"
9 für "Megaphon"
10 für "Info"
11 für "Idee/Glühbirne"
""")

if (ideo=="1"):
    ideo=""
elif (ideo=="2"):
    ideo=""
elif (ideo=="3"):
    ideo=""
elif (ideo=="4"):
    ideo=""
elif (ideo=="5"):
    ideo=""
elif (ideo=="6"):
    ideo=""
elif (ideo=="7"):
    ideo=""
elif (ideo=="8"):
    ideo=""
elif (ideo=="9"):
    ideo=""
elif (ideo=="10"):
    ideo=""
elif (ideo=="11"):
    ideo=""

text = valueDialog(dialogheader,'Text')

iconright = valueDialog(dialogheader,'Icon nach Rechts (1) oder nach Links (0)?')

if (iconright=="0"):
    iconright=False
elif (iconright=="1"):
    iconright=True
else:
    iconright=False

DrawHeader(int(col),int(y),ideo,text,iconright)
