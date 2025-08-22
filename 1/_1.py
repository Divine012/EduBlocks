#Start code here
while True:
  print("\n1.+  2.-  3.*  4./  5.%  6.//  7.**  8.Exit")
  c = input("Choice:- ")
  if c == "8":
    break
  a = float(input("First :- "))
  b = float(input("Second :"))
  if c == "1":
    print("=",a+b) # your own code
  elif c == "2":
    print("=",a-b) # your own code
  elif c == "3":
    print("=",a*b) # your own code
  elif c == "4":
    print("=",a/b) # your own code
  elif c == "5":
    print("=",a%b) # your own code
  elif c == "6":
    print("=",a//b) # your own code
  elif c == "7":
    print("=",a**b) # your own code
  else:
      print("Invalid !!!")
