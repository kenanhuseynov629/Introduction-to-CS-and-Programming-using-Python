def mult_recur(a, b):
    if b == 1:
        return a
    else:
        return a + mult_recur(a, b - 1)

print(mult_recur(5, 4))  # Çıxış: 20

