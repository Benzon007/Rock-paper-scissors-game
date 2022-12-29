
#Rock, Paper, Scissors

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

User = int(input("What do you chose? Type 0 for Rock, 1 for Paper, 2 for Scissors"))

game = [rock,paper,scissors]
print(game[User])
game1 = len(game)
Computer = random.randint(0,game1-1)
Computer1 = game[Computer]
print("Computer chose:\n",Computer1)
if User == 0 and Computer == 0:
  print("Retry")
elif User == 0 and Computer ==1:
  print("You lose")
elif User == 0 and Computer ==2:
  print("You won")
elif User == 1 and Computer ==0:
  print("You won")
elif User == 1 and Computer ==1:
  print("Retry")
elif User == 1 and Computer ==2:
  print("You lose")
elif User == 2 and Computer ==0:
  print("You lose")
elif User == 2 and Computer ==1:
  print("You won")
elif User == 2 and Computer ==2:
  print("Draw")