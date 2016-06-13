echo "This script is meant to be run from the src directory" # because i don't know how to bash

if [[ ! $1 ]]; then
	echo "Usage: $0 filename"
	exit
fi

if [ -d "visualisation_java/" ]; then
    rm -r visualisation_java/*
fi

# create files for java tree visualisation
java -jar ../resources/antlr-4.5.3-complete.jar -o visualisation_java C.g4

cd visualisation_java
javac -classpath ../../resources/antlr-4.5.3-complete.jar C*.java

# run visualisation
java -cp ../../resources/antlr-4.5.3-complete.jar: org.antlr.v4.gui.TestRig C program -gui ../$1
cd ..
