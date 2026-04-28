def compound_interest(balance, rate, years):
    interest = balance * (1+rate)**years
    return interest
print(compound_interest(100, 2, 5))
