import random

def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print("🎮 Welcome to 'Guess the Number' Game!")

    while True:
        play_game()

        while True:
            choice = input("\nDo you want to play again? Press 1 for Yes, 0 for No: ")
            if choice == '1':
                print("\nStarting a new game...\n")
                break
            elif choice == '0':
                print("Thanks for playing! Goodbye.")
                return
            else:
                print("Invalid choice. Please press 1 or 0.")
main()
