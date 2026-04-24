# Final price calculation program

price = int(input("Enter price: "))
dis_percent = int(input("Enter discount percentage "))

dis_percent2 = dis_percent / 100.0
dis_amount = dis_percent2 * price
final_price = price - dis_amount

print("discount amount is $", dis_amount)
print("Final price is $", final_price)

