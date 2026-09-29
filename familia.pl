% padres

padre(juan, carla).
padre(juan, jose). 
padre(juan, agustin).
padre(agustin, mateo).
padre(jose, luis).

% madres

madre(maria, carla).
madre(maria, jose).
madre(maria, agustin).
madre(sofia, mateo).
madre(ana, luis).

% reglas

% abuelos

abuelo(X, Y) :- padre(X, Z), padre(Z, Y).
abuela(X, Y) :- madre(X, Z), madre(Z, Y).

% hermanos
hermano(X, Y) :- padre(Z, X), padre(Z, Y), madre(W, X), madre(W, Y), X \= Y.

% tios

tio(X, Y) :- hermano(X, Z), padre(Z, Y).
tia(X, Y) :- hermana(X, Z), madre(Z, Y).

% Consultas De Prueba

%- abuelo(juan, mateo).
% true.

%- abuelo(juan, luis).
% true.

%- hermano(carla, jose).
% true.

% hermano(jose, agustin).
% true.

% tio(agustin, luis).
% true.

