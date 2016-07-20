from random import *
from time import sleep

xCoordinate = 250
yCoordinate = 250
directionChoice = [-4, 4]
moveX = random() * choice(directionChoice)
moveY = random() * choice(directionChoice)


      
def setup():
    size(500, 500)
    background(255)
    
def draw():
    global xCoordinate
    global yCoordinate
    global moveX
    global moveY
    
    xCoordinate = xCoordinate + moveX
    yCoordinate = yCoordinate + moveY
    
    ellipseMode(CENTER)
    rectMode(CENTER)
    
    background(255)
    fill(0, 0, 255)
    img = loadImage("drake.png")
    image(img, mouseX, mouseY, 30, W * 0.05)
    
    #Paddle
    fill(255, 0, 0)
    rect(mouseX, 465, 75, 30)
    
    if xCoordinate <= 15:
        moveX = -moveX
    elif xCoordinate > 485:
        moveX = -moveX
    elif yCoordinate <= 15:
        moveY = -moveY
    elif yCoordinate >= 435 and yCoordinate <= 500 and xCoordinate >= (mouseX - 37.5) and xCoordinate <= (mouseX + 37.5):
        moveY = -moveY
    elif yCoordinate >= 530:
        
        xCoordinate = 250
        yCoordinate = 250
        moveX = random() * choice(directionChoice)
        moveY = random() * choice(directionChoice)
        
        sleep(1)