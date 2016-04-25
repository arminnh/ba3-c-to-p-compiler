// antlr keywords: import, fragment, lexer, parser, grammar, returns, locals, throws, catch, finally, mode, options, tokens, rule
grammar SmallC;

// parser rules (rule names start with lower case character)


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

program :
      header functions mainFunction
    ;

header :
      include*
    ;
    
include :
      '#include' LABRA stdInclude RABRA
    | '#include' customInclude
    ;

stdInclude :
      identifier '.' identifier // https://en.wikipedia.org/wiki/C_standard_library
    ;

customInclude :
      stringLiteral
    ;

functions :
      functionDeclaration* functionDefinition*
    ;

functionDeclaration :
      typeDeclaration identifier LBRA parameters RBRA ';'
    ;

functionDefinition :
      typeDeclaration identifier LBRA parameters RBRA statements
    ;

parameters :
    | parameter (',' parameter)*
    |
    ;

parameter :
      declarationSpecifier+ identifier
    | arrayParameter
    ;

arrayParameter :
      declarationSpecifier+ identifier (LSBRA integerLiteral? RSBRA)?
    ;

mainFunction :
      (TYPEINT 'main' LBRA parametersMain RBRA statements)?
    ;

parametersMain :
      TYPEVOID
    | 'int argc, char *argv[]'
    ;

statements :
      LCBRA statement* RCBRA
    ;

statement :
      statements
    | ifCond
    | whileCond
    | doWhileCond
    | expression ';'
    | variableDeclaration ';'
    | returnExpression ';'
    ;
    
expression :
      functionCall
    | variable
    | numberLiteral
    | textLiteral
    | oplevel15
    ;

arguments :
      expression (',' expression)*
    |
    ;

ifCond :
      IF LBRA expression RBRA statement elseCond?
    ;

elseCond:
      ELSE statement
    ;

whileCond :
      WHILE LBRA expression RBRA statement
    ;

doWhileCond :
      DO LCBRA statement* RCBRA WHILE LBRA expression RBRA ';'
      // DO LCBRA doWhileCondStatements RCBRA WHILE LBRA expression RBRA ';'
      // ; doWhileCondStatements : statement* ;
    ;

variableDeclaration :
      declarationSpecifier+ declaratorInitializer (',' declaratorInitializer)*
    ;

declarationSpecifier :
      typeDeclaration
    | cvQualifier
    ;

cvQualifier :
      CONST
//  | VOLATILE | MUTABLE
    ;

declaratorInitializer :
      identifier ('=' expression)?
    | arrayDeclaration
    ;

arrayDeclaration :
      identifier LSBRA integerLiteral? RSBRA ('=' LCBRA arguments RCBRA)?
    ;

returnExpression :
      RETURN expression
    ;

functionCall:
      identifier LBRA arguments RBRA // identifier is not completely correct, IDENTIFIER   : [a-zA-Z]+;
    ;


variable :
      identifier
    ;

textLiteral :
      characterLiteral
    | stringLiteral
    ;

numberLiteral :
      floatLiteral
    | integerLiteral
    ;


identifier : IDENTIFIER | pointer IDENTIFIER | reference IDENTIFIER;
pointer : '*';
reference : '&';

typeDeclaration : TYPECHAR | TYPEFLOAT | TYPEINT | TYPEVOID;

floatLiteral : FLOAT;
integerLiteral : INTEGER;
characterLiteral : CHARACTER;
stringLiteral : STRING;




// lexer rules (rule names start with capital character)
COMMA     : ',';
LBRA      : '(';
RBRA      : ')';
LABRA     : '<';
RABRA     : '>';
LCBRA     : '{';
RCBRA     : '}';
LSBRA     : '[';
RSBRA     : ']';
QUOTE     : '"';
OPERATOR  : [+-*/%];

TYPECHAR  : 'char';
TYPEFLOAT : 'float';
TYPEINT   : 'int';
TYPEVOID  : 'void';
CONST     : 'const';
VOLATILE  : 'volatile';
MUTABLE   : 'mutable';

//CFUN      : 'printf' | 'scanf';
IF        : 'if';
ELSE      : 'else';
DO        : 'do';
WHILE     : 'while';
FOR       : 'for';
BREAK     : 'break';
CONTINUE  : 'continue';
RETURN    : 'return';

COMMENT   : '//'~[\r\n]* -> skip;
MULTICOMMENT : '/*'(.)*?'*/' -> skip;

INTEGER   : [0-9]+;
FLOAT     : INTEGER '.' INTEGER ([eE] [+-]? INTEGER)?
          | INTEGER [eE] [+-]? INTEGER
          ;

IDENTIFIER   : [a-zA-Z0-9]+;
CHARACTER    : ['] (. | '\n') ['];
STRING       : ["] ( [\\] [\\"nr] | ~[\\"\r\n] )* ["];

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines, \r (Windows)
