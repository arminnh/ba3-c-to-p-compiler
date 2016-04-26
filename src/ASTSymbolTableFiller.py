from AbstractSyntaxTree import *
from SymbolTable import *

class ASTSymbolTableFiller:
    def __init__(self, ast:AbstractSyntaxTree, table:SymbolTable):
        self.ast = ast
        self.table = table

    def fill(self, node=None): # call without arguments initially
        if node is None:
            node = self.ast.root

        # if node.label == "identifier":
        #     print(node.getChildren()[0].label)

        if hasattr(node, "identifier"):
            print(node.identifier)

        for child in node.getChildren():
            self.fill(child)
