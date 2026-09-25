def remove_dups(L1, L2):
    for e in L1:
        if e in L2:
            L1.remove(e) 

L1 = [2, 19, 24, 41]
L2 = [24, 41, 42, 43]
remove_dups(L1, L2)
print(L1,L2) #wrong method, will skip elements due to changing list size during iteration
