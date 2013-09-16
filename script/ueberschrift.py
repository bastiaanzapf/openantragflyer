
# coding=utf8

try:
    from scribus import *
except ImportError:
    print "This script only runs from within Scribus."
    sys.exit(1)

from util import *

colwidth=280
overprint=1

def DrawHeaderText(title,iconright):
    global key
    global col,y
    global guideleft

    # 2/3-1/2 = 1/6
    # 3/10-1/3

    if (not(iconright)):
        x=guideleft+(3*colwidth/10)
    else:
        x=guideleft+(1*colwidth/10) 
    text=createText(x,y+10,(2*colwidth/3),30)
    insertText(title, 0, text)  
    setFontSize(24,text)
    setFont("Bebas Neue Regular",text)
    setTextAlignment(ALIGN_CENTERED, text)
    setTextColor("Openantrag-Blau-2",text)
    objname='OA_' + key + '_TEXT'
    setProperty(text,'itemName',objname)
#    setOffsetPolicy(1,text)

    return objname

def DrawIdeogram(ideogram,iconright):
    global key
    global col,y
    global guideleft

    if (not(iconright)):
        x=guideleft+(1*colwidth/10)
    else:
        x=guideleft+(7*colwidth/10)
    text=createText(x,y+5,(2*colwidth/10),35)
    insertText(ideogram, 0, text)  
    setFontSize(30,text)
    setFont("fontello-openantrag Regular",text)
    setTextAlignment(ALIGN_CENTERED, text)
    setTextColor("White",text)
    objname='OA_' + key + '_IDEO'
    setProperty(text,'itemName',objname)
    return objname

def Draw1ColBox():
    global key
    global col,y
    global guideleft

    oablue1=getColor("Openantrag-Blau")    

    if (col==0):
        box=createRect(guideleft-trim-overprint,
                       y,
                       colwidth+trim+2*overprint,
                       50)
    elif (col==1):
        box=createRect(guideleft-overprint,
                       y,
                       colwidth+2*overprint,
                       50)
    elif (col==2):
        box=createRect(guideleft-overprint,
                       y,
                       colwidth+trim+2*overprint,
                       50)
    else:
        sys.exit(1)

#    textBox=createText(24
    setFillColor("Openantrag-Blau",box)
    setLineWidth(10,box)
    setLineColor("None",box)

    objname='OA_' + key + '_BG'
    setProperty(box,'itemName',objname)

    return objname

def DrawHeader(column,ycoord,ideogram,title,iconright,newkey=None):
    global key
    global col
    col=column
    global y
    y=ycoord
    global guideleft
    global trim

    if (newkey==None):
        key=title        
    else:
        key=newkey

    guideleft=col*colwidth
    trim=5.67

    group=list()
#    colwidth=280

    Obox=Draw1ColBox()

    Otext=DrawHeaderText(title,iconright)
    Oideo=DrawIdeogram(ideogram,iconright)

    group=groupObjects([Obox,Otext,Oideo])

#    objname='OA_' + key
#    setProperty(group,'itemName',objname)

#    textFlowsAroundFrame(group,true)

