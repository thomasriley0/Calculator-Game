import tkinter
import random
import math

class stateVars:
    def __init__(self):
        self.questions = []
        self.question = ""
        self.answer = 0
        self.guess = None
        self.attempts = 0
        self.solved = 0
        self.average = 0
        self.totalAttempts = 0
        self.incorrect = 0
        self.totalIncorrect = 0
    
    def addTotalIncorrect(self):
        self.totalIncorrect += 1
    
    def addIncorrect(self):
        self.incorrect += 1
    
    def clearIncorrect(self):
        self.incorrect = 0
        
    def calculateTotalAttempts(self):
        self.totalAttempts = self.totalIncorrect + self.solved
       
    def addAttempt(self):
        self.attempts += 1
    
    def calculateAverage(self):
        if self.solved > 0:
            self.average = self.totalAttempts / self.solved
            self.average = math.ceil(self.average * 100) / 100
        else:
            print("Please attempts a question: ")
    
    def addSolved(self):
        self.solved += 1
        
    def setAnswer(self, answer):
        self.answer = answer

    def setQuestion(self, question):
        self.question = question  
    
    def setGuess(self, guess):
        self.guess = guess
    
    def addPastQuestion(self, question):
        self.questions.append(question)
        
    def getAttempts(self):
        return self.attempts
    
    
def startMathGame():
    global state
    state = stateVars()
    global questionLabel
    global mainWindow
    global firstFrame
    global guessEntry
    global guessButton
    global guessLabel
    global secondFrame
    global problemLabel
    global fourthFrame
    global fifthFrame
    global sixthFrame
    global signVar
    global averageLabel
    global incorrectLabel

    
    intializeGame()
    
    mainWindow = tkinter.Tk()
    mainWindow.title("Calculator")
    
    firstFrame = tkinter.Frame(mainWindow)
    firstFrame.pack()
    
    questionLabel = tkinter.Label(firstFrame, text="")
    questionLabel.pack(side=tkinter.LEFT)
    
    guessEntry = tkinter.Entry(firstFrame)
    guessEntry.pack(side=tkinter.LEFT)
    
    guessButton = tkinter.Button(firstFrame, text="Check it!", command=checkGuess)
    guessButton.pack(side=tkinter.RIGHT)
    
    secondFrame = tkinter.Frame(mainWindow)
    secondFrame.pack()

    guessLabel = tkinter.Label(secondFrame, text="")
    guessLabel.pack()
    
    thirdFrame = tkinter.Frame(mainWindow)
    thirdFrame.pack()
    
    incorrectLabel = tkinter.Label(thirdFrame, text="Incorrect solutions: " + str(state.incorrect))
    incorrectLabel.pack()
    
    problemLabel = tkinter.Label(thirdFrame, text="Problems attempted: " + str(state.attempts) + ", solved: " + str(state.solved))
    problemLabel.pack()
    
    fourthFrame = tkinter.Frame(mainWindow)
    fourthFrame.pack()
    
    averageLabel = tkinter.Label(fourthFrame, text="Average number of answer attempts per solved problem: " + str(state.average))
    averageLabel.pack()
    
    fifthFrame = tkinter.Frame(mainWindow)
    fifthFrame.pack()
    
    sixthFrame = tkinter.Frame(mainWindow)
    sixthFrame.pack()
    
    signVar = tkinter.IntVar()
    
    
    addCheckBox = tkinter.Radiobutton(fifthFrame, text="+", variable=signVar, value=0)
    addCheckBox.pack(side=tkinter.LEFT)
    subCheckBox = tkinter.Radiobutton(fifthFrame, text="-", variable=signVar, value=1)
    subCheckBox.pack(side=tkinter.LEFT)
    multiCheckBox = tkinter.Radiobutton(fifthFrame, text="*", variable=signVar, value=2)
    multiCheckBox.pack(side=tkinter.LEFT)
    divCheckBox = tkinter.Radiobutton(fifthFrame, text="/", variable=signVar, value=3)
    divCheckBox.pack(side=tkinter.LEFT)
    anyCheckBox = tkinter.Radiobutton(fifthFrame, text="ANY", variable=signVar, value=4)
    anyCheckBox.pack(side=tkinter.LEFT)
    anyCheckBox.select()
    
    newProblemButton = tkinter.Button(sixthFrame, text="Show me a new problem", command=showNewProblem)
    newProblemButton.pack()

    quitButton = tkinter.Button(sixthFrame, text="Quit", command=masterQuit)
    quitButton.pack()


    
    updateQuestionLabel()
    
    mainWindow.mainloop()
    
    
    
def updateQuestionLabel():
    questionLabel.configure(text=state.question)

def updateIncorrectLabel():
    incorrectLabel.configure(text="Incorrect solutions: " + str(state.incorrect))
    
def updateAverageLabel():
    averageLabel.configure(text="Average number of answer attempts per solved problem: " + str(state.average))
    
def showNewProblem():
    sign = signVar.get()
    generateQuestion(sign)
    updateQuestionLabel()
    guessEntry.config(state='normal')
    guessButton.config(state='normal')
    guessEntry.delete(0, 'end')
    updateProblemLabel()
    state.clearIncorrect()
    updateIncorrectLabel()
    guessLabel.configure(text="")
    
def masterQuit():
    mainWindow.destroy()
    print("Game Stats: \n" + "Total number of problems attempted: " + str(state.totalAttempts) + "\n" + "Total number of problems solved: " + str(state.solved) + "\n" + "Average number of guesses per solved question: " + str(state.average))
    
def intializeGame():
    random_sign = random.randint(0, 3)
    generateQuestion(random_sign)
    
def checkGuess():
    state.setGuess(guessEntry.get())
    
    if state.guess.isdigit():
        if guessEntry["state"] != 'disabled':
            if int(state.guess) == int(state.answer):
                guessLabel.configure(text="Correct!")
                state.addSolved()
                guessEntry.config(state='disabled')
                guessButton.config(state='disabled')
            else:
                guessLabel.configure(text="Incorrect!")
                state.addIncorrect()
                state.addTotalIncorrect()
                updateIncorrectLabel()
            updateProblemLabel()
    state.calculateTotalAttempts()
    if state.solved > 0:
        state.calculateAverage()
        updateAverageLabel()
        
def updateProblemLabel():
    problemLabel.configure(text="Problems attempted: " + str(state.attempts) + ", solved: " + str(state.solved))


def generateQuestion(index):
    types = ["+", "-","*", "/", "ANY"]
    sign = types[index]
    first_term = 0
    second_term = 0
    question = ""
    answer = 0
    terms = []
    
    if sign == "*":
        first_term = random.randint(1, 25)
        second_term = random.randint(1, 40)
        terms = [first_term, second_term]
        answer = max(terms) * min(terms) 
        
    if sign == "/":
        first_term = random.randint(1, 50)
        second_term = random.randint(1, 20)
        second_term = second_term * first_term 
        terms = [first_term, second_term]
        answer = max(terms) / min(terms)
        
    if sign == "+":
        first_term = random.randint(1, 500)
        second_term = random.randint(1, 499)
        terms = [first_term, second_term]
        answer = max(terms) + min(terms)
        
    if sign == "-":
        first_term = random.randint(1, 500)
        second_term = random.randint(1, 499)
        terms = [first_term, second_term]
        answer = max(terms) - min(terms)
        
    if sign == "ANY":
        random_sign = random.randint(0, 3)
        generateQuestion(random_sign)
    
        
        
    if len(terms) != 0:
        question_list = [max(terms), min(terms), sign]
        if question_list not in state.questions:
            state.addAttempt()
            question = str(max(terms)) + sign + str(min(terms))
            state.setQuestion(question)  
            state.setAnswer(answer)
            state.addPastQuestion(question_list)
        else:
            generateQuestion(index)
            
       
