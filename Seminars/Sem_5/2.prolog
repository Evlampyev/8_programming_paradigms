# Максимальный элемент в списке

find_max([X], X).
find_max([C|T], Max) :- find_max(T, Max1),
    (C > Max1, Max is C; Max is Max1).


?- find_max([1,6,3,4,5], X), write(X).