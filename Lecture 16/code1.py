def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        s = fib_efficient(n - 1, d) + fib_efficient(n - 2, d)
        d[n] = s
        return s

# Baza halı lüğətdə reallaşdırılır:
d = {1: 1, 2: 1}
print(fib_efficient(34, d))  # Nəticə: 5702887