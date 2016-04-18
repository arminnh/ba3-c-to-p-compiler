grammar lists;

// parser rules (rule names start with lower case character)
lst : LBRACKET seq RBRACKET {print("another list %d:%d" % ($LBRACKET.line, $LBRACKET.pos))};

// lst : LBRACKET! seq^ RBRACKET! {print("another list %d:%d" % ($LBRACKET.line, $LBRACKET.pos))}; 
// normally ! will delete the token from the parse tree, ^ will make the token root, 
//use -> for a rewrite rule (not supported anymore in ANTLR 4: http://scottschanel.blogspot.be/2014/01/antlr4-vs-antlr-3.html)
seq : ( item ( COMMA seq ) * )?; 
item : number | lst;
number : NUMBER; // so number becomes a parse tree node type

// lexer rules (rule names start with capital character)
NUMBER : [0-9]+;
COMMA : ',';
LBRACKET : '(';
RBRACKET : ')';
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines, \r (Windows)
