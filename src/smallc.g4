grammar smallc;

// antlr keywords: import, fragment, lexer, parser, grammar, returns, locals, throws, catch, finally, mode, options, tokens, rule

// parser rules (rule names start with lower case character)
program : header mainFunction;

header : includes;

includes : '#include' LABRA ID '.' ID RABRA
    |
    ;

mainFunction : ;

// lexer rules (rule names start with capital character)
ID : [a-z]+ ;             // match lower-case identifiers
STRING : '(.*?)';
NUMBER : [0-9]+;
COMMA : ',';
LBRA : '(';
RBRA : ')';
LABRA : '<';
RABRA : '>';
LCBRA : '{';
RCBRA : '}';
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines, \r (Windows)


/* lists
    lst : LBRACKET seq RBRACKET {print("another list %d:%d" % ($LBRACKET.line, $LBRACKET.pos))};

    // lst : LBRACKET! seq^ RBRACKET! {print("another list %d:%d" % ($LBRACKET.line, $LBRACKET.pos))};
    // normally ! will delete the token from the parse tree, ^ will make the token root,
    //use -> for a rewrite rule (not supported anymore in ANTLR 4: http://scottschanel.blogspot.be/2014/01/antlr4-vs-antlr-3.html)


    seq : ( item ( COMMA seq ) * )?;
    item : number | lst;
    number : NUMBER; // so number becomes a parse tree node type
*/
