x = 54321
epsilon = 0.01
num_guesses = 0

# Axtarış sahəsinin sərhədlərini təyin edirik
low = 0.0
high = x

# İlk təxmini aralığın tam ortası olaraq götürürük
guess = (high + low) / 2.0

# Hələ də epsilon aralığından kənardayıqsa, dövr davam edir
while abs(guess**2 - x) >= epsilon:
    num_guesses += 1
    
    # Əgər təxminin kvadratı x-dən kiçikdirsə, deməli təxmin çox kiçikdir
    if guess**2 < x:
        low = guess    # Aşağı sərhədi təxmin səviyyəsinə qaldırırıq
    # Əks halda təxmin çox böyükdür
    else:
        high = guess   # Yuxarı sərhədi təxmin səviyyəsinə endiririk
        
    # Yeni sərhədlərə əsasən yeni orta nöqtəni (təxmini) hesablayırıq
    guess = (high + low) / 2.0

print(f'num_guesses = {num_guesses}')
print(f'{guess} is close to square root of {x}')