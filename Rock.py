import random
options = ["Rock", "Paper" "Scissors"]
user_choice = input("Choose Rock,Paper, or Scissors: ")
computer_choice = random.choice(options)
print("You chose: ",user_choice)
print("computer chose: ",computer_choice)
if user_choice == computer_choice:
    print("It is a tie")
elif user_choice == "Rock" and computer_choice == "Scissors":
    print("Rock smashes Scissors! You Win")
elif user_choice == "Paper" and computer_choice == "Rock":
    print("Paper covers Rock! You Win")
elif user_choice == "Scissors" and computer_choice == "Paper":
    print("Scissors cut Paper! You Win")
else:
    print("You Lose! ")
