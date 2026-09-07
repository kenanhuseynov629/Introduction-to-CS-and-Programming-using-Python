def list_sum(*L):
    total = 0
    for e in L: # e dəyişəni növbə ilə siyahıdakı hər bir ədədi götürür
        total += e
    return total # [55]

print(list_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))