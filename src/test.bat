@echo off

echo Running Python3 tests with file /src/tests/main.py

if not exist "antlr4_generated\CParser.py" GOTO build
if not exist "antlr4_generated\CLexer.py" GOTO build
if not exist "antlr4_generated\CLexer.tokens" GOTO build
if not exist "antlr4_generated\CListener.py" GOTO build
if not exist "antlr4_generated\CParser.py" GOTO build
if not exist "antlr4_generated\C.tokens" GOTO build

:test
cd tests/
python3 main.py
cd ..
GOTO end

echo Tests Done

:build
echo Missing some necessary files. Building before tests.
call ./build.bat
GOTO test

:end
