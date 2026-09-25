def flatten(L):
    """
    L daxilində siyahılar olan bir siyahıdır.
    Bütün daxili siyahıların elementlərini tək bir siyahıda birləşdirir.
    """
    if len(L) == 1:
        return L[0]
    else:
        return L[0] + flatten(L[1:])

test = [[4, 5], [8, 9], [7, 10, 11]]
print(flatten(test))  # Nəticə: [4, 5, 7-11]