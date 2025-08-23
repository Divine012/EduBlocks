#Start code here
s = input("Enter a string: ")
print("Length =", len(s)) # your own code
v = 0
c = 0
sp = 0
for ch in s.lower():
  if ch in "aeiou":
    v = v + 1
  elif ch == " ":
    sp = sp + 1
  elif ch.isalpha():
    c = c + 1
print("Vowels =", v, "Consonants =", c, "Spaces =", sp) # your own code
t = ""
for ch in s:
  if ch != " ":
    t = t + ch.lower() # your own code
rev = ""
for ch in t:
  rev = ch + rev
if t == rev:
  print("Palindrome")
else:
  print("Not Palindrome")
words = s.split()
print("Word count =", len(words)) # your own code
