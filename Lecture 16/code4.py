def total_recur(L):
    if len(L) == 0:
        return 0
    else:
        # Birinci ədədi götürürük və qalan siyahının cəmi ilə toplayırıq
        return L[0] + total_recur(L[1:])

test = [1, 2, 3]
print(total_recur(test))  # Nəticə: 6