@echo off

echo Running Python3 tests with file /src/tests/main.py

if not exist "antlr4_generated\SmallCParser.py" GOTO build
if not exist "antlr4_generated\SmallCLexer.py" GOTO build
if not exist "antlr4_generated\SmallCLexer.tokens" GOTO build
if not exist "antlr4_generated\SmallCListener.py" GOTO build
if not exist "antlr4_generated\SmallCParser.py" GOTO build
if not exist "antlr4_generated\SmallC.tokens" GOTO build

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
