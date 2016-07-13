from Myro import *

init("sim")
penUp()

backward(1, 2)

def drawA(size):
    penDown()

    turnBy(70, "deg")
    forward(1, size)
    turnBy(-140, "deg")
    forward(1, size*0.48)
    turnBy(-110, "deg")
    forward(1, size*0.35)
    backward(1, size*0.35)
    turnBy(110, "deg")
    forward(1, size*0.52)
    
    penUp()
    
    #Repositioning for next letter
    turnBy(70, "deg")
    forward(1, size * 0.2)
    
    drawT(size)

def drawT(size):
    penDown()
    forward(1, size * 0.275)
    turnBy(90, "deg")
    forward(1, size * 0.8)
    turnBy(90, "deg")
    forward(1, size * 0.275)
    backward(1, size * 0.45)
    
    
drawA(5)