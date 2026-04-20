#collect input from user
#check for negative numbers
#use the for loop to iterate
#formula for calculating factorials
#print result
number = int(input("Enter number "))
if number < 0:
   print("Error")
else:
    factorial = 1
    for number1 in range(1, number + 1):
        factorial = factorial * number1

    print(f"The factorial of {number} is {factorial}")
  
