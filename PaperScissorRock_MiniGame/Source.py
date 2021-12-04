import random
print("***Welcome To SCISSOR PAPER ROCK Game***")
t=1
Won=0
Lost=0
Draw=0
while(t<=5):
    user=input("Enter Your (P, S, R) : ")
    game=["Paper", "Scissor", "Rock"]
    choice=random.choice(game)
    comp=print("Computer Entry : ",choice)
    if user=="p":
        if choice== "Rock":
            print("You Won")
            Won=Won+1
        elif choice== "Scissor":
            print("You Lose")
            Lost=Lost+1
        else:
            print("Draw")
            Draw=Draw+1
    elif user=="s":
        if choice== "Rock":
            print("You Lose")
            Lost = Lost + 1
        elif choice== "Paper":
            print("You Won")
            Won = Won + 1
        else:
            print("Draw")
            Draw = Draw + 1
    elif user == "r":
        if choice == "Scissor":
            print("You Won")
            Lost = Lost + 1
        elif choice == "Paper":
            print("You Lose")
            Won = Won + 1
        else:
            print("Draw")
            Draw = Draw + 1
    else:
        print("Draw")
        Draw=Draw+1;
    t=t+1
print("\n")
print("Total Won:", Won , end="    ")
print("Total Lost:", Lost, end="    ")
print("Draw:", Draw)
input("Press Enter to close")