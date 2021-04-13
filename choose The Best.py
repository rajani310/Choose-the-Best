##### scissor paper and rock game 
import random
#create a list of play options.
mylist = ['scissor','paper','rock']
won = 0
loose = 0
drew = 0
def Refree(x_user,x_com):
    global won
    global loose 
    global drew 
    if x_user =='scissor'and x_com == "paper":
        won = won + 1
        return "Won."
    elif x_user == 'paper' and x_com == 'scissor':
        loose =loose + 1
        return 'Loose.'
    elif x_user == 'paper' and x_com == 'rock':
        won = won + 1
        return 'Won.'
    elif x_user == 'rock' and x_com == 'paper':
        loose = loose + 1
        return 'Loose.'
    elif x_user == 'rock' and x_com == 'scissor':
        won = won + 1
        return 'Win.'
    elif x_user == 'scissor' and x_com == 'rock':
        loose = loose + 1
        return 'Loose.'
    else:
        drew = drew + 1
        return "Drew"

while True:
    user= str(input('Choose S for Scissor ,Choose R  for Rock, Choose P for Paper: ')).lower()
    try: 
        user == "s"
        user="scissor"
    except:
         user == "p"
         user="paper"
    else:
        user="rock" 
    #Assign a random play to the computer
    computer=random.choice(mylist)
    print("You Choosed",user,'Against',computer)
    decision = Refree(user,computer)
    print('You',decision)
    #Create the game choice if continues then yes otherwise no
    game_choice = input("You want to continue? if Yes press Y else N : ").lower()
    if game_choice == "y":
        pass
    else:
        print("Won",won)
        print("Loose",loose)
        print("Drew",drew)
        break
    print("*"*90)