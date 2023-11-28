grammar Gramatica;
// Tokens
ID : [a-zA-Z]+ ; // Identificadores
INT : [0-9]+ ;   // Números enteros
NEXLINE: '\r'?'\n';
WS : [ \t]+ -> skip ; // Espacios en blanco
apagar: 'apagar';






// Reglas de la gramática extendida
//compilar: antlr4 -visitor -no-listener -Dlanguage=Python3 Gramatica.g4
prog : statement+ ;

runStatemen: 'run(' INT ',' INT ')';
runItStatemen: 'run(' INT ',' INT ',' INT ')';
runItPStatemen: 'run(' INT ',' INT ',' INT ',(' INT ',' INT ',' INT ')';

statement : runStatemen | runItStatemen | runItPStatemen | apagar;





