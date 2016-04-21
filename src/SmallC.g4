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
      LABRA stringLiteral RABRA
    | stringLiteral
    ;

stdInclude :
      
    ;
    
customInclude :
      
    ;

statements :
      statement*
    ;

statement :
      statementBody ';'
    ;

statementBody :
      expression
    | variableDeclaration
    | RETURN expression
    ;

expression :
      functionCall
    | variable
    | integerLiteral
    | stringLiteral
    | floatLiteral
    ;

variableDeclaration :
      typeDeclaration identifier ('=' expression)?
    ;
    
variable :
      identifier
    ;

arithmeticop :
      integerLiteral OPERATOR integerLiteral
      variable OPERATOR variable
    ;

functionDeclaration :
    ;

functionDefinition :
    ;

mainFunction :
      typeDeclaration 'main' LBRA 'void' RBRA LCBRA statements RCBRA
    ;

typeDeclaration :
      TYPECHAR
    | TYPEFLOAT
    | TYPEINT
    ;

functionCall:
      CFUN LBRA arguments? RBRA
    ;
    
arguments :
    | argument (',' argument)*
    |
    ;
    
argument :
      stringLiteral
    | integerLiteral
    | variable
    | floatLiteral
    ;

floatLiteral :
      FLOAT
    ;
    
integerLiteral :
      INTEGER
    ;

stringLiteral :
      STRING
    ;

identifier :
      IDENTIFIER
    ;



// lexer rules (rule names start with capital character)
COMMA     : ',';
LBRA      : '(';
RBRA      : ')';
LABRA     : '<';
RABRA     : '>';
LCBRA     : '{';
RCBRA     : '}';
QUOTE     : '"';
OPERATOR  : [+-*/%];

TYPECHAR  : 'char';
TYPEFLOAT : 'float';
TYPEINT   : 'int';

CFUN      : 'printf' | 'scanf';
RETURN    : 'return';

COMMENT   : '//'~[\r\n]* -> skip;

INTEGER   : [0-9]+;
FLOAT     : INTEGER . INTEGER ([eE] [+-]? INTEGER)?
          | INTEGER [eE] [+-]? INTEGER
          ;

IDENTIFIER   : [a-zA-Z]+;
CHARACTER    : ['] (. | '\n') ['];
STRING       : ["] ( [\\] [\\"nr] | ~[\\"\r\n] )* ["];

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines, \r (Windows)
