def sum_and_prod(L):
    """
    L is a list of numbers
    Return a tuple where the first value is the sum of all elements in L 
    and the second value is the product of all elements in L
    """
    # Hasil üçün ilkin dəyəri 1 götürürük, çünki 0-a vursaq sıfırlanar
    s_total = 0
    p_total = 1
    
    for e in L:
        s_total += e
        p_total *= e
        
    return (s_total, p_total) # Kortej olaraq qaytarırıq

# Test:
print(sum_and_prod([1, 2, 37, 51])) # Ekrana (10, 24) çap olunacaq [57]