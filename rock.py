import random
while True:
    l=['rock','paper','scissor']
    computer=random.choice(l)
    human=None
    while human not in l:
        human=input('Enter your chioce : ')
        human=str.lower(human)
    if(computer==human):
        print('Computer choice:',computer)
        print('Human choice:',human)
        print('Match tie')
    elif(computer=="rock"):
        if(human=="paper"):
            print('Computer choice:',computer)
            print('Human choice:',human)
            print('Human wins')
        else:
            print('Computer choice:',computer)
            print('Human choice:',human)
            print('Computer wins')
    elif(computer=="paper"):
        if(human=="rock"):
            print('Computer choice:',computer)
            print('Human choice:',human)
            print('Computer wins')
        else:
            print('Computer choice:',computer)
            print('Human choice:',human)
            print('Human wins')
    elif(computer=="scissor"):
        if(human=="rock"):
            print('Computer choice:',computer)
            print('Human choice:',human)
            print('Human wins')
        else:
            print('Computer choice:',computer)
            print('Human choice:',human)
            print('Computer wins')
    choice=str.lower(input("Do you want to continue (Yes/No)?"))
    if(choice!="yes"):
            break
