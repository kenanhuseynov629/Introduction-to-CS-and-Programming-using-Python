def apply(criteria, n):
    """
    criteria is a function that takes in a number and returns a Boolean
    n is an int
    Returns how many ints from 0 to n (inclusive) match the criteria
    """
    count = 0
    # 0-dan n-ə qədər bütün ədədləri daxil etmək üçün range(0, n + 1) yazırıq
    for i in range(0, n + 1):
        if criteria(i) == True: # criteria(i) Boolean qaytarır
            count += 1
            
    return count

def is_even(x):
    return x % 2 == 0

# 0-dan 10-a qədər cüt ədədlərin sayını tapır: 0, 2, 4, 6, 8, 10 (cəmi 6 ədəd)
print(apply(is_even, 10))  # 6 çap edir [103].

# Lambda (anonim funksiya) ilə tətbiqi:
# 0-dan 100-ə qədər ədədlərdən neçəsi 5-ə bərabərdir? (yalnız 1 ədəd: 5)
print(apply(lambda x: x == 5, 100))  # 1 çap edir [101].