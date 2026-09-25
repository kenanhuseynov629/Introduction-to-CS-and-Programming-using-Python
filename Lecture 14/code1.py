qiymetler = {'Elvin': 90, 'Leyla': 95, 'Murad': 88}

# 1. Bütün açarların siyahısını (iterable) almaq
butun_acarlar = qiymetler.keys()
# Nəticə: dict_keys(['Elvin', 'Leyla', 'Murad'])
print("Bütün açarlar:", list(butun_acarlar))

# 2. Bütün dəyərlərin siyahısını almaq
butun_deyerler = qiymetler.values()
# Nəticə: dict_values([90, 95, 88])
print("Bütün dəyərlər:", list(butun_deyerler))

# 3. Açar və dəyərləri tuple cütlüyü kimi dövrdə oxumaq
for acar, deyer in qiymetler.items():
    print(acar, "tələbəsinin qiyməti:", deyer)