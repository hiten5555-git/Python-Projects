import random
l=["rock","scissor","paper"]

"""
rock vs paper = paper wins
rock vs scissor = rock wins
paper vs scissor = scissor wins
"""

while True:
    ucount=0
    ccount=0
    a=int(input('''
                    Game start
                    1) Yes 
                    2) No | Exit
                    '''))
    if a==1:
        for i in range(1,6):
            user_input=int(input('''
                                    1) Rock
                                    2) Scissor
                                    3) Paper
                                    '''))
            if user_input==1:
                uc="rock"
            elif user_input==2:
                uc="scissor"
            elif user_input==3:
                uc="paper"

            cc=random.choice(l)
            if uc==cc:
                print("User Value",uc)
                print("Computer Value",cc)
                print("Game Draw")
                ucount+=0.5 
                ccount+=0.5
            elif (uc=="rock" and cc=="scissor") or (uc=="paper" and cc=="rock") or (uc=="scissor" and cc=="paper"):
                print("User Value",uc)
                print("Computer Value",cc)
                print("You Win")
                ucount+=1
            else:
                print("User Value",uc)
                print("Computer Value",cc)
                print("Computer Win")
                ccount+=1
        print()
        print()
        if ucount==ccount:
            print("Final Result Draw...")
            print("User Value",ucount)
            print("Computer Value",ccount)
        elif ucount>ccount:
            print("HURRAYYY..! You Win The Game")
            print("User Value",ucount)
            print("Computer Value",ccount)
        else:
            print("OH NO!! Computer Win")
            print("User Value",ucount)
            print("Computer Value",ccount)
                
                   
    else:
        break
