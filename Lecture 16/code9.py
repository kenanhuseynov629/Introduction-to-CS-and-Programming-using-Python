def my_rev(L):
    if len(L) == 1:
        return L
    else:
        return my_rev(L[1:]) + [L[0]]

test1 = [1, 2, "abc"]
print(my_rev(test1))  # Nəticə: ['abc', 2, 1]

test2 = ["abc", ['d'], ['e', ['f', 'g']]]
print(my_rev(test2))  # Nəticə: [['e', ['f', 'g']], ['d'], 'abc']