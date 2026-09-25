def remove_all(L, e):
    for elem in L:
        if elem == e:
            L.remove(e) 

Lin = [1,2,2,2]
remove_all(Lin, 2)
print(Lin) #wrong method, will skip elements due to changing list size during iteration