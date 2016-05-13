import linecache

class CompilerErrorHandler:
    def __init__(self, srcFilename):
        self.srcFilename = srcFilename
        self.errors = []

    def addError(self, error, linenumber, column):
        self.errors.append((error, linenumber, column))

    # def addWarning(self, error, linenumber, column):
    #     self.errors.append((error, linenumber, column))

    def errorCount(self):
        return len(self.errors)

    def errorToString(self, index):
        msg = ""
        error = self.errors[index]
        if error[1] is not None and error[2] is not None:
            column = error[2]
            msg += "{filename}:{line}:{column}: error: {error}".format(filename=self.srcFilename, line=error[1], column=column + 1, error=error[0]) + "\n"

            line = linecache.getline(self.srcFilename, error[1])[:-1]
            while len(line) and line[0] in [" ", "\t"]: # remove whitespace in front
                line = line[1:]
                column -= 1

            msg += line + "\n"
            msg += " " * (column) + "^\n"
        else:
            msg += "Error: {error}".format(error=error[0]) + "\n"

        return msg

    def errorsToString(self):
        s = ""

        for i, error in enumerate(self.errors):
            s += self.errorToString(i)

        return s

    def printError(self, index):
        print(self.errorToString(index), end="")

    def printErrors(self):
        for i in range(len(self.errors)):
            self.printError(i)
