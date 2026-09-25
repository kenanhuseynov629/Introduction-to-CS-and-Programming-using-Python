# Orijinal obyekt yaradılır
warm = ['red', 'yellow', 'orange'] 

# Alyas yaradılır (hot artıq warm ilə eyni obyekti göstərir)
hot = warm 

# hot vasitəsilə obyekti mutasiya edirik
hot.append('pink') 

print(hot)   # Ekrana çıxır: ['red', 'yellow', 'orange', 'pink'] [34]
print(warm)  # Ekrana çıxır: ['red', 'yellow', 'orange', 'pink'] [34]
# warm siyahısı da dəyişdi, çünki yaddaşda hər iki ad eyni obyekti göstərir! [29, 32]