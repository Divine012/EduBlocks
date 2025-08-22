#Start code here
marks = []
for i in range(5):
  m = int(input("Enter mark (0-100): "))
  marks.append(m) # your own code
  total = sum(marks) # your own code
  avg = total / len(marks) # your own code
  if avg >= 90:
     grade = "A" # your own code
  elif avg >= 75:
     grade = "B" # your own code
  elif avg >= 60:
     grade = "C" # your own code
  elif avg >= 40:
     grade = "D" # your own code
  else:
     grade = "F" # your own code
  if min(marks) >= 40:
      result = "Pass" # your own code
  else:
      result = "Fail" # your own code
  print("Marks:", marks) # your own code
  print("Total:", total) # your own code
  print("Average:", avg) # your own code
  print("Grade:", grade) # your own code
  print("Result:", result) # your own code
