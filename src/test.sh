#!/bin/bash

echo "Running Python3 tests with file /src/tests/main.py"

if [ ! -f "antlr4_generated/CParser.py" -o ! -f "antlr4_generated/CLexer.py" -o ! -f "antlr4_generated/CLexer.tokens" -o ! -f "antlr4_generated/CListener.py" -o ! -f "antlr4_generated/CParser.py"  -o ! -f "antlr4_generated/C.tokens" ]; then
    echo "Missing some necessary files. Building before tests."

    source ./build.sh
fi

cd tests/
python3 main.py
cd ..

echo "Tests Done"
