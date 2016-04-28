#!/bin/bash

echo "Running Python3 tests with file tests.py"

if [ ! -f "./SmallCParser.py" -o ! -f "./SmallCLexer.py" -o ! -f "./SmallCLexer.tokens" -o ! -f "./SmallCListener.py" -o ! -f "./SmallCParser.py"  -o ! -f "./SmallC.tokens" ]; then
    echo "Missing some necessary files. Building before tests."

    source ./build.sh
fi

python3 tests.py

echo "Tests Done"
