from random import randint, choice

currentLetters = [
    [chr(randint(65, 90)), -150, 50 * randint(1, 9)],
    [chr(randint(65, 90)), -300, 50 * randint(1, 9)],
    [chr(randint(65, 90)), -450, 50 * randint(1, 9)],
    [chr(randint(65, 90)), -600, 50 * randint(1, 9)]
]

# [ 'a', -150, y)
    
xSpeed = 3
currentScore = 0 
highScore = 0

def createLetter(lastLocation):
    global currentLetters
    
    currentLetters.append([chr(randint(65, 90)), lastLocation-600, 50 * randint(1, 9)])

def setup():
    size(500, 500)
    background(255)
    
def draw():
    global currentLetters
    global xSpeed
    global currentScore
    global highScore
    
    background(255)
    
    fill(255, 0, 0)
    textSize(20)
    text("High Score:" + str(highScore), 10, 25)
    
    fill(0, 0, 255)
    textSize(20)
    text("Score:" + str(currentScore), 10, 50)
    
    for i in currentLetters:
        i[1] = i[1] + xSpeed
        
        if i[1] <= 500:
            textAlign(LEFT, CENTER)
            textSize(30)
            fill(0)
            text(i[0], i[1], i[2])
        else:
            currentLetters.remove(i)
            createLetter(500)
            
            currentScore = currentScore - 2
            
            
def keyPressed():
    global currentLetters
    global currentScore
    global xSpeed
    global highScore
    
    if key.upper() == currentLetters[0][0]:
        createLetter(currentLetters[0][1])
        
        currentLetters.remove(currentLetters[0])
        
        currentScore = currentScore + 1
        
        if highScore < currentScore:
            highScore = currentScore
        
        if xSpeed < 10:
            if currentScore % 5 == 0:
                xSpeed = xSpeed + 0.5