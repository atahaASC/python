xCoordinate = 0

def setup():
    size(500, 500)
    background(255)

def makeCar(x, y, color, w, h, desc):
    rectMode(CENTER)
    textAlign(CENTER, CENTER)
    
    fill(0)
    rect(x + (w * 0.35), y, w * 0.1, h * 1.1)
    rect(x - (w * 0.35), y, w * 0.1, h * 1.1)
    rect(x + (w * 0.35), y + (h * 0.6), w * 0.15, h * 0.1)
    rect(x + (w * 0.35), y - (h * 0.6), w * 0.15, h * 0.1)
    rect(x - (w * 0.35), y + (h * 0.6), w * 0.15, h * 0.1)
    rect(x - (w * 0.35), y - (h * 0.6), w * 0.15, h * 0.1)
    
    if color == "red":
        fill(255, 0, 0)
    elif color == "green":
        fill(0, 255, 0)      
    elif color == "blue":
        fill(0, 0, 255)
    else:
        fill(255)
        
    rect(x, y, w, h)
    
    fill(0)
    textSize(w * 0.1)
    text(desc, x, y)
    
    return {x, y, color, w, h, desc}
        

def draw():
    global xCoordinate
    background(255)
    
    makeCar(xCoordinate, 250, "blue", 100, 50, "pokeman mobile")
    xCoordinate = xCoordinate + 1