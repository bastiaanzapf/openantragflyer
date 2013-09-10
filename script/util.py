
# coding=utf8

# set the "offset policy", the position of the first line of a Text

# setze die Position der ersten Zeile
try:
    from scribus import *
except ImportError:
    print "This script only runs from within Scribus."
    sys.exit(1)

def setOffsetPolicy(policy,text):
    setProperty(text,"firstLineOffset",policy)
