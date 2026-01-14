import random
import os
from colorama import Fore, Style, init
init(autoreset=True)

def load_scores():
    if not os.path.exists("leaderboard.txt"):
        return []
    with open("leaderboard.txt", "r") as f:
        return [int(x.strip()) for x in f.readlines() if x.strip().isdigit()]

def save_score(score):
    scores = load_scores()
    scores.append(score)
    scores = sorted(scores)[:5]
    with open("leaderboard.txt", "w") as f:
        for s in scores:
            f.write(str(s) + "\n")

while True:
    print(Fore.CYAN + "\n=== GUESS THE NUMBER PRO ===")

    difficulty = input("Difficulty (easy / medium / hard): ").lower()
    if difficulty == "easy":
        max_num, max_attempts = 50, 10
    elif difficulty == "hard":
        max_num, max_attempts = 200, 5
    else:
        max_num, max_attempts = 100, 7

    secret = random.randint(1, max_num)
    guesses = []
    attempts = 0

    print(Fore.YELLOW + f"\nGuess 1 - {max_num}. Attempts: {max_attempts}")

    while attempts < max_attempts:
        try:
            g = int(input("Your guess: "))
        except:
            print(Fore.RED + "Invalid input!")
            continue

        if g in guesses:
            print(Fore.MAGENTA + "Already guessed!")
            continue

        guesses.append(g)
        attempts += 1

        if g < secret:
            print(Fore.BLUE + "Too low!")
        elif g > secret:
            print(Fore.RED + "Too high!")
        else:
            print(Fore.GREEN + f"\n🎉 YOU WON in {attempts} attempts!")
            save_score(attempts)
            break
    else:
        print(Fore.RED + f"\n💀 You lost! Number was {secret}")

    scores = load_scores()
    if scores:
        print(Fore.CYAN + "\n🏆 TOP 5 SCORES:")
        for i, s in enumerate(scores, 1):
            print(f"{i}. {s} attempts")

    if input("\nPlay again? (y/n): ").lower() != "y":
        print(Fore.YELLOW + "Goodbye!")
        break
