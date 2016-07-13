import random

def createQuestion():
    numberOne = random.randrange(1, 11)
    numberTwo = random.randrange(1, 11)
    randomOp = 1#random.randrange(1, 5)
    questionAnswer = 0
    
    if randomOp == 1:
        questionAnswer = numberOne+numberTwo
        
        answerGiven = int(raw_input("(", questionsGiven, ") What is the answer to", numberOne, "+", numberTwo, "?"))   
    elif randomOp == 2:
        questionAnswer = numberOne-numberTwo
    elif randomOp == 3:
        questionAnswer = numberOne*numberTwo
    elif randomOp == 4:
        questionAnswer = numberOne/numberTwo
    
    return;

numberOfQuestions = int(raw_input("How many questions do you want?"))
g
def whileTest():
q   uestionsGiven = 1
    while questionsGiven < numberOfQuestions + 1:
        createQuestion()
        
        
        questionsGiven = questionsGiven + 1
    
    return;

def forTest():

    return;
