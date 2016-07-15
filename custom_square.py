from Myro import *

init("sim")

#Makes one square of given size

init("sim")
penDown()

def makeSide(size):
    forward(1, size)
    turnBy(90, "deg")

i = 0

while i < 4:
    makeSide(1)
    i = i + 1