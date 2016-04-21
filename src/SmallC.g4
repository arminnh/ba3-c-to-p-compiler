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
    | oplevel15
    ;

oplevel15 :
      oplevel14
    ;

oplevel14 :
      oplevel13 '=' oplevel14 // simple assignment
    | oplevel13
    ;

oplevel13 :
      oplevel12 '?' oplevel12 ':' oplevel13
    | oplevel12
    ;

oplevel12 :
      oplevel12 '||' oplevel11
    | oplevel11
    ;  
    
oplevel11 :
      oplevel11 '&&' oplevel10
    | oplevel10
    ;
    
oplevel10 :
      oplevel9
    ;

oplevel9 :
      oplevel8
    ;

oplevel8 :
      oplevel7
    ;

oplevel7 :
      oplevel7 '==' oplevel6
    | oplevel7 '!=' oplevel6
    | oplevel6
    ;
    
oplevel6 :
      oplevel6 '<' oplevel5
    | oplevel6 '<=' oplevel5
    | oplevel6 '>' oplevel5
    | oplevel6 '>=' oplevel5
    | oplevel5
    ;

oplevel5 :
      oplevel4
    ;

oplevel4 :
      oplevel4 '+' oplevel3
    | oplevel4 '-' oplevel3
    | oplevel3
    ;

oplevel3 :
      oplevel3 '*' oplevel2
    | oplevel3 '/' oplevel2
    | oplevel3 '%' oplevel2
    | oplevel2
    ;

oplevel2 :
      '++' oplevel2
    | '--' oplevel2
    | '&' oplevel1
    | '*' oplevel2
    | '!' oplevel2
    | numberLiteral
    | characterLiteral
    | LBRA typeDeclaration RBRA oplevel2
    | oplevel1
    ;

oplevel1 :
      oplevel1 '++'
    | oplevel1 '--'
    | variable
    | '(' expression ')'
    ;

variableDeclaration :
      typeDeclaration identifier ('=' expression)?
    ;
    
variable :
      identifier
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
      CFUN LBRA arguments RBRA
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

numberLiteral :
      FLOAT
    | INTEGER
    ;

floatLiteral :
      FLOAT
    ;
    
integerLiteral :
      INTEGER
    ;

characterLiteral :
      CHARACTER
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

