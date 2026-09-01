def is_triangular(n):
    """
    n is an int > 0
    Returns True if n is triangular, False otherwise
    """
    total = 0
    # n ədədinin özünü də daxil etmək üçün range(n + 1) yazırıq
    for i in range(1, n + 1):
        total += i
        if total == n:
            return True   # Şərt ödənən an funksiya dərhal True qaytarıb dayanır
        elif total > n:
            return False  # Əgər cəm n-i keçibsə, növbəti addımları yoxlamağa ehtiyac yoxdur
            
    return False

print(is_triangular(6))