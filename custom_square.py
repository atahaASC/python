from Myro import *

size = float(raw_input("What size do you want your square to be? (Integer only, please)"))

init("sim")

i = 0

def oneSide():
    turnBy(90, "deg")

while i < 4:
    oneSide()