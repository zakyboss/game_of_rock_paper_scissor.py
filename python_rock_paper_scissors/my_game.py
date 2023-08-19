import sys
import random
player_choice=input("Please Select Number\n 1 For Rock\n 2 For Paper \n 3 For Scissors \n: ")
player=int(player_choice)

computer_choice=random.choice("123")
if player<1|player>3:
    sys.exit("Please Select from 123")
computer=int(computer_choice)
print('you Chose'+" "+(player_choice))
print("Python Chose"+" "+(computer_choice))
print("")
print("")
if player==1 and computer==3:
    print("🎉 You Win")
elif player==2 and computer==1:
    print("🎉 You Win")
elif player==3 and computer==2:
    print("🎉 You Win")
elif player==computer:
    print("🤭 A Tie")
else:
    print("😔 Python Wins")


