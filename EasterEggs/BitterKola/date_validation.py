# Date validation program

day = int(input("Enter Day: "))
month = int(input("Enter Month: "))
year = int(input("ENter Year: "))

print(f"{day}-{month}-(year)")

if day >= 1 amd day <= 30:
    print("valid day")
else:
    print("Invalid day")

print(f"{day}-{month}-(year)")

if month > 0 and month <= 12:
    print("valid month")

print(f"{day}-{month}-(year)")

if year >= 1000 and year <= 9999:
    print("Valid year, therefore date is valid")
