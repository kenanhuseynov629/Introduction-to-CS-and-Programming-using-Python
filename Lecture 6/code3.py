cube = -27
neg = False

# Əgər ədəd mənfidirsə, işarəni müvəqqəti müsbət edib sonda qaytarırıq
if cube < 0:
    neg = True
    cube = abs(cube)

epsilon = 0.01
low = 0
high = cube
guess = (high + low) / 2.0

while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube:
        low = guess       # Təxmin çox kiçikdirsə, aşağı sərhədi qaldırırıq
    else:
        high = guess      # Təxmin çox böyükdürsə, yuxarı sərhədi endiririk
    guess = (high + low) / 2.0

# Əgər ilkin ədəd mənfi idisə, tapılmış kökü də mənfiyə çeviririk
if neg == True:
    guess = -guess

print(f'{guess} is close to the cube root of {cube}')