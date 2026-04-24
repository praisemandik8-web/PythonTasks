# Annual tax calculation program

salary = int(input("Enter monthly salary: "))

tax1 = 0.15 * salary
tax2 = 0.25 * salary

annual_tax1 = tax1 * 12
annual_tax2 = tax2 * 12

if salary <= 300000:
    print("No tax owed")
elif 300001 <= salary <= 600000:
    print("Annual tax owed is", annual_tax1)
else: 
    print("Annual tax owed is", annual_tax2)
