"""
Created by Ahnaf Taha and Jordane Thomas
--
ASC Goldman Gang 2016
7/20/2016
"""
from random import *

gameList = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

timesClicked = 0

def setup():
    global gameList    
    
    size(500, 500)
    background(255)
    
    gameList[randint(0,4)][randint(0,4)] = 1
    
def draw():
    global gameList
    global timesClicked
    
    background(255)
    
    j = 0
    
    while j < 5:
        
        i = 0
        while i < 5:
            if gameList[j][i] == 0 or gameList[j][i] == 1:
                fill(0, 0, 255)
            elif gameList[j][i] == 2:
                fill(0, 255, 0)
            elif gameList[j][i] == -1:
                fill(255, 0, 0)
            
            rect(100 * i, 100 * j, 100, 100)
            
            i = i + 1
        
        j = j + 1
        
    if timesClicked == 5:
        fill(255)
        noStroke()
        
        textSize(32)
        textAlign(CENTER, CENTER)
        text("YOU HAVE FAILED! (CLAP NOW)", 250, 250)
        
def mouseClicked():
    global timesClicked
    
    if timesClicked < 5:
        global gameList
        
        row = 0
        co = 0
        
        if mouseY <= 100:
            row = 0
        elif mouseY <= 200:
            row = 1
        elif mouseY <= 300:
            row = 2
        elif mouseY <= 400:
            row = 3
        elif mouseY <= 500:
            row = 4
            
        if mouseX <= 100:
            co = 0
        elif mouseX <= 200:
            co = 1
        elif mouseX <= 300:
            co = 2
        elif mouseX <= 400:
            co = 3
        elif mouseX <= 500:
            co = 4
            
        if gameList[row][co] == 0:
            gameList[row][co] = -1
        elif gameList[row][co] == 1:
            gameList[row][co] = 2
            
        timesClicked = timesClicked + 1