#snake water gun
import random 
CHOICE=["SNAKE","GUN","WATER"]
print("WELCOME TO THE 'SNAKE ,WATER AND GUN' GAME \n")
print("RULES AND INSTRUCTION :\n" \
"1. YOU WILL BE COMPETING WITH BOT\n " \
"2.IF YOU CHOOSE WATER AND THE OPPONENT CHOOSES SNAKE THEN , THE OPPONENT WIN \n" \
"3. IF YOU  CHOOSE GUN AND OPPONENT CHOOSES SNAKE THEN YOU WIN\n" \
"4.IF YOU CHOOSE WATER AND THE OPPONENT CHOOSES GUN , THEN YOU WIN \n" \
"5.IF BOTH CHOOSE SAME THING , IT WILL BE CONSIDERED A TIE [BOTH WILL GET +1 POINT]\n" \
"6.THE FINAL RESULT WILL BE BASED ON THE CUMULATIVE SCORES OF TEN ROUNDS \n  ")
print(" NOW , LET THE GAME BEGIN , PLAY SMARTLY ")
your_points=0
my_points=0
chances =10
no_ofchances =0

while (no_ofchances<chances):
    your_choice=input("ENTER YOUR CHOICE (UPPERCASE ACCEPTED ONLY)\n")
    print("YOUR ENTERED CHOICE :",your_choice)
    print("NOW OPPONENT'S TURN TO CHOOSE")
    random_choice=random.choice(CHOICE)
    print("OPPONENT CHOOSED:",random_choice)
    if your_choice=="SNAKE" and random_choice=="GUN":
        print("THE SNAKE WAS TAKEN DOWN BY THE GUN!!!YOU LOST")
        my_points=my_points+1
        print("your points:",your_points)
        print("bot points:",my_points)
        print("NO. OF ROUNDS LEFT:",9-no_ofchances)
        no_ofchances=no_ofchances+1
        continue
    elif your_choice==random_choice:
        print("OMG! IT'S A TIE")
        my_points=my_points+1
        your_points=your_points+1
        print("your points:",your_points)
        print("bot points:",my_points)
        print("NO. OF ROUNDS LEFT:",9-no_ofchances)
        no_ofchances=no_ofchances+1
        continue
    elif your_choice=="WATER" and random_choice=="GUN":
        print("WATER BLOCKS THE GUNSHOT ... YOU WON ")
        your_points=your_points+1
        print("your points:",your_points)
        print("bot points:",my_points)
        print("NO. OF ROUNDS LEFT:",9-no_ofchances)
        no_ofchances=no_ofchances+1
        continue
    elif your_choice=="SNAKE" and random_choice=="WATER":
        print("SNAKE WILL DRINK THE WATER... YOU WON ")
        your_points=your_points+1
        print("your points:",your_points)
        print("bot points:",my_points)
        print("NO. OF ROUNDS LEFT:",9-no_ofchances)
        no_ofchances=no_ofchances+1
        continue
    elif your_choice=="GUN" and random_choice=="WATER":
        print("WATER BLOCKS THE GUNSHOT ... YOU LOST ")
        my_points=my_points+1
        print("your points:",your_points)
        print("bot points:",my_points)
        print("NO. OF ROUNDS LEFT:",9-no_ofchances)
        no_ofchances=no_ofchances+1
        continue
    elif your_choice=="WATER" and random_choice=="SNAKE":
        print("SNAKE WILL DRINK THE WATER...YOU LOST")
        my_points=my_points+1
        print("your points:",your_points)
        print("bot points:",my_points)
        print("NO. OF ROUNDS LEFT:",9-no_ofchances)
        no_ofchances=no_ofchances+1
        continue 
    elif your_choice=="GUN" and random_choice=="SNAKE":
        print("THE SNAKE WAS TAKEN DOWN BY THE GUN!!YOU WON")
        your_points=your_points+1
        print("your points:",your_points)
        print("bot points:",my_points)
        print("NO. OF ROUNDS LEFT:",9-no_ofchances)
        no_ofchances=no_ofchances+1
        print(no_ofchances)
        continue

    else:
        print("ERROR FOUND!!TRY PUTTING INPUT IN CAPITAL LETTERS ")
        break
if my_points==your_points:
    print("TOUGH MATCH ... IT WAS A TIE")
if my_points<your_points:
    print("CONGRATS!! YOU'VE WON THE GAME ")
if my_points>your_points:
    print("IT WAS A NICE MATCH BUT I WON :)")            
if no_ofchances==chances:
    print("GAME COMPLETED")
    





