#use a for loop to ask for inputs from the user and store them
#store the inputs, calculate and sisplay the sum, average, product, smallest and largest of those values.
sum = 0
product = 1


for numbers in range (4):
    numbers = int(input("Enter numbers "))
    sum += numbers
    average = sum/4
    product *= numbers
    

    smallest = numbers
    largest = numbers
    if numbers < smallest:
        smallest = numbers
    if numbers > largest:
        largest = numbers
    
print("sum of numbers is ", sum)
print("Average of numbers is ", average)
print("product is ", product)
print("smallest is ", smallest)
print("largest is ", largest)

