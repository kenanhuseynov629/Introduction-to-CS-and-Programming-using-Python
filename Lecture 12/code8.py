def is_pal(x):
    """
    Siyahı x-in palindrom olub-olmadığını yoxlayır.
    """
    temp = x[:]
    temp.reverse()
    if temp == x:
        return True
    else:
        return False

print(is_pal(list('ab')))