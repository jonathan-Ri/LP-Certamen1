grammar Gramatica;
// Tokens
ID : [a-zA-Z]+ ; // Identificadores
INT : [0-9]+ ;   // Números enteros
NEXLINE: '\r'?'\n';
WS : [ \t]+ -> skip ; // Espacios en blanco
ESPACIO:  INT ;
CAPAS:  INT ;
ITERACIONES:  INT ;
PACIENTE0 : '(' INT ',' INT ',' INT ')';
RUN: 'run(' ESPACIO ',' CAPAS ',' ITERACIONES ')';
RUN2: 'run(' ESPACIO ',' CAPAS ',' ITERACIONES ',' PACIENTE0 ')';
RUN3: 'run(' ESPACIO ',' CAPAS ')';


// Reglas de la gramática extendida
//compilar: antlr4 -visitor -no-listener -Dlanguage=Python3 Gramatica.g4
prog : statement+ ;
// run((5),(3),(4))
statement : RUN | RUN2 | RUN3 ;