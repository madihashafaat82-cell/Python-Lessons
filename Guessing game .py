import random

def play_game():
    print("🎮 Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("⚠ Please enter a number between 1 and 100.")
                continue

            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Correct! You guessed it in {attempts} attempts.")
                break

        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")

def main():
    while True:
        play_game()
        again = input("Do you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
