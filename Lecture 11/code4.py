cool = ['blue', 'green', 'grey'] 

# cool siyahısının müstəqil klonu yaddaşda yaradılır
chill = cool[:] 

# chill siyahısına element əlavə edirik
chill.append('black') 

print(chill)  # Ekrana çıxır: ['blue', 'green', 'grey', 'black'] [13]
print(cool)   # Ekrana çıxır: ['blue', 'green', 'grey'] [13]
# Orijinal siyahı toxunulmaz qaldı! Çünki yaddaşda fərqli obyektlərdir [16, 36].
