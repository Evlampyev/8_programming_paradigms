female(galina).
female(olga).
female(anastasiya).
female(lubov).
female(vera).
male(vladimir).
male(sergey).
male(aleksey).
male(aleksandr).
male(serafim).

parent(lubov, vera).
parent(sergey, vera).
parent(vladimir, aleksey).
parent(galina, aleksey).
parent(aleksey, olga).
parent(vera, olga).
parent(aleksey, anastasiya).
parent(vera, anastasiya).
parent(anastasiya, serafim).
parent(aleksandr, serafim).


grandpa(X, Y) :- parent(X, Z), parent(Z, Y), male(X).
father(X, Y) :- parent(X, Y), male(X).

?- father(X, vera), write(X), write('\n').
?- grandpa(X, serafim), write(X).