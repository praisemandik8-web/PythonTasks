#the code prints the symbol "<" if row ends with an odd number
#prints the symbol ">" if row ends with an odd number
for row in range(10):
    for column in range(10):
        print('<' if row % 2 == 1 else '>', end='')
    print()
