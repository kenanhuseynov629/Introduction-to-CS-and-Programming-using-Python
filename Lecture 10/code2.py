def make_ordered_list(n):
    # n ədədini daxil etmək üçün range(n+1) yazırıq
    ordered_list = []
    for i in range(n+1):
        ordered_list.append(i)
    return ordered_list

print(make_ordered_list(5))