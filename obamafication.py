from Myro import *

def obamaFy():
    picture = makePicture(pickAFile())

    ObamaDarkBlue = makeColor(0,51,76)
    ObamaRed = makeColor(217, 26, 33)
    ObamaBlue = makeColor(112,150,158)
    ObamaYellow = makeColor(252, 227, 166)

    for i in getPixels(picture):
        if getGray(i) > 180:
            setColor(i, ObamaYellow)
        elif getGray(i) > 120:
            setColor(i, ObamaBlue)
        elif getGray(i) > 60:
            setColor(i, ObamaRed)
        else:
            setColor(i, ObamaDarkBlue)
           
            
    show(picture)

obamaFy()