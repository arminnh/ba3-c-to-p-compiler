grammar NestedLists;

nstdlst : '(' lst ')';

lst : itm
  | itm (',' itm)*
  | ;

itm : '(' lst ')'
     | INT;

INT : ['-']?[0-9]+;

