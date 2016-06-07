from antlr4 import *
from AbstractSyntaxTree import *
from Visitor import *
from TypeInfo import TYPES

class VisitorDecorator(Visitor):
    def __init__(self):
        super(VisitorDecorator, self).__init__()

    def fillIndirectionsList(self, node):
        arrayIterator = -1

        for (i, (isArray, isConstant)) in reversed(list(enumerate(node.indirections))):
            if not isArray:
                continue

            arrayIterator += 1
            arrayLengthNode = node.arrayLengths[arrayIterator]

            # ex. int a[] = {1, 2, 3};
            if not arrayLengthNode.children and arrayIterator == 0 and node.initializerList is not None:
                # ex. char s[] = "hello";
                if node.getType().baseType == "char" and \
                   node.initializerList.children and isinstance(node.initializerList.children[0], ASTStringLiteralNode) and \
                   node.getType().isCompatible(node.initializerList.children[0].getType()):
                    node.indirections[i] = (len(node.initializerList.children[0].decodedValue)+1, False)
                else:
                    node.indirections[i] = (len(node.initializerList.children), False)

            elif arrayLengthNode.children and isinstance(arrayLengthNode.children[0], ASTIntegerLiteralNode):
                node.indirections[i] = (arrayLengthNode.children[0].value, node.indirections[i][1])

    # int a[myFun(5)] = {1, 2+"a", 3}
    def visitDeclaratorInitializerNode(self, node):
        for child in node.children:
            if isinstance(child, ASTInitializerListNode):
                node.initializerList = child

        self.fillIndirectionsList(node)
