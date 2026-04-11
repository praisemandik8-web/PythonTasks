 #Write a Python program that takes a mark (0-100) as input and
#prints the corresponding letter grade: A (90-100), B (80-89), C
#(70-79), D (60-69), F (below 60)

grade = input("Enter your grade chairman ")
grade = int (grade)

if grade >= 90 and grade <=100:
    print("chairman, your grade na A")

if grade >= 80 and grade <=89:
    print("Og, your grade na B")

if grade >= 70 and grade <=79:
    print("your grade na C")

if grade >= 60 and grade <=69:
    print("your grade na D")

if grade < 60:
    print("Senior man, na F you get!")



