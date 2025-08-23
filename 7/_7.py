#Start code here
num = int(input("Enter number:- "))
s = 0
rev = 0
while num > 0 :
  d = num % 10
  s = s + d
  rev = rev * 10 + d
  num = num // 10
print("Sum of digits =", s) # your own code
print("Reversed number =", rev) # your own code
