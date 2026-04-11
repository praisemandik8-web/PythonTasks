principal = input("Enter principal ")
principal = int(principal)

rate = input("Enter rate in percentage")
rate = int(rate)
rate_two= rate/100

time = input("Enter time in years")
time = int(time)

simple_interest = (principal * rate_two * time)/100
total_amt =  principal + simple_interest

print ("Simple interest is", simple_interest)
print("total amount is", total_amt) 


