#5. Repeat a greeting
#Ask the user for their name once, then print 'Hello, <name>!' five times using loop.
#Expected output (name = Adeola): Hello, Adeola! is printed 5 times
#collect name input from the user
#declare a variable "count" and assign 1 to it
#run a for loop to make the count variable loop 5 times
#print "hello" followed by the name variable

name = input("Enter name ")
count = 1
for count in range(1, 5):
    print(f"Hello, {name}!")
