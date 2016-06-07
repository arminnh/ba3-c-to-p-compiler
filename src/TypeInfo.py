import copy

class TypeInfo:
    def __init__(self, baseType, rvalue=False, indirections=[(False, False)]):
        self.rvalue = rvalue
        self.baseType = baseType
        self.indirections = indirections # list of tuples: (is array, is constant)

    def array(self):
        return [indirect[0] for indirect in self.indirections]

    def const(self):
        return [indirect[1] for indirect in self.indirections]

    def size(self):
        size = 1
        for i in range(len(self.indirections) - 1, -1, -1):
            if type(self.array()[i]) is bool and self.array()[i] == False:
                return size
            size *= self.array()[i]

    def nrIndirections(self):
        return len(self.indirections) - 1

    def toRvalue(self):
        if self.rvalue:
            return self
        cpy = copy.deepcopy(self)
        cpy.rvalue = True
        cpy.indirections[-1] = (False, cpy.indirections[-1][1])

        return cpy

    def isArray(self):
        if type(self.array()[-1]) is bool:
            return self.array()[-1]
        return True

    def arrayNrDimensions(self):
        nr = 0
        for i in range(len(self.array()) - 1, -1, -1):
            if type(self.array()[i]) is bool and self.array()[i] == False:
                return nr
            nr += 1

    def isConst(self):
        return self.const()[-1]

    def isCompatible(self, other):
        if self is None or other is None:
            return False

        return  self.baseType         == other.baseType \
            and self.nrIndirections() == other.nrIndirections() \
            and self.isArray()        == other.isArray()


    def isConstCompatible(self, other):
        cself = self.const()
        cother = other.const()
        if len(cself) != len(cother):
            raise Exception("isConstCompatible expects const lists of the same length; got {0} for {1} and {2} for {3}".format(\
            cself, str(self), cother, str(other)))

        for i in range(len(cself) - 1):
            # last one is always OK because that's the one we're actually assigning (sorry bad explanation ask me)
            if cother[i] and not cself[i]:
                return False

        return True

    def equals(self, other, ignoreRvalue=True):
        if self is None or other is None:
            return False

        if not ignoreRvalue and self.rvalue != other.rvalue:
            return False

        return  self.baseType         == other.baseType \
            and self.nrIndirections() == other.nrIndirections() \
            and self.isArray()        == other.isArray()

    def __eq__(self, other):
        return self.equals(other)

    def out(self, withRvalue=False):
        out = ""

        if len(self.const()) and self.const()[0]:
            out += "const "

        out += str(self.baseType)

        declarator = ""
        for i in range(self.nrIndirections() - 1, -1, -1):
            arrayPart = self.array()[i+1]
            if type(arrayPart) is bool and arrayPart == False:
                if i+1 < len(self.const()) and self.const()[i+1]:
                	declarator = "*const " + declarator
                else:
                	declarator = "*" + declarator
            else:
            	if i + 2 < len(self.indirections) and (self.indirections[i + 2][0] == False and type(self.indirections[i + 2][0]) is bool):
            		if declarator[-1] == " ": declarator = declarator[:-1] # if closing parenthesis, remove space added by const declaration
            		declarator = "(" + declarator + ")"
            	declarator += "[{0}]".format(arrayPart if type(arrayPart) is int else "")

        out += (" " if len(declarator) else "") + declarator

        if withRvalue and self.rvalue is not None:
            out += " " + ("r" if self.rvalue else "l") + "value"

        return out

    def __str__(self):
        return self.out()


# global dictionary to get types
TYPES = {
    "int"    : TypeInfo(baseType="int"),
    "float"  : TypeInfo(baseType="float"),
    "char"   : TypeInfo(baseType="char"),
    "string" : TypeInfo(baseType="char", indirections=[(False, False), (True, False)]),
    "void"   : TypeInfo(baseType="void")
}
