from pprint import *

class ASTNode:

    def __init__(self, label="no label", parent=None):
        self.label = label
        self.children = []
        self.parent = parent

    def addChildNode(self, node):
        if not isinstance(node, ASTNode):
            print("trying to add child of non-ASTNode type: expected" + str(ASTNode) + ", got " + str(type(node)))
            return
        self.children.append(node)
        node.parent = self
        return node

    def addChild(self, label:str):
        if type(label) is not str:
            print("trying to add child with label of non-str type")
        node = ASTNode(label, self)
        self.children.append(node)
        return node

    def out(self, level=1):
        str = self.label + "\n"

        for child in self.children:
            str += "   " * level + child.out(level+1)

        if not self.children:
            str += "\n"

        return str

    def __str__(self):
        return self.label


class ASTInequalityOperatorNode(ASTNode):
    def __init__(self, lt:bool, eq:bool, parent=None):
        label = ("<" if lt else ">") + ("=" if eq else "")
        ASTNode.__init__(self, label, parent)
        self.lt = lt
        self.eq = eq

class ASTEqualityOperatorNode(ASTNode):
    def __init__(self, ineq:bool, parent=None):
        ASTNode.__init__(self, "!=" if ineq else "==", parent)
        self.ineq = ineq

class AbstractSyntaxTree:

    def __init__(self, root=ASTNode("root")):
        self.root = root

    def __str__(self):
        return "AST:\n" + self.root.out()





# tests
if __name__=="__main__":
    root = ASTNode("root")

    one = root.addChild("child1")
    two = root.addChild("child2")

    three = one.addChild("three")

    four = two.addChild("four")
    five = two.addChild("five")

    three.addChild("six")

    ast = AbstractSyntaxTree(root)
    print (root.out())

    currentNode = root
    print (currentNode)
    print (currentNode.parent)
    currentNode = currentNode.addChild("bla")
    print (currentNode)
    print (currentNode.parent)
    currentNode = currentNode.addChild("blabla")
    print (currentNode)
    print (currentNode.parent)
    currentNode = currentNode.parent
    print (currentNode)
    print (currentNode.parent)
