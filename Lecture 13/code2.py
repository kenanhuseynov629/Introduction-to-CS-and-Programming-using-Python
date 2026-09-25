def sum_digits(s):
    """
    s rəqəmlərdən ibarət boş olmayan mətndir.
    Mətndəki rəqəm olan bütün simvolların cəmini qaytarır.
    """
    total = 0
    for char in s:
        try:
            val = int(char)
            total += val
        except:
            print("Çevrilə bilməyən simvol:", char)
    return total

print(sum_digits('a1b2c3'))