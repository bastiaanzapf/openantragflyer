
# coding=utf8

from ueberschrift import *

col = valueDialog('Piraten OpenAntrag Flyer','Spalte')
y = valueDialog('Piraten OpenAntrag Flyer','y-Koordinate (pt)')

ideo = valueDialog('Piraten OpenAntrag Flyer',
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

text = valueDialog('Piraten OpenAntrag Flyer','Text')

DrawHeader(int(col),int(y),ideo,text)
