# create files for java tree visualisation
java -jar ../resources/antlr-4.5.2-complete.jar SmallC.g4 -visitor
javac -classpath ../resources/antlr-4.5.2-complete.jar SmallC*.java

# move java files to build dir
if [ -d "build" ]; then
    rm -r build/*
else
    mkdir build
fi
mv *.java *.class build/

# create python files
java -jar ../resources/antlr-4.5.3-complete.jar -Dlanguage=Python3 SmallC.g4 -visitor

# run visualisation
(cd build && java -cp ../../resources/antlr-4.5.3-complete.jar: org.antlr.v4.gui.TestRig SmallC program -gui ../testfiles/hello_world.c)
#(cd build && java -cp ../../resources/antlr-4.5.2-complete.jar: org.antlr.v4.gui.TestRig SmallC program -gui ../testfiles/hello_world0.c ../testfiles/hello_world.c )
