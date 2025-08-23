#Start code here
num = int(input("Enter Number:- "))
if num % 2 == 0:
  print("Even")
else:
  print("Odd")
if num % 3 == 0:
  print("Divisible by 3")
elif num % 5 == 0:
  print("Divisible by 5")
elif num % 7 == 0:
  print("Divisible by 7")
else:
  print("Not divisible by 3, 5, or 7")
