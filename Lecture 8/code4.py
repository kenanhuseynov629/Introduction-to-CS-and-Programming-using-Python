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

print(bisection_root(36))