#Start code here
a = int(input("Enter 1st number: ")) # your own code
b = int(input("Enter 2nd number: ")) # your own code
c = int(input("Enter 3rd number: ")) # your own code
if a >= b and a >= c:
  largest = a # your own code
elif b >= a and b >= c:
  largest = b # your own code
else:
  largest = c # your own code
if a <= b and a <= c:
  smallest = a # your own code
elif b <= a and b <= c:
  smallest = b # your own code
else:
  smallest = c # your own code
print("Largest:", largest) # your own code
print("Smallest:", smallest) # your own code
