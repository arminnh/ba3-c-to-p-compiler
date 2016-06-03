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
      oplevel11 '&&' oplevel7
    | oplevel7
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
      oplevel6 '<' oplevel4
    | oplevel6 '<=' oplevel4
    | oplevel6 '>' oplevel4
    | oplevel6 '>=' oplevel4
    | oplevel4
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
    | '+' oplevel2
    | '-' oplevel2
    | '&' oplevel2 // address of
    | '*' oplevel2 // dereference
    | '!' oplevel2
    | functionCall
    | typeCast
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

typeCast :
      '(' declarationSpecifier+ pointerPart* ')' oplevel2
    ;

program :
      (include | functionDeclaration | functionDefinition | variableDeclaration ';')*
    ;

include :
      '#include' '<' stdInclude '>'
    | '#include' customInclude
    ;

stdInclude :
      identifier '.' identifier // https://en.wikipedia.org/wiki/C_standard_library
    ;

customInclude :
      stringLiteral
    ;

functionDeclaration :
      declarationSpecifier+ pointerPart* identifier '(' parameters ')' ';'
    ;

functionDefinition :
      declarationSpecifier+ pointerPart* identifier '(' parameters ')' statements
    ;

parameters :
    | parameter (',' parameter)*
    |
    ;

parameter :
      declarationSpecifier+ paramDeclarator
    ;

paramDeclarator :
      '(' paramDeclarator1 ')'
    | paramDeclarator1
    ;

paramDeclarator1 :
      pointerPart* '(' paramDeclarator1 ')' arrayPart*
    | pointerPart* identifier? arrayPart*
    ;

pointerPart:
      pointer cvQualifier?
    ;

arrayPart :
      '[' expression? ']'
    ;

statements :
      '{' statement* '}'
    ;

statement :
      statements
    | ifCond
    | whileCond
    | doWhileCond
    | forLoop
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
    | oplevel14
    ;

ifCond :
      IF '(' expression ')' statement elseCond?
    ;

elseCond :
      ELSE statement
    ;

whileCond :
      WHILE '(' expression ')' statement
    ;

doWhileCond :
      DO statements WHILE '(' expression ')' ';'
    ;

// TODO: add forLoopNode and all the rest for scope and type checking
forLoop :
      FOR '(' forLoopInitStatement ';' forLoopCondition ';' forLoopIterationExpression ')' statement
    ;

forLoopInitStatement :
      variableDeclaration
    | expression
    |
    ;

forLoopCondition :
      expression
    |
    ;

forLoopIterationExpression :
      expression
    |
    ;

variableDeclaration :
      declarationSpecifier+ (declaratorInitializer) (',' declaratorInitializer)*
    ;

declarationSpecifier :
      typeDeclaration
    | cvQualifier
    ;

cvQualifier :
      CONST //| VOLATILE | MUTABLE
    ;

declaratorInitializer :
      '(' declarator1 ')' ('=' initializer)?
    | declarator1 ('=' initializer)?
    ;

declarator1 :
      pointerPart* '(' declarator1 ')' arrayPart*
    | pointerPart* identifier arrayPart*
    ;

initializer :
      '{' (expression (',' expression)*)?   '}'
    | '{' (initializer (',' initializer)*)? '}'
    | expression
    ;

returnStmt :
      RETURN expression?
    ;

arguments :
      expression (',' expression)*
    |
    ;

functionCall:
      identifier '(' arguments ')'
    ;

variable :
      identifier
    ;


identifier : IDENTIFIER;
pointer : '*';

typeDeclaration : TYPECHAR | TYPEFLOAT | TYPEINT | TYPEVOID;

floatLiteral     : FLOAT /*| FLOAT floatSpecifier*/;
/*floatSpecifier   : 'f';*/
integerLiteral   : INTEGER;
characterLiteral : CHARACTER;
stringLiteral    : STRING;


// lexer rules (rule names start with capital character)
TYPECHAR  : 'char';
TYPEFLOAT : 'float';
TYPEINT   : 'int';
TYPEVOID  : 'void';
CONST     : 'const';
VOLATILE  : 'volatile';
MUTABLE   : 'mutable';

IF        : 'if';
ELSE      : 'else';
DO        : 'do';
WHILE     : 'while';
FOR       : 'for';
BREAK     : 'break';
CONTINUE  : 'continue';
RETURN    : 'return';
//MAIN    : 'main';

COMMENT      : '//'~[\r\n]* -> skip;
MULTICOMMENT : '/*'(.)*?'*/' -> skip;

INTEGER   : [0-9]+;
FLOAT     : INTEGER '.' INTEGER ([eE] [+-]? INTEGER)?
          | INTEGER [eE] [+-]? INTEGER
          ;

IDENTIFIER   : [a-zA-Z_][a-zA-Z0-9\_]*;
CHARACTER    : ['] (. | '\n') ['];
STRING       : ["] ( [\\] [\\"nr] | ~[\\"\r\n] )* ["];

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines, \r (Windows)
