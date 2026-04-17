#write a statement that collectes input(purchase amount) from the user
#initialize input(purchase amount) as integer
#use the if statement to make a mathematical argument for purchases between 1000 and 10000
#use the if statement to make a mathematical argument for purchases between 10000 and 50000
#use the if statement to make a mathematical argument for purchases greater than 50000

purchase_amt = input("Enter purchase amount")
purchase_amt = int(purchase_amt)

if purchase_amt >= 1000 & purchase_amt <= 10000:
    discount = 0.05 * purchase_amt
    discount_calc = purchase_amt - discount
    print(discount_calc)

if purchase_amt > 10000 & purchase_amt <= 50000:
    discount = 0.1 * purchase_amt
    discount_calc = purchase_amt - discount
    print(discount_calc)

if purchase_amt > 50000:
    discount = 0.2 * purchase_amt
    discount_calc = purchase_amt - discount
    print("new amount after discount is removed is", discount_calc)
