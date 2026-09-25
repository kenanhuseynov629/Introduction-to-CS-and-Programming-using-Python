def in_lists_of_list(L, e):
    """L elementləri siyahı olan bir siyahıdır.

    e elementi daxili siyahıların içində varsa True, yoxdursa False qaytarır.
    """
    if len(L) == 0:
        return False
    elif e in L[0]:  # İlk daxili siyahının içində axtarırıq
        return True
    else:
        return in_lists_of_list(L[1:], e)


test = [[4, 5], [8, 9], [6, 11, 12]]
print(in_lists_of_list(test, 5))  # True
print(in_lists_of_list(test, 3))  # False
print(in_lists_of_list(test, 0))  # False