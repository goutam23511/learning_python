
import random

print("<<<<<<<<<<WELCOME TO THE GUESSING GAME>>>>>>>>>>")
secret = random.randint(1, 5)
user_guess = 0
lives = 4

while lives > 0:
    user_guess = int(input("Guess the secret number (1-5): "))

    if user_guess == secret:
        print(f"You got it right in {4 - lives + 1} tries")
        break

    lives -= 1
    print(f"Wrong you have {lives * '❤ '}")

    if lives == 0:
        print("You lost try again 😢 ")
        print(f"The number was {secret}")
        break

