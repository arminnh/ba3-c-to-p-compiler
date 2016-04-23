from pprint import *

class Node:

    def __init__(self, label="no label", parent=None):
        self.label = label
        self.children = []
        self.parent = parent

    def addChild(self, label):
        node = Node(label, self)
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




class AbstractSyntaxTree:

    def __init__(self, root=Node("root")):
        self.root = root

    def __str__(self):
        return "AST:\n" + self.root.out()





# tests
if __name__=="__main__":
    root = Node("root")

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
