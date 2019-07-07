from nltk import *
from queue import Queue as Q
from queue import LifoQueue as LQ
import tkinter
import numpy as np
from OperatorClass import *
import copy

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
    def ParanthesisChecker(tokenizedInput):
        parens = "()"
        leftParen = 0
        rightParen= 0
        balanceCheck = lambda l,r: True if l==r else False
        for token in tokenizedInput:
            if token == "(":
                leftParen+=1
            if token == ")":
                rightParen+=1
        return balanceCheck(leftParen,rightParen)
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
        variables = "abcdefghijklmnopqrstuwxyz"
        operators = "^v>"
        numOfVars = 0
        listedVariables = iter(list(variables))
        listedOperators = iter(list(operators))
        hashOfVarsAndOps = {}
        [hashOfVarsAndOps.setdefault(next(listedVariables), list(operators)) for i in range(len(list(variables)) )]
        [hashOfVarsAndOps.setdefault(next(listedOperators) , list(variables)) for j in range(len(list(operators))) ]
        illegal = "()!"
        tokenizedInput = LogicalParser.MakeTokenz(inputFromPrompt)
        validOut = LogicalParser.ParanthesisChecker(tokenizedInput)
        used = []
        tokenizedInputRaw = [item for item in tokenizedInput if item not in illegal]
        tokenizedInputRaw.append("`")

        if (len(tokenizedInput) == 2 and tokenizedInput[0] != "!" and tokenizedInput[1]in operators):
            validOut = False
            self.outLabel["text"] = "Invalid Input"

        for i in range(0, len(tokenizedInputRaw), 2):
            if tokenizedInputRaw[i] in variables and tokenizedInputRaw[i] not in used:
                numOfVars = numOfVars + 1
                used.append(tokenizedInputRaw[i])
            if(tokenizedInputRaw[i] == "`" or tokenizedInputRaw[i+1] == "`"):
                break
            if tokenizedInputRaw[i] not in hashOfVarsAndOps[tokenizedInputRaw[i+1]]:

                validOut = False
                break
            if(tokenizedInputRaw[i+1] not in hashOfVarsAndOps[tokenizedInputRaw[i+2]]    ):
                validOut = False
                break


        if(validOut and len(tokenizedInputRaw) !=1):
            print("Valid Input . . .")
            self.NaiveSearch(LogicalParser.MakeQueueFromTokenz(tokenizedInput),numOfVars)

        else:
            self.outLabel["text"] = "Invalid Input"
    def ParanthesisChecker(tokenizedInput):
        leftParen = 0
        rightParen= 0
        balanceCheck = lambda l,r: True if l==r else False
        for token in tokenizedInput:
            if token == "(":
                leftParen+=1
            if token == ")":
                rightParen+=1
        return balanceCheck(leftParen,rightParen)
    def NaiveSearch(self,tokenizedQueue,numOfVars):

        listOfTokenz = [tokenizedQueue.get() for i in range( tokenizedQueue.qsize()) ]
        tokenizedQueue = LogicalParser.MakeQueueFromTokenz(listOfTokenz)
        setOfVars = set(listOfTokenz)
        listOfTokenzNonRepeat = list(setOfVars)
        illegalChars = ['^','v','>','(',')','!']
        Variables = "abcdefghijklmnopqrstuwxyz"
        OperatorS = illegalChars
        discardThatWorks = lambda set,char: set.discard(char)
        [discardThatWorks(setOfVars,illegalChars[i]) for i in range(len(illegalChars))]
        VarTFTable = LogicalParser.CreateVariableDefintions( len(setOfVars))
        equationObjects = []
        while(tokenizedQueue.qsize() != 0):
            currVar = tokenizedQueue.get()
            if(currVar == '!'):
                nextVar = tokenizedQueue.get()
                equationObjects.append(Variable(nextVar,False, True))
            elif(currVar in OperatorS):
                equationObjects.append(Operator(currVar))
            elif(currVar in Variables):
                equationObjects.append( Variable(currVar,False,False))
        print(equationObjects)
        print(VarTFTable)
        tokenizedQueueSearch = LogicalParser.MakeQueueFromTokenz(equationObjects)
        print(LogicalParser.GetResult(tokenizedQueueSearch))




    def GetResult(tokenizedQueueSearch):
        stagingObj = Stage()
        while (tokenizedQueueSearch.empty() != True):
            if (stagingObj.Full()):
                stagingObj.Result(Operation.Simplify(stagingObj))
            stagingObj.push(tokenizedQueueSearch.get())
        return stagingObj.FinalVal()

    def CreateVariableDefintions(numOfVars):
        print("in parsing ", numOfVars)
        boolCollection = np.ndarray((2 ** numOfVars, numOfVars))
        modolusSwitch = True
        modolusOp = (1 / 2) * (2 ** numOfVars)
        for i in range(len(boolCollection)):
            for j in range(len(boolCollection[i])):
                boolCollection[i][j] = False
        boolCollection = boolCollection.copy()
        for i in range(numOfVars):
            for j in range(1, (2 ** numOfVars) + 1):
                if (modolusSwitch):
                    boolCollection.__getitem__(j-1).__setitem__(i,True)
                if (j % modolusOp == 0):
                    modolusSwitch = not modolusSwitch
            modolusSwitch = True
            modolusOp /= 2
        return boolCollection
    def VarOrOp(token):
        variables = "abcdefghijklmnopqrstuwxyz"
        operators = "^v>"


program_start = LogicalParser()
