echo "This script is meant to be run from the src directory" # because i don't know how to bash

if [[ ! $1 ]]; then
	echo "Usage: $0 filename"
	exit
fi

# create files for java tree visualisation
java -jar ../resources/antlr-4.5.3-complete.jar SmallC.g4 #-visitor
javac -classpath ../resources/antlr-4.5.3-complete.jar SmallC*.java

# move java files to build dir
if [ -d "build" ]; then
    rm -r build/*
else
    mkdir build
fi
mv *.java *.class build/

# create python files
java -jar ../resources/antlr-4.5.3-complete.jar -Dlanguage=Python3 SmallC.g4 #-visitor

# run visualisation
(cd build && java -cp ../../resources/antlr-4.5.3-complete.jar: org.antlr.v4.gui.TestRig SmallC program -gui ../$1)
#(cd build && java -cp ../../resources/antlr-4.5.2-complete.jar: org.antlr.v4.gui.TestRig SmallC program -gui ../testfiles/hello_world0.c ../testfiles/hello_world.c )
