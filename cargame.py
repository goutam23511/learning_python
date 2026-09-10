car="hi"
car_running=""

while car!="quit":
    car=input("> ").lower()
    if car=="help":            
        print('''
    start= start the car
    stop=stop teh car
    quit=exit the game''')

    elif car=="start":
        if car_running==True:
            print(f'CAR HAS ALREADY STARTED!!')
        else:
            print(f'car has started....ready to go!!')
            car_running=True

    elif car=='stop':
        if car_running==False:
            print(f'CAR HAS ALREADY STOPPED!!')
        else:
            print(f'car has STOPPED....ready to go!!')
            car_running=False
    elif car=="quit":
        break

    else:
        print("i dont understand")


    
