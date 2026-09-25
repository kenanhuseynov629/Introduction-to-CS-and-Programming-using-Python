def bolme(a, b):
    # Proqramçı b-nin sıfır ola bilməyəcəyini təsdiqləyir
    assert b != 0, "Bölən sıfır ola bilməz!"
    return a / b

print(bolme(10, 2))  # 5.0
print(bolme(10, 0))  # AssertionError: Bölən sıfır ola bilməz!