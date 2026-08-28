initial_deposit = float(input("Enter the initial deposit: "))
cost_of_dream_home = 800000
portion_down_payment = 0.25
down_payment_needed = cost_of_dream_home * portion_down_payment 
months_limit = 36
low = 0.0
high = 1.0
steps = 0
if initial_deposit >= down_payment_needed - 100:
    r = 0.0
    steps = 0
else:
    max_saved = initial_deposit * (1 + 1.0 / 12) ** months_limit
    if max_saved < down_payment_needed - 100:
        r = None
        steps = 0
    else:
        while True:
            steps += 1
            r = (low + high) / 2
            amount_saved = initial_deposit * (1 + r / 12) ** months_limit
            
            if abs(amount_saved - down_payment_needed) <= 100:
                break
            elif amount_saved > down_payment_needed:
                high = r
            else:
                low = r

print("Best savings rate:", r)
print("Steps in bisection search:", steps)