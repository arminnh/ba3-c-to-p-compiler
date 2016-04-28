import linecache

class CompilerErrorHandler:
    def __init__(self, srcFilename):
        self.srcFilename = srcFilename
        self.errors = []

    def addError(self, error, linenumber, column):
        self.errors.append((error, linenumber, column))
        self.printError(0)
        quit()
    
    def printError(self, index):
        error = self.errors[index]
        if error[1] is not None and error[2] is not None:
            column = error[2]
            print("Error at {line}:{column}: {error}".format(line=error[1], column=column, error=error[0]))
            
            line = linecache.getline(self.srcFilename, error[1])[:-1]
            while len(line) and line[0] in [" ", "\t"]: # remove whitespace in front
                line = line[1:]
                column -= 1
            
            print(line)
            print(" " * (column) + "^")
        else:
            print("Error: {error}".format(error=error[0]))
    
    def printErrors():
        for i in range(len(self.errors)):
            self.printError(i)