#Start code here
N = int(input("Enter N :- "))
a = 0
b = 1
s = 0
print("Fibonacci Series :-")
for i in range(N):
  print(a, end=" ") # your own code
  s += a
  a, b = b, a + b  # your own code
print("\nSum =", s) # your own code
