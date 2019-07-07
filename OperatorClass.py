class Stage:
    def __init__(self):
        self.leftVar = None
        self.rightVar = None
        self.operation = None
    def push(self,equationObject):
        if(self.leftVar == None):
            if (equationObject.Neg):
                self.leftVar = not equationObject.valueTF
            else:
                self.leftVar = equationObject.valueTF

        elif(self.operation == None):
            self.operation = equationObject.operator
        elif(self.rightVar == None):
            if(equationObject.Neg):
                self.rightVar = not equationObject.valueTF
            else:
                self.rightVar = equationObject.valueTF

    def Full(self):
        return True if self.rightVar != None else False
    def RightEmpty(self):
        return True if self.rightVar == None else False

    def Result(self,simplifiedLeftVal):
        self.leftVar = simplifiedLeftVal
        self.operation = None
        self.rightVar = None
    def FinalVal(self):
        return self.leftVar

class Operation:
    def Simplify(StageObject):
        Conjunction = lambda varLeft,varRight:  bool(varLeft and varRight)
        Disjunction = lambda varLeft,varRight:  bool(varLeft or varRight)
        Conditional = lambda varLeft, VarRight: bool(True if varLeft else VarRight)
        operations = {'^': Conjunction, 'v': Disjunction, ">": Conditional}
        operation = operations[StageObject.operation]
        return operation(StageObject.leftVar,StageObject.rightVar)


class Variable:

    def __init__(self,variable, valueTF,Neg):
        self.variable = variable
        self.valueTF = valueTF
        self.Neg = Neg
    def setValueTF(self,valueTF):
        self.valueTF = valueTF

    def __repr__(self):
        return '({} - variable)\t ({} - Truth Value) \t ({} - Include Negation'.format(self.variable,self.valueTF, self.Neg)
class Operator:
    def __init__(self,operator):
        self.operator = operator
    def __repr__(self):
        return '{} - operator '.format(self.operator)





