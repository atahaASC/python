from Myro import *

#Each square will be bigger than the last

squareNumber = raw_input("How many squares do you want (integer number please, i.e. 1, 2, 3)?")
sizeDifference = raw_input("What size difference do you want between each consecutive square?")

init("sim")

def makeSide(size):
    forward(1, size)
    turnBy(90, "deg")
    
penDown()

i = 0

while i < squareNumber:
    j = 0
    
    while j < 4:
        makeSize(sizeDifference)
        j = j + 1
    sizeDifference = sizeDifference + 1