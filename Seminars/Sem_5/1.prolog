# Поиск родителя
men(sergey, male).

men(vera, female).
men(vera, female).

parent(lubov, vera).
parent(sergey, vera).


father(X, Y):- parent(X,Y), men(X, male).

?- father(X, vera), write(X).