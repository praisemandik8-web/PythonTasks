number1 = input("Enter number ")
number2 = input("Enter number ")
number3 = input("Enter number ")

number1 = int(number1)
number2 = int(number2)
number3 = int(number3)

sum_numbers= number1+number2+number3

print("sum is ", number1+number2+number3)
print("Average is ", (sum_numbers/3))
print("product is ", number1*number2*number3)

if number1 > number2 and number1> number3: 
    print(number1,"is greater than", number2,"and", number3)

if number2 > number1 and number2> number3: 
    print(number2,"is greater than", number1,"and", number3)

if number3 > number1 and number3> number2: 
    print(number3,"is greater than", number1,"and", number2)

if number1 < number2 and number1< number3: 
    print(number1,"is the smallest number")

if number2 < number1 and number2< number3: 
    print(number2,"is the smallest number")

if number3 < number1 and number3< number2: 
    print(number3, "is the smallest number")
