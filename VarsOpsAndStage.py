class Stage:
    def __init__(self):
        self.leftVar = None
        self.rightVar = None
        self.operation = None
    def push(self,equationObject):
        if(self.leftVar == None):
            self.leftVar = equationObject

        elif(self.operation == None):
            self.operation = equationObject.operator
        elif(self.rightVar == None):
            self.rightVar = equationObject

    def Full(self):
        return True if self.rightVar != None else False
    def RightEmpty(self):
        return True if self.rightVar == None else False

    def Result(self,simplifiedLeftVal):

        self.leftVar.setValueTF(simplifiedLeftVal)
        self.operation = None
        self.rightVar = None
    def FinalVal(self):
        return self.leftVar.valueTF
    def __repr__(self):
        return '{} {} {}'.format(self.leftVar,self.operation,self.rightVar)

class Operation:
    def Simplify(StageObject):

        Conjunction = lambda varLeft,varRight:  bool(varLeft and varRight)
        Disjunction = lambda varLeft,varRight:  bool(varLeft or varRight)
        Conditional = lambda varLeft, VarRight: bool(not (varLeft) or VarRight)
        operations = {'^': Conjunction, 'v': Disjunction, ">": Conditional}
        operation = operations[StageObject.operation]
        print("OPEration: ", StageObject.leftVar.valueTF,StageObject.rightVar.valueTF)
        TF = operation(StageObject.leftVar.valueTF,StageObject.rightVar.valueTF)
        print("TF:" ,TF)
        return TF
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





