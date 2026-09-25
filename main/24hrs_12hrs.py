
Time=input("Enter the time: ")
split=Time.split(":")

if int(split[0])<=12:
    split[0]=split[0]
elif int(split[0])>24:
    print("Dont play around")
    exit()
else:
    split[0]=int(split[0])-12

print(f'The time is {split[0]}:{split[1]}')