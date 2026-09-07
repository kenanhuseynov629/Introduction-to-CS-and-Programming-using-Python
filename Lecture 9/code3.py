def quotient_and_remainder(x, y):
    q = x // y # Qismət
    r = x % y  # Qalıq
    return (q, r) 

# Unpacking (Gələn korteji dəyişənlərə paylamaq):
(quot, rem) = quotient_and_remainder(5, 2) 
print('quotient is:', quot)  # quotient is: 2 [43]
print('remainder is:', rem)  # remainder is: 1 [43]