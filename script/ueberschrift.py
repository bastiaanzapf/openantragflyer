
# coding=utf8

try:
    from scribus import *
except ImportError:
    print "This script only runs from within Scribus."
    sys.exit(1)

colwidth=280
overprint=1

def DrawHeaderText(title):
    global col,y
    global guideleft

    x=guideleft+(3*colwidth/10)

    text=createText(x,y+10,(2*colwidth/3),30)
    insertText(title, 0, text)  
    setFontSize(24,text)
    setFont("Bebas Neue Regular",text)
    setTextAlignment(ALIGN_CENTERED, text)
    setTextColor("Openantrag-Blau-2",text)

    return text

def DrawIdeogram(ideogram):
    global col,y
    global guideleft

    x=guideleft+(1*colwidth/10)

    text=createText(x,y+10,(2*colwidth/10),30)
    insertText(ideogram, 0, text)  
    setFontSize(30,text)
    setFont("fontello-openantrag Regular",text)
    setTextAlignment(ALIGN_CENTERED, text)
    setTextColor("White",text)
    return text

def Draw1ColBox():
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

    return box

def DrawHeader(column,ycoord,ideogram,title):

    global col
    col=column
    global y
    y=ycoord
    global guideleft
    global trim

    guideleft=col*colwidth
    trim=5.67

    group=list()
#    colwidth=280

    Obox=Draw1ColBox()
    Otext=DrawHeaderText(title)
    Oideo=DrawIdeogram(ideogram)

    group=groupObjects([Obox,Otext,Oideo])

#    textFlowsAroundFrame(group,true)

