import random
items = ["rock","paper","scissor"]

computer = random.choice(items)

user = input("Rock Paper or Scissor: ").lower()

print("COMPUTER CHOOSES", computer)

if user == computer:
    print("Match Draw ........!")
    
elif user == "rock" and computer == "scissor":
    print("User Winnnnn!!!!!!!")
    
elif user == "paper" and computer == "rock":
    print("User Winnnnnn!!!!!!!!")
elif user == "scissor" and computer == "paper":
    print("User Winnnnnnn!!!!!!!!")
else:
    printf("Computer winnnnn!!!!!")
    
    