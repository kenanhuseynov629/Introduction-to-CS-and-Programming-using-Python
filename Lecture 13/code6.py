def sum_digits_assert(s):
    """
    s - rəqəmlərdən ibarət BOŞ OLMAYAN mətndir.
    """
    assert len(s) != 0, "Mətn boşdur!"  # Giriş şərtini yoxlayırıq
    
    total = 0
    for char in s:
        try:
            val = int(char)
            total += val
        except:
            raise ValueError("Mətndə rəqəm olmayan simvol var!")
    return total

s = input("Mətndi daxil edin: ")
print(sum_digits_assert(s))