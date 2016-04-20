// antlr keywords: import, fragment, lexer, parser, grammar, returns, locals, throws, catch, finally, mode, options, tokens, rule
grammar smallc;

// parser rules (rule names start with lower case character)
program :
      header mainFunction
    ;

header :
      includes
    ;

includes :
      '#include' LABRA ID '.' ID RABRA
    |
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
      CFUN LBRA STRING RBRA ';'
    | RETURN NUMBER ';'
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

CHAR   : 'char';
FLOAT  : 'float';
INT    : 'int';
CFUN   : 'printf' | 'scanf';
RETURN : 'return';

ID     : [a-zA-Z]+;
NUMBER : [1-9][0-9]* | [0];
STRING : ["].*?["];

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines, \r (Windows)
