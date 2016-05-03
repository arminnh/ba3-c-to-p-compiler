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
    | '&' oplevel1 // address of
    | '*' oplevel2 // dereference
    | '!' oplevel2
    | functionCall
    | LBRA typeDeclaration RBRA oplevel2
    | oplevel1
    ;

oplevel1 :
      oplevel1 '++'
    | oplevel1 '--'
    | oplevel1 '[' expression ']'
    | variable
    | floatLiteral
    | integerLiteral
    | characterLiteral
    | stringLiteral
    | '(' expression ')'
    ;

program :
      (include | functionDeclaration | functionDefinition | variableDeclaration ';')*
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

functionDeclaration :
      declarationSpecifier+ pointerPart* identifier LBRA parameters RBRA ';'
    ;

functionDefinition :
      declarationSpecifier+ pointerPart* identifier LBRA parameters RBRA statements
    ;

parameters :
    | parameter (',' parameter)*
    |
    ;

parameter :
      declarationSpecifier+ pointerPart* identifier? arrayPart?;

pointerPart:
      pointer cvQualifier?
    ;

arrayPart :
      LSBRA expression? RSBRA
    ;
/*
mainFunction :
      TYPEINT MAIN LBRA parametersMain RBRA statements
    ;

parametersMain :
      TYPEVOID
    | 'int argc, char *argv[]'
    |
    ;
*/
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
    | returnStmt ';'
    | ';'
    ;

expression :
      variable
    | floatLiteral
    | integerLiteral
    | characterLiteral
    | stringLiteral
    | functionCall
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
      DO statements WHILE LBRA expression RBRA ';'
    ;

variableDeclaration :
      declarationSpecifier+ (declaratorInitializer) (',' declaratorInitializer)*
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
      pointerPart* identifier ('=' expression)?
    | pointerPart* identifier arrayPart ('=' (LCBRA arguments RCBRA | expression))?
    ;

returnStmt :
      RETURN expression
    ;

functionCall:
      identifier LBRA arguments RBRA // identifier is not completely correct, IDENTIFIER   : [a-zA-Z]+;
    ;

variable :
      identifier
    ;


identifier : IDENTIFIER;
pointer : '*';

typeDeclaration : TYPECHAR | TYPEFLOAT | TYPEINT | TYPEVOID;

floatLiteral     : FLOAT;
integerLiteral   : INTEGER;
characterLiteral : CHARACTER;
stringLiteral    : STRING;




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
//MAIN      : 'main';

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
