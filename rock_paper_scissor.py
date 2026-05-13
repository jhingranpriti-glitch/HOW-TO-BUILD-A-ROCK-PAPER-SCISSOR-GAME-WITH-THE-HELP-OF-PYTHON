import random
choices=["rock","paper","scissors"]
print("Let's play rock paper and scissors")
user_choice=int(input('Type 0 if you want rock type 1 if you want paper or type 2 if you want scissors:  '))
if user_choice>=3 or user_choice<0:
    print("invalid number")
else:
    computer_choice=random.randint(0,2)
    print(f"your choice {choices[user_choice]} and computer choice {choices[computer_choice]}")
    if computer_choice==user_choice:
        print("Its a draw")
    elif computer_choice==0 and user_choice==1:
        print("YOU WIN")
    elif computer_choice==1 and user_choice==2:
        print("YOU WIN")
    elif computer_choice==2 and user_choice==0:
        print("YOU WIN")
    else:
        print("you lose")
