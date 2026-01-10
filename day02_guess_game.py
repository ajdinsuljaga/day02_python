import random

print("Welcome to Guess the number\n I'm thinking of a number between 1 and 100.")

#random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0 
guess = None 

while guess != secret_number:
    guess = int(input("Make a guess:"))
    attempts += 1

    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")

    else:
        print(f"Congratulations! You have gussed the number {secret_number} in {attempts} attempts")
