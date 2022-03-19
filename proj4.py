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

#Write your code below this line 👇
import random

print("ROCK, PAPER, SCISSORS!")
print("\/---/----\/----/---\/")
print(" ")

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

while (player != 0) and (player != 1) and (player != 2):
  player = int(input("Pleae enter a valid option. Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer = random.randint(0, 2)

if player == 0:
  if computer == 0:
    print(rock)
    print(f"Computer chose:\n{rock}")
    print("Draw!")
  elif computer == 1:
    print(rock)
    print(f"Computer chose:\n{paper}")
    print("You Lose")
  else:
    print(rock)
    print(f"Computer chose:\n{scissors}")
    print("You Win!")
elif player == 1:
  if computer == 1:
    print(paper)
    print(f"Computer chose:\n{paper}")
    print("Draw!")
  elif computer == 2:
    print(paper)
    print(f"Computer chose:\n{scissors}")
    print("You Lose")
  else:
    print(paper)
    print(f"Computer chose:\n{rock}")
    print("You Win!")
else:
  if computer == 2:
    print(scissors)
    print(f"Computer chose:\n{scissors}")
    print("Draw!")
  elif computer == 0:
    print(scissors)
    print(f"Computer chose:\n{rock}")
    print("You Lose")
  else:
    print(scissors)
    print(f"Computer chose:\n{paper}")
    print("You Win!")
