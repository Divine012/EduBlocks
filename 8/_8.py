#Start code here
n = int(input("Enter Number:- "))
flag = True
if n < 2:
  flag = False
else:
  for i in range(2, n):
    if  n % i == 0:
      flag = False
      break
if flag:
  print(n, "is Prime") # your own code
else:
  print(n, "is Not Prime") # your own code
print("Primes up to", n, ":") # your own code
for num in range(2, n+1):
  prime = True # your own code
  for j in range(2, num):
    if num % j == 0:
      prime = False # your own code
      break
  if prime:
    print(num,) # your own code
