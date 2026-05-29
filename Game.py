import random
item_list = [ " Rock ","Paper","Scissor"]

User_Choice = input("Enter Your Move: Rock, Paper , Scissor = ", )
Comp_Choice = random.choice(item_list)

print(f"Your Choice = { User_Choice }, Computer Choice = { Comp_Choice }")

if User_Choice == Comp_Choice :
    print("Tie")

elif User_Choice == "Rock":
    if Comp_Choice == "Paper":
        print("Computer Wins")
    else: 
        print("User Wins")
elif User_Choice == "Paper":
    if Comp_Choice == "Scissor":
        print("Computer Wins")
    else:
        print("User Wins")
elif User_Choice == "Scissor":
    if Comp_Choice == "Rock":
        print("Computer Wins")
    else:
        print("User Wins")