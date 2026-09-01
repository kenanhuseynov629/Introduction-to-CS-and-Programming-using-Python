# Bizdən elə bir funksiya yazmaq tələb olunur ki, 
# daxil edilmiş n tam ədədinin müsbət/mənfi epsilon 
# ətrafında kvadrat kökü olan neçə tam ədədin (integer) olduğunu tapsın

def bisection_root(x):
    """
    Assumes x > 0 and a float.
    Returns the approximate square root of x within epsilon.
    """
    epsilon = 0.01
    low = 0
    high = x
    ans = (high + low) / 2.0
    
    while abs(ans**2 - x) >= epsilon:
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
        
    return ans

def count_nums_with_sqrt_close_to(n, epsilon):
    """
    n is an int > 2
    epsilon is a positive number < 1
    Returns how many integers have a square root within epsilon of n
    """
    count = 0
    # i-nin yuxarı sərhəddini n**3 götürürük ki, hədəf aralığı tam əhatə edək
    for i in range(n**3):
        # bisection_root vasitəsilə hər i-nin kvadrat kökünü tapırıq
        approx_sqrt = bisection_root(i)
        
        # Əgər tapılan kök (n - epsilon) ilə (n + epsilon) arasındadırsa
        if (n - epsilon) < approx_sqrt < (n + epsilon):
            count += 1 # sayğacı 1 vahid artırırıq
            
    return count

print(count_nums_with_sqrt_close_to(10, 0.1))