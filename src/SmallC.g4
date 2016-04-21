// antlr keywords: import, fragment, lexer, parser, grammar, returns, locals, throws, catch, finally, mode, options, tokens, rule
grammar SmallC;

// parser rules (rule names start with lower case character)
program :
      header mainFunction
    ;

header :
      ('#include' include)*
    ;

include :
      LABRA STRING1 RABRA
    | STRING2
    ;

stdInclude :
      
    ;
    
customInclude :
      
    ;

mainFunction :
      typeDecl 'main' LBRA 'void' RBRA LCBRA (functionBody)+ RCBRA
    ;

typeDecl :
      CHAR
    | FLOAT
    | INT
    ;

functionBody:
      CFUN LBRA STRING2 RBRA ';'
    | RETURN number ';'
    ;

number :
      NUMBER
    ;

// lexer rules (rule names start with capital character)
PTR   : '*';
COMMA : ',';
LBRA  : '(';
RBRA  : ')';
LABRA : '<';
RABRA : '>';
LCBRA : '{';
RCBRA : '}';
QUOTE : '"';

CHAR   : 'char';
FLOAT  : 'float';
INT    : 'int';
CFUN   : 'printf' | 'scanf';
RETURN : 'return';

NUMBER : [0-9]+;

//ID     : [a-zA-Z]+;
//TEXT   : [a-zA-Z\-\.\_\\\s]+;
//STRING : ["].*?["];

STRING1 : ~[\\"\r\n];
STRING2 : '"' ( '\\' [\\"] | STRING1 ) '"';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines, \r (Windows)
