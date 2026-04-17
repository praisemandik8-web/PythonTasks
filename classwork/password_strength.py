#collect input from the user(password)
#analyze length by using the len keyword
#if length is < 8, print very week
# if length id = 8, print weak
#if length is between 8 and 16, print strong
#if password length is above 16, print very strong
password= input("Enter password")
#password = int (password)
password_length =  len (password)
if password_length < 8:
    print("very weak")
if password_length == 8:
    print(" weak")
if password_length > 8:
    print(" strong")

