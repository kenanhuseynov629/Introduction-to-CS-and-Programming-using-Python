def char_counts(s):
    """
    s is a string of lowercase chars
    Returns a tuple where the first value is the number of vowels in s 
    and the second value is the number of consonants in s
    """
    vowels = "aeiou"
    v_count = 0
    c_count = 0
    
    # Doğrudan elementlər (simvollar) üzərində dövr (Pythonic yol)
    for char in s:
        if char in vowels:
            v_count += 1
        else:
            c_count += 1
            
    return (v_count, c_count) # Nəticə kortej olaraq qayıdır

print(char_counts('hello'))