# Valid pin checking program

pin = int(input("Enter 4 digit pin"))
if pin >= 1000 and pin <= 9999:
    print("valid pin")
else:
    print("invalid pin")
