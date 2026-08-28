# Nyuton-Rafson düsturu
epsilon = 0.01
k = 24.0                # kvadrat kökü axtarılan ədəd
guess = k / 2.0         # ilkin təxmin olaraq ədədin yarısını götürürük
num_guesses = 0

while abs(guess*guess - k) >= epsilon:
    num_guesses += 1
    # Nyuton-Rafson düsturu ilə yeni daha dəqiq təxmin tapırıq
    guess = guess - (((guess**2) - k) / (2 * guess))

print(f'num_guesses = {num_guesses}')
print(f'Square root of {k} is about {guess}')