import random

computer = random.choice(["s", "w", "g"])
you = input("Enter your choice: ")

print(f" you chose {you} and computer chose {computer}")

if(computer == you):
    print("Its a draw")
else:
    if(computer == 'w' and you == 's'): 
        print("You win!")

    elif(computer == 'w' and you == 'g'):
        print("You Lose!")

    elif(computer == 's' and you == 'w'):
        print("You lose!")

    elif(computer == 's' and you == 'g'):
        print("You Win!")

    elif(computer == 'g' and you == 'w'):
        print("You Win!")

    elif(computer == 'g' and you == 's'):
        print("You Lose!")

    else:
        print("Something went wrong!")
