def add(a, b):
    """
    a-ya 1 əlavə etməklə b dəfə toplamanı rekursiv yerinə yetirir.
    """
    if b == 0:
        return a
    else:
        return 1 + add(a, b - 1)

print(add(3, 4))  # Çıxış: 7