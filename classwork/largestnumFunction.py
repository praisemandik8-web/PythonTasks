def largestnum(number_one, number_two, number_three):
    largestnum = number_one
    if number_two > number_one:
        largestnum = number_two
        if number_three > number_two:
            largestnum = number_three
    return largestnum

print (largestnum(11, 10, 5))
