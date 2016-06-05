import linecache


class Error:
    def __init__(self, message, lineNumber, column, isWarning=False):
        self.message    = message
        self.lineNumber = lineNumber
        self.column     = column
        self.isWarning  = isWarning


class ErrorHandler:
    def __init__(self, srcFilename):
        self.srcFilename = srcFilename
        self.errors = []

    def addError(self, message, lineNumber, column):
        self.errors.append(Error(message, lineNumber, column, isWarning=False))

    def addWarning(self, message, lineNumber, column):
        self.errors.append(Error(message, lineNumber, column, isWarning=True))

    def errorCount(self):
        return len(list([True for error in self.errors if not error.isWarning]))

    def warningCount(self):
        return len(list([True for error in self.errors if error.isWarning]))

    def errorToString(self, index):
        msg = ""
        error = self.errors[index]

        if error.lineNumber is not None and error.column is not None:
            column = error.column
            msg += "{filename}:{line}:{column}: {isError}: {error}\n".format(filename=self.srcFilename, line=error.lineNumber, column=column + 1, error=error.message, isError=("error" if not error.isWarning else "warning"))

            line = linecache.getline(self.srcFilename, error.lineNumber)[:-1]

            msg += " " + line + "\n"
            msg += " " + " " * (column) + "^\n"
        else:
            msg += "Error: {error}\n".format(error=error.message)

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
