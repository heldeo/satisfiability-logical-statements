from nltk import *
from queue import Queue as Q
firstTestString = "     (  p    vp )^    (!p^q)"

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



inputToQueue = MakeQueueFromTokenz(MakeTokenz(firstTestString))
for i in range(inputToQueue.qsize()):
    print(inputToQueue.get(), end = " ")

