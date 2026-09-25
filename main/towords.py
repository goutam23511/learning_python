words={
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine"
}

user=input("enter your number: ")
final=""

for i in user:
    final+=words.get(i)+" "
print(final)

