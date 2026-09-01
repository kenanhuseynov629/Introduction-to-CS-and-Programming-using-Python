#Dəyişənə Mənimsədilmə Nümunəsi:

def is_even(i):
    return i % 2 == 0

my_func = is_even  # Mötərizə qoymuruq! Sadəcə obyekti mənimsədirik [77].
print(my_func(4))  # True çap olunacaq [74, 75].