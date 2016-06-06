@echo off

echo Generating Python3 files for grammar C.g4

:: create python files
java -jar ./antlr-4.5.3-complete.jar -o antlr4_generated -Dlanguage=Python3 C.g4

echo Generating done
