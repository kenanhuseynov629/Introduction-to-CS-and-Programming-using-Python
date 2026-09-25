def total_len_recur(L):
    """
    L daxilindəki bütün sətirlərin ümumi simvol uzunluğunu qaytarır.
    """
    if len(L) == 0:
        return 0
    else:
        return len(L[0]) + total_len_recur(L[1:])

test = ["ab", "c", "defgh"]
print(total_len_recur(test))  # Nəticə: 8 (çünki 2 + 1 + 5 = 8)