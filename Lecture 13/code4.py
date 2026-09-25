def sum_digits_raise(s):
    total = 0
    for char in s:
        try:
            val = int(char)
            total += val
        except:
            raise ValueError("Mətndə rəqəm olmayan simvol var!")
    return total


s = input("Mətndi daxil edin: ")
print(sum_digits_raise(s))