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
    | returnExpression
    ;

expression :
      functionCall
    | variable
    | numberLiteral
    | textLiteral
    | oplevel15
    ;

returnExpression :
      RETURN expression
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
    | textLiteral
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
      typeDeclaration 'main' LBRA arguments RBRA LCBRA statements RCBRA
    ;

typeDeclaration :
      TYPECHAR
    | TYPEFLOAT
    | TYPEINT
    ;

functionCall:
      identifier LBRA arguments RBRA // identifier is not completely correct, IDENTIFIER   : [a-zA-Z]+;
    ;

arguments :
    | argument (',' argument)*
    |
    ;

argument :
      numberLiteral
    | textLiteral
    | variable
    ;

floatLiteral :
      FLOAT
    ;

integerLiteral :
      INTEGER
    ;

numberLiteral :
      floatLiteral
    | integerLiteral
    ;

characterLiteral :
      CHARACTER
    ;

stringLiteral :
      STRING
    ;

textLiteral :
      characterLiteral
    | stringLiteral
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

//CFUN      : 'printf' | 'scanf';
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
