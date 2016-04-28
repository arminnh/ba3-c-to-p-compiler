#!/bin/bash

echo "Generating Python3 files for grammar SmallC.g4"

# create python files
java -jar ./antlr-4.5.3-complete.jar -Dlanguage=Python3 SmallC.g4 #-visitor

echo "Generating done"
