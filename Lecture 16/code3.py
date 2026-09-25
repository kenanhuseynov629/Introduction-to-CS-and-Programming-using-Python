def total_iter(L):
    result = 0
    for e in L:
        result += e
    return result

test = [1, 2, 3]
print(total_iter(test))