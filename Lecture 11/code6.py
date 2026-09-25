def remove_dups(L1, L2):
    L1_copy = L1[:]  # Real klon yaradıldı! [37, 47, 48]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)

L1 = [2, 19, 24, 41]
L2 = [24, 41, 42, 43]
remove_dups(L1, L2)
print(L1,L2)     