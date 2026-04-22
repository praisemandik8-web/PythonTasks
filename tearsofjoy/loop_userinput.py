#9. While loop with user input
#Keep asking the user to enter a positive number. Stop and print it when they #enter a number greater than 0.
#Expected output: Enter number: -3 / Enter number: 0 / Enter number: 5 / You #entered: 5

number = int(input("Enter number"))
while number > 0:
    
    print(f"you enterted: {number}")
    
    break
