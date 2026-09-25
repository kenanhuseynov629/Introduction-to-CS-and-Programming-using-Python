def remove_all(L, e):
    while e in L:
        L.remove(e) 

Lin = [1,2,2,2]
remove_all(Lin, 2)
print(Lin) #correct method, will remove all occurrences of e from L