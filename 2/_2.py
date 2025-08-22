#Start code here
while True:
  print("1.cm→m  2.m→cm  3.C→F  4.F→C  5.kg→g  6.g→kg  7.Exit") # your own code
  ch = int(input("Choice:- "))
  if ch == 1:
    print(float(input("cm:"))/100) # your own code
  elif ch == 2:
    print(float(input("m:"))*100) # your own code
  elif ch == 3:
    print((float(input("C:"))*9/5)+32) # your own code
  elif ch == 4:
    print((float(input("F:"))-32)*5/9) # your own code
  elif ch == 5:
    print(float(input("kg:"))*1000) # your own code
  elif ch == 6:
    print(float(input("g:"))/1000) # your own code
  elif ch == 7:
    break
  else:
    print("Invalid option")
