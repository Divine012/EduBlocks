#Start code here
import random
N = int(input("Enter total rounds:- "))
target = N // 2 + 1
user_score = 0
comp_score = 0
choices = ["rock", "paper", "scissors"]
while user_score < target and comp_score < target:
  user = input("rock/paper/scissors: ").lower() # your own code
  comp = random.choice(choices) # your own code
  print("Computer chose:", comp) # your own code
  if user == comp:
    print("Draw")
  elif (user == "rock" and comp == "scissors") or (user == "paper" and comp == "rock") or (user == "scissors" and comp == "paper"):
    user_score += 1
    print("You win this round 🙌")
  else:
    comp_score += 1
    print("Computer wins this round 😂")
  print("Score -> You:", user_score, "Computer:", comp_score) # your own code
if user_score > comp_score:
  print("🎉 You Win the Game! PARADISE 😎")
else:
  print("💻 Computer Wins the Game!")
