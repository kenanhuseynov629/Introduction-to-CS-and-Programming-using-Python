def remove_elem(L, e):
    """
    L is a list
    Returns a new list with elements in the same order as L but without any elements equal to e.
    """
    Lout = []                   # Yeni boş siyahı yaradırıq 
    for i in L:                 # L siyahısındakı hər bir elementi birbaşa oxuyuruq
        if i != e:              # Əgər element e-yə bərabər deyilsə 
            Lout.append(i)      # Onu yeni siyahımıza əlavə edirik 
    return Lout                 # Yeni yaranmış siyahını qaytarırıq 

print(remove_elem([1, 2, 3, 4, 5], 3))