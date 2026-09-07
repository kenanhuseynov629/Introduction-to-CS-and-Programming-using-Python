def mean(*args):
    """
    Assumes at least one argument and all arguments are numbers.
    Returns the mean (ədədi orta) of the arguments.
    """
    tot = 0
    for a in args: # args artıq normal bir tuple-dır
        tot += a
    return tot / len(args)

# Fərqli sayda parametrlərlə çağırışlar:
print(mean(1, 2, 3, 4, 5, 6)) # 6 arqument -> 3.5 [47]
print(mean(6, 0, 9))          # 3 arqument -> 5.0 [47]