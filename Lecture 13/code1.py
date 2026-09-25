def sum_digits(s):
    """
    s rəqəmlərdən ibarət boş olmayan mətndir.
    Mətndəki rəqəm olan bütün simvolların cəmini qaytarır.
    """
    total = 0
    for char in s:
        if char in '0123456789':
            val = int(char)
            total += val
    return total

print(sum_digits('a1b2c3'))