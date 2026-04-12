principal = input("Enter the principal amount ")
principal = int(principal)

rate = input("Enter annual interest rate ")
rate = float(rate)
 
duration = input("Enter duration in years ")
duration = int(duration) 

duration2= duration *12
duration2 = int(duration2) 

rate2= rate/100/12
rate2= float(rate2)

r1= 1+rate2
r2= r1**duration2
r3= rate2 * r2
r4= r2 -1
r5= r3/r4
r6= principal * r5


print("Monthly payment is $",r6)
