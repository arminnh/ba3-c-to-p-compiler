#!/bin/bash

echo "Running Python3 tests with file /src/tests/main.py"

if [ ! -f "antlr4_generated/SmallCParser.py" -o ! -f "antlr4_generated/SmallCLexer.py" -o ! -f "antlr4_generated/SmallCLexer.tokens" -o ! -f "antlr4_generated/SmallCListener.py" -o ! -f "antlr4_generated/SmallCParser.py"  -o ! -f "antlr4_generated/SmallC.tokens" ]; then
    echo "Missing some necessary files. Building before tests."

    source ./build.sh
fi

cd tests/
python3 main.py
cd ..

echo "Tests Done"
