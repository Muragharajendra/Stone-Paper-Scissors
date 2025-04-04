import random
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice (s for Stone, p for Paper, z for Scissors): ").lower()

youDict = {"s": 1, "p": -1, "z": 0}
reverseDict = {1: "Stone", -1: "Paper", 0: "Scissors"}

you = youDict[youstr]

# Display choices
print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

# Determine winner
if computer == you:
    print("It's a draw!")

else:
    if (computer == -1 and you == 1): 
        print("You Lose!")

    elif (computer == -1 and you == 0):
        print("You Win!")

    elif (computer == 1 and you == -1):
        print("You Win!")

    elif (computer == 1 and you == 0):
        print("You Lose!")

    elif (computer == 0 and you == -1):
        print("You Lose!")

    elif (computer == 0 and you == 1):
        print("You Win!")

    else:
        print("Something went wrong!")
