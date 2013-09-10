
# coding=utf8

from ueberschrift import *

col = valueDialog('Piraten OpenAntrag Flyer','Spalte')
y = valueDialog('Piraten OpenAntrag Flyer','y-Koordinate (pt)')

ideo = valueDialog('Piraten OpenAntrag Flyer',
"""
Ideogramm:
Copy&Paste ODER
1 für "Personen"
""")

if (ideo=="1"):
    ideo=""

text = valueDialog('Piraten OpenAntrag Flyer','Text')

DrawHeader(int(col),int(y),ideo,text)
