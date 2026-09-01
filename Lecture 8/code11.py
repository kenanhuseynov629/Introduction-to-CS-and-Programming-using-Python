def calc(op, x, y):
    return op(x, y)

def add(a, b):
    return a + b

def div(a, b):
    if b != 0:
        return a / b
    print("Denominator was 0.")

print(calc(div, 2, 0))