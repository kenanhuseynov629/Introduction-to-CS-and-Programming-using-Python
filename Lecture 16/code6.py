def in_list_simplified(L, e):
    if len(L) == 0:
        return False
    elif L[0] == e:  # Bütöv L yox, siyahının ilk elementi
        return True
    else:
        return in_list_simplified(L[1:], e)


L = [1, 2, 3, 4, 5]
print(in_list_simplified(L, 6))