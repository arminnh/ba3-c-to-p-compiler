java -jar ../resources/antlr-4.5.2-complete.jar SmallC.g4 -visitor
java -jar ../resources/antlr-4.5.2-complete.jar -Dlanguage=Python3 SmallC.g4 -visitor
javac -classpath ../resources/antlr-4.5.2-complete.jar SmallC*.java
cat testfiles/hello_world.c | java -cp ../resources/antlr-4.5.2-complete.jar: org.antlr.v4.gui.TestRig SmallC program -gui

