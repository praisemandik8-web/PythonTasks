#declare numbers variable
#declare squares variable = number multiplied by number 
#declare cubes variable = number * number * number
#use for loop to iterate from 0 to 5
#print result

for number in range(6):
    squares = number * number
    cubes = number * number * number
    print(number, squares , cubes)
