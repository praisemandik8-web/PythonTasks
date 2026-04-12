principal = 1000
rate = 0.7
year_one = 10
year_two = 20
year_three = 30

amount_one = principal * (1 + rate) ** year_one
print("after 10 years, amount on deposit is ", amount_one)

amount_two = principal * (1 + rate) ** year_two
print("after 20 years, amount on deposit is ", amount_two)

amount_three = principal * (1 + rate) ** year_three
print("after 30 years, amount on deposit is ", amount_three)
