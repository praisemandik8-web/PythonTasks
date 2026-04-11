seconds = input("Enter number of seconds ")
seconds = int(seconds)

hours = seconds//3600
rem_seconds1 = seconds % 3600

minutes = rem_seconds1 // 60

seconds2 = rem_seconds1// 60

print(hours, minutes, seconds2)
