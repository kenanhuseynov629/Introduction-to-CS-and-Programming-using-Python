def is_even_without_return(i):
    """
    Input: i, a positive int
    Does not return anything
    """
    print('without return')
    remainder = i % 2
    has_rem = (remainder == 0)
    print(has_rem)