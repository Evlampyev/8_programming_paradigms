% Нахождение суммы элементов списка


% Rules
summa([X], X).
summa([C|T], Sum) :-
    summa(T, Sum1), Sum is Sum1 + C.

% Query
?- summa([1, 2, 3, 4], X), write(X).