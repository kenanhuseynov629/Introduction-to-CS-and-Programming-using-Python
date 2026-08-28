x = 0.5
epsilon = 0.01
guess_count = 0

# x-in dəyərinə uyğun olaraq axtarış sərhədlərini tənzimləyirik
if x >= 1:
    low = 1.0     # Çünki x >= 1 olduqda kvadrat kök 1-dən kiçik ola bilməz
    high = x
else:
    low = x       # Kəsr ədədlər üçün kök ədədin özündən böyük, 1-dən kiçikdir
    high = 1.0

guess = (high + low) / 2.0

while abs(guess**2 - x) >= epsilon:
    if guess**2 < x:
        low = guess
    else:
        high = guess
    guess = (high + low) / 2.0
    guess_count += 1

print(f'{guess} is close to square root of {x}')
print(f'guess count = {guess_count}')