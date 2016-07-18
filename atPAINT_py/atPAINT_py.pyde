from random import *

W = 1000
H = 500

currentShape = 2
currentColor = [255,0,0]

def setup():
    global W
    global H
    
    size(W, H)
    background(255, 255, 255)
    
def draw():
    global W
    global H
    
    rectMode(CENTER)
    textAlign(CENTER, CENTER)
    
    noStroke()
    
    #Create Menu
    fill(150, 150, 150)
    rect(W * 0.85, H * 0.5, W * 0.3, H)
    
    #Text
    fill(0, 0, 255)
    textSize(W * 0.065)
    text("MENU", W * 0.85, H * 0.1)

    fill(0, 0, 0)    
    textSize(W * 0.015)
    text("Press Z to cycle between shapes.", W * 0.85, H * 0.25)
    
    fill(0, 0, 0)    
    textSize(W * 0.015)
    text("Click to choose color.", W * 0.85, H * 0.375)
    
    fill(255, 0, 0)
    rect(W * 0.85, H * 0.5, W * 0.05, W * 0.05)
    
    fill(0, 255, 0)
    rect(W * 0.775, H * 0.5, W * 0.05, W * 0.05)
    
    fill(0, 0, 255)
    rect(W * 0.925, H * 0.5, W * 0.05, W * 0.05)
    
    fill(200, 200, 200)
    rect(W * 0.85, H * 0.75, W * 0.2, H * 0.15)
    
    fill(0, 0, 0)
    textSize(W * 0.02)
    text("CLEAR CANVAS", W * 0.85, H * 0.75)
    
    if mousePressed:
        if mouseX < W * 0.7 and mouseX > W * 0.01:
            if currentShape == 0:
                fill(currentColor[0], currentColor[1], currentColor[2])
                rect(mouseX, mouseY, W * 0.01, W * 0.01)
            elif currentShape == 1:
                fill(currentColor[0], currentColor[1], currentColor[2])
                ellipse(mouseX, mouseY, W * 0.01, W * 0.01)
            elif currentShape == 2:
                tint(currentColor[0], currentColor[1], currentColor[2])
                img = loadImage("kanye.png")
                image(img, mouseX, mouseY, W * 0.05, W * 0.05)
                
def keyPressed():
    global currentShape
    
    if key == 'z':
        if currentShape == 0:
            currentShape = 1
        elif currentShape == 1:
            currentShape = 2
        elif currentShape == 2:
            currentShape = 0
            
def mouseClicked():
    global currentColor
    
    print("hi")
    
    if mouseX < (W * 0.775) + (W * 0.025) and mouseX > (W * 0.775) - (W * 0.025) and mouseY < (H * 0.5) + (W * 0.025) and mouseY > (H * 0.5) - (W * 0.025):
        currentColor = [0,255,0]
    elif mouseX < (W * 0.85) + (W * 0.025) and mouseX > (W * 0.85) - (W * 0.025) and mouseY < (H * 0.5) + (W * 0.025) and mouseY > (H * 0.5) - (W * 0.025):
        currentColor = [255,0,0]
    elif mouseX < (W * 0.925) + (W * 0.025) and mouseX > (W * 0.925) - (W * 0.025) and mouseY < (H * 0.5) + (W * 0.025) and mouseY > (H * 0.5) - (W * 0.025):
        currentColor = [0,0,255]
    elif mouseX < (W * 0.85) + (W * 0.1) and mouseX > (W * 0.85) - (W * 0.1) and mouseY < (H * 0.75) + (H * 0.075) and mouseY > (H * 0.75) - (H * 0.075):
        background(255, 255, 255)