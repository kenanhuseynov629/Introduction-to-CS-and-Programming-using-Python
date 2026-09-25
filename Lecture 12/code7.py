def make_prod(a):
    def g(b):
        return a * b
    return g

print(make_prod(3)(4))  # Ekrana çıxır: 12

ikiyle_vuran = make_prod(2)  # ikiyle_vuran artıq 'g' funksiyasının alyasıdır
val = ikiyle_vuran(3)
print(val)  # Ekrana çıxır: 6