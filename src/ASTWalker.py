from AbstractSyntaxTree import *

class ASTWalker:
    def __init__(self, ast, nodetypes:list, callbacks:list):
        self.nodetypes = nodetypes
        self.callbacks = callbacks
        self.ast = ast

    def walk(node=None):
        if node is None:
            node = self.ast.root

        for i, nodetype in enumerate(nodetypes):
            if type(node) is nodetype:
                self.callback[i](node)

        for child in node.getChildren():
            walk(child)
