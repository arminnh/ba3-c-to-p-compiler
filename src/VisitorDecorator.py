from antlr4 import *
from AbstractSyntaxTree import *
from Visitor import *
from TypeInfo import types

class VisitorDecorator(Visitor):
    def __init__(self):
        super(VisitorDecorator, self).__init__()

    # TODO: refactor
    def isTypeCheckArrayInitializerValid(self, node):
        if node.getType().isArray() and node.initializerList and \
            not node.initializerList.isArray and \
            not isinstance(node.initializerList.children[0], ASTStringLiteralNode):
                return

        arrayIterator = -1
        for (i, (isArray, isConstant)) in reversed(list(enumerate(node.indirections))):
            if not isArray:
                continue

            arrayIterator += 1
            arrayLengthNode = node.arrayLengths[arrayIterator]

            if not arrayLengthNode.children:
                if arrayIterator == 0:
                    if node.initializerList is not None:
                        node.indirections[i] = (len(node.initializerList.children), False)
                        continue
                    else:
                        return
                elif i <= len(node.indirections) and node.indirections[i+1][0] == False:
                    continue
                else:
                    return

            if not isinstance(arrayLengthNode.children[0], ASTIntegerLiteralNode):
                continue

            node.indirections[i] = (arrayLengthNode.children[0].value, node.indirections[i][1])


    # int a[myFun(5)] = {1, 2+"a", 3}
    def visitDeclaratorInitializerNode(self, node):
        if self.visitChildren(node) == "error":
            return

        if node.getType().isCompatible(types["void"].toRvalue()):
            return

        # TODO: find a better place for this
        for child in node.children:
            if isinstance(child, ASTInitializerListNode):
                node.initializerList = child

        # if basetype is array, typecheck with each elements of initializer list
        if node.getType().isArray():
            if not self.isTypeCheckArrayInitializerValid(node):
                return

            for initListElement in node.initializerList.children:
                # get basetype for typechecking with initializer list elements, example: int a[] = {1, 2, 3, 4};
                t1 = copy.deepcopy(node.getType())
                t2 = initListElement.getType().toRvalue()

                # if initializer is not a string literal, pop the array from the variable to be initialized
                if not isinstance(initListElement, ASTStringLiteralNode):
                    t1.indirections.pop()

                #  char a[] = "special case";   // types char [] and  char *
                if isinstance(node.initializerList.children[0], ASTStringLiteralNode) and node.getType().equals(types["string"]):
                    continue

                # do the type checking
                if not self.isTypeCheckInitializerValid(t1, t2, node):
                    continue

        # only typecheck with 1st element of initializer list, example: int a = {1, 2.0, "aaa", 'a'} is ok
        else:
            # if initializer list does not have any children (int a = {}), error
            if len(node.initializerList.children) == 0:
                return

            # do the type checking
            if not self.isTypeCheckInitializerValid(node.getType().toRvalue(), node.initializerList.children[0].getType().toRvalue(), node):
                return
