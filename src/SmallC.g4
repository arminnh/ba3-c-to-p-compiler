// antlr keywords: import, fragment, lexer, parser, grammar, returns, locals, throws, catch, finally, mode, options, tokens, rule
grammar SmallC;

///////////////////////////////////////////////////////////////
// PARSER RULES (rule names start with lower case character) //
///////////////////////////////////////////////////////////////

// oplevel15 is the highest level of expression, parsing expressions begins at level15 and can go down to level1
oplevel15
    : oplevel15 ',' oplevel14
    | oplevel14
    ;

oplevel14
    : oplevel13 '=' oplevel14 // simple assignment
    | oplevel13
    ;

oplevel13
    : oplevel12 '?' oplevel12 ':' oplevel13
    | oplevel12
    ;

oplevel12
    : oplevel12 '||' oplevel11
    | oplevel11
    ;

oplevel11 :
      oplevel11 '&&' oplevel7
    | oplevel7
    ;

oplevel10
    : oplevel9
    ;

oplevel9
    : oplevel8
    ;

oplevel8
    : oplevel7
    ;

oplevel7
    : oplevel7 '==' oplevel6
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

oplevel5
    : oplevel4
    ;

oplevel4
    : oplevel4 '+' oplevel3
    | oplevel4 '-' oplevel3
    | oplevel3
    ;

oplevel3
    : oplevel3 '*' oplevel2
    | oplevel3 '/' oplevel2
    | oplevel3 '%' oplevel2
    | oplevel2
    ;

oplevel2
    : '++' oplevel2
    | '--' oplevel2
    | '+' oplevel2
    | '-' oplevel2
    | '&' oplevel2 // address of
    | '*' oplevel2 // dereference
    | '!' oplevel2
    | typeCast
    | oplevel1
    ;

oplevel1
    : oplevel1 '++'
    | oplevel1 '--'
    | oplevel1 '[' oplevel15 ']'
    | variable
    | floatLiteral
    | integerLiteral
    | characterLiteral
    | stringLiteral
    | '(' oplevel15 ')'
    | functionCall
    ;

typeCast
    : '(' declarationSpecifier+ pointerPart* ')' oplevel2
    ;

program
    : (include | functionDeclaration | functionDefinition | variableDeclaration ';')*
    ;

include
    : '#include' '<' stdInclude '>'
    | '#include' customInclude
    ;

stdInclude
    : identifier '.' identifier // https://en.wikipedia.org/wiki/C_standard_library
    ;

customInclude
    : stringLiteral
    ;

functionDeclaration
    : declarationSpecifier* pointerPart* identifier '(' parameters ')' ';'
    ;

functionDefinition
    : declarationSpecifier* pointerPart* identifier '(' parameters ')' statements
    ;

parameters
    : parameter (',' parameter)*
    |
    ;

parameter
    : declarationSpecifier+ paramDeclarator
    ;

paramDeclarator
    : '(' paramDeclarator1 ')'
    | paramDeclarator1
    ;

paramDeclarator1
    : pointerPart* '(' paramDeclarator1 ')' arrayPart*
    | pointerPart* identifier? arrayPart*
    ;

pointerPart
    : '*' cvQualifier?
    ;

arrayPart
    : '[' oplevel15? ']'
    ;

statements
    : '{' statement* '}'
    ;

statement
    : statements
    | ifCond
    | whileCond
    | doWhileCond
    | forLoop
    | oplevel15 ';'
    | variableDeclaration ';'
    | returnStmt ';'
    | breakStmt ';'
    | continueStmt ';'
    | ';'
    ;

ifCond
    : IF '(' oplevel15 ')' statement elseCond?
    ;

elseCond
    : ELSE statement
    ;

whileCond
    : WHILE '(' oplevel15 ')' statement
    ;

doWhileCond
    : DO statements WHILE '(' oplevel15 ')' ';'
    ;

forLoop
    : FOR '(' forLoopInitStatement ';' forLoopCondition ';' forLoopIterationExpression ')' statement
    ;

forLoopInitStatement
    : variableDeclaration
    | oplevel15
    |
    ;

forLoopCondition
    : oplevel15
    |
    ;

forLoopIterationExpression
    : oplevel15
    |
    ;

variableDeclaration
    : declarationSpecifier+ (declaratorInitializer) (',' declaratorInitializer)*
    ;

declarationSpecifier
    : typeDeclaration
    | cvQualifier
    ;

cvQualifier
    : CONST //| VOLATILE | MUTABLE
    ;

declaratorInitializer
    : '(' declarator1 ')' ('=' initializer)?
    | declarator1 ('=' initializer)?
    ;

declarator1
    : pointerPart* '(' declarator1 ')' arrayPart*
    | pointerPart* identifier arrayPart*
    ;

initializer
    : '{' (oplevel14 (',' oplevel14)*)?   '}'
    | '{' (initializer (',' initializer)*)? '}'
    | oplevel14
    ;

returnStmt
    : RETURN oplevel15?
    ;

breakStmt
    : BREAK
    ;

continueStmt
    : CONTINUE
    ;

arguments
    : oplevel14 (',' oplevel14)*
    |
    ;

functionCall
    : identifier '(' arguments ')'
    ;

variable
    : identifier
    ;


identifier : IDENTIFIER;
pointer : '*';

typeDeclaration : TYPECHAR | TYPEFLOAT | TYPEINT | TYPEVOID;

floatLiteral     : FLOAT /*| FLOAT floatSpecifier*/;
/*floatSpecifier   : 'f';*/
integerLiteral   : INTEGER;
characterLiteral : CHARACTER;
stringLiteral    : STRING;

///////////////////////////////////////////////////////////////
//   LEXER RULES (rule names start with capital character)   //
///////////////////////////////////////////////////////////////

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
