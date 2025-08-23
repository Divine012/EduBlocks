#Start code here
n = int(input("How Many Numbers? = "))
nums = []
for i in range(n):
  x = int(input("Enter Number:- "))
  nums.append(x) # your own code
avg = sum(nums) / len(nums) # your own code
mx = nums[0]
mn = nums[0]
for n in nums:
  if n > mx:
    mx = n # your own code
  if n < mn:
    mn = n # your own code
pos = neg = zer = 0 # your own code
for n in nums:
  if n > 0:
    pos += 1 # your own code
  elif n < 0:
    neg += 1 # your own code
  else:
    zer += 1 # your own code
print("Average =", avg) # your own code
print("Max =", mx) # your own code
print("Min =", mn) # your own code
print("Positives =", pos) # your own code
print("Negatives =", neg) # your own code
print("Zeros =", zer) # your own code
