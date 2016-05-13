echo "This script is meant to be run from the src directory" # because i don't know how to bash

if [[ ! $1 ]]; then
	echo "Usage: $0 filename"
	exit
fi

if [ -d "visualisation_java/" ]; then
    rm -r visualisation_java/*
fi

# create files for java tree visualisation
java -jar ./antlr-4.5.3-complete.jar -o visualisation_java SmallC.g4

cd visualisation_java
javac -classpath ../antlr-4.5.3-complete.jar SmallC*.java

# run visualisation
java -cp ../../resources/antlr-4.5.3-complete.jar: org.antlr.v4.gui.TestRig SmallC program -gui ../$1
cd ..
