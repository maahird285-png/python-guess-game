import random

def play_game():
    round_number = 1
    max_number = 100

    while True:
        secret_number = random.randint(1, max_number)
        attempts = 0
        max_attempts = 7

        print("\n==============================")
        print(f"Round {round_number}")
        print(f"Guess a number between 1 and {max_number}")
        print("You have 7 attempts!")
        print("==============================\n")

        while attempts < max_attempts:
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue  # does NOT use an attempt

            attempts += 1

            if guess < secret_number:
                print("Too low\n")
            elif guess > secret_number:
                print("Too high\n")
            else:
                print(f"Correct! 🎉 You guessed it in {attempts} attempts.")
                break
        else:
            print(f"\nGame Over ❌ The correct number was {secret_number}")

        again = input("\nDo you want to play again? (yes/no): ").lower()

        if again != "yes":
            print("Thanks for playing! 👋")
            break

        round_number += 1
        max_number += 50  # increase difficulty each round


play_game()