from nltk import *
from queue import Queue as Q
import tkinter

class LogicalParser:
    def __init__(self):
        self.window = tkinter.Tk()

        self.window.title("prin")
        self.window.geometry("500x300")
        self.window.resizable(False, False)
        self.label = tkinter.Label(self.window, text="Type Logical Statement", justify="left", anchor="w")
        self.outLabel = tkinter.Label(self.window, text="\n\nWaiting for input . . . ", font="Times 24", justify="center",
                                 anchor="s", bd=1)
        self.inputPrompt = tkinter.Entry(self.window, justify="left")
        self.keyLabel = tkinter.Label(self.window, justify="left",
                                 text="^   | (shift6) for conjuction\nv   | (alphabet, lowercase) for disjunction\n!    | for negation\n>   | for implication\n",
                                 font="Times 12")
        self.button = tkinter.Button(self.window, justify="left", anchor="w", text="check",
                                command= lambda:self.validInputChecker(self.inputPrompt.get())      )
        self.keyLabel.pack()

        self.label.pack()
        self.inputPrompt.pack()
        self.outLabel.pack()

        self.button.pack()
        self.window.mainloop()
    def MakeTokenz(inputString):

        tokenized_clean = []
        tokenizedString = word_tokenize(inputString)
        tokenized_clean = [char for item in tokenizedString for char in item ]
        return tokenized_clean

    def MakeQueueFromTokenz(tokenizedInput):
        tokenQueue =  Q(len(tokenizedInput))
        tokIter = iter(tokenizedInput)
        tokToQueue = lambda token: tokenQueue.put(token)
        [tokToQueue(next(tokIter)) for i in range(len(tokenizedInput)) ]
        return tokenQueue


    def validInputChecker(self,inputFromPrompt):
        operatorCounter = 0
        variableCounter = 0
        operators = "^v>"
        parens = "()"
        previous = ""
        variables = "abcdefghijklmnopqrstuwxyz"
        tokenizedInput = LogicalParser.MakeTokenz(inputFromPrompt)
        for item in tokenizedInput:
            if item in parens:
                previous = ""
                continue
            if item in operators:
                operatorCounter+=1
            if item in variables:
                variableCounter+=1
            previous = item
        if(operatorCounter == 0 and variableCounter ==0):
            print("no input . . .")
        elif( (operatorCounter*2) == variableCounter):
            self.outLabel['text'] = "MainParser!"

        else:
            self.outLabel["text"] = "Invalid Input"







program_start = LogicalParser()
