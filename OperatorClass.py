
class Operation:
    def Simplify(varLeft, operator, varRight):
       Conjunction = lambda varLeft,varRight:  bool(varLeft and varRight)
       Disjunction = lambda varLeft,varRight:  bool(varLeft or varRight)
       Conditional = lambda varLeft, VarRight: bool(True if varLeft else varRight)
       operations = {'^': Conjunction, 'v': Disjunction, ">": Conditional}
       operation = operations[operator.operator]
       return operation(varLeft,varRight)


class Variable:
    def __init__(self, variable, valueTF):
        self.variable = variable
        self.valueTF = valueTF
    def __init__(self,variable, valueTF,Neg):
        Variable(variable,valueTF)
        self.Neg = True



    def __repr__(self):
        return '{} - variable\n{} - Truth Value'.format(self.variable,self.valueTF)
class Operator:
    def __init__(self,operator):

        self.operator = operator




