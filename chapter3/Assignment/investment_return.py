#prompt user to enter investment amount
#use a loop to run through year 1 to 30
#claculate percentage
#calculate investment return
#print investment return

investment_amount = int(input("Enter investment amount "))
for investment_amount in range(30):
    percentage = 0.07 * investment_amount
    investment_return = investment_amount + percentage
print("chairman, your returns after 30 years na  $", investment_return)
