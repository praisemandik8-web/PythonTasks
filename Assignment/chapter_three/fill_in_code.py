#use the first for loop to signify the number of rows needed
#use the second for loop statement to signify the number of columns needed
#use print statement to print thw @ symbols in 2 rows and 7 columns
#use the end satement to make sure it doesnt go to the next line after each row iteration
for row in range(2):
    for column in range(7):
        print('@', end='')
    print()
