def sum_odd(a, b):
    total = 0
    for i in range(a, b + 1):
        if i % 2 == 1:
            total += i
    return total

print(sum_odd(1, 10))