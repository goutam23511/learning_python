import random
cmp=random.randint(1,100)
tries=0

while True:
    user=int(input("Guess the number(1-100): "))
    dis=abs(cmp-user)
    

    if dis == 0:
      tries+=1
      if tries == 1:
        print(f"Yes you got it in {tries} try")
      else:
        print(f"Yes you got it in {tries} tries")
      break

    elif dis<10:
        tries+=1
        print(f"You are extremely close!!HOT!!")

    elif dis<25>10:
        tries+=1
        print("Eh kinda close")

    else:
        print("COLD")