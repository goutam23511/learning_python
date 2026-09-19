import random 
choices=['rock','paper','scissors']
player=''
count=0

while player!="quit":
    player=input("choose(rock,paper,scissors,quit): ").lower()
    comp=random.choice(choices)

    if comp=='rock' and player=='scissors' or comp=='scissors' and player=='paper'or comp=='paper' and player=='rock':
        count-=1
        print(f'Sorry you lose. computer chose {comp}.You have {count} wins')

    elif player=="quit":
        print(f'Thanks for playing!')
        break 
    elif comp==player:
        print(f'AHH computer picked {comp} too')

    else:
        count+=1
        print(f'You win.computer chose {comp}.You have {count} wins')
        