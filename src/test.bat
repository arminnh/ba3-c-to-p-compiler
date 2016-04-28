@echo off

echo Running Python3 tests with file tests.py

if not exist "./SmallCParser.py" GOTO build
if not exist "./SmallCLexer.py" GOTO build
if not exist "./SmallCLexer.tokens" GOTO build
if not exist "./SmallCListener.py" GOTO build
if not exist "./SmallCParser.py" GOTO build
if not exist "./SmallC.tokens" GOTO build

:test
python3 tests.py
GOTO end

echo Tests Done

:build
echo Missing some necessary files. Building before tests.
call ./build.bat
GOTO test

:end
