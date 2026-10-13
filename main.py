import random

def number_guessing_game():
    
    target_number = random.randint(1, 100)
    attempts = 0

    
    print("      WELCOME TO THE NUMBER GUESSING GAME      ")
    print("=" * 40)
    print(f"I am thinking of a number between 1 and 100.")
    print("Can you guess what it is?\n")

    while True:
        user_input = input("Enter your guess: ")

        # Validate that the input is an integer
        if not user_input.isdigit():
            print("Invalid input! Please enter a valid whole number.\n")
            continue

        guess = int(user_input)
        attempts += 1

        # Check bounds
        if guess < 1 or guess > 100:
            print(f"Out of bounds! Please guess a number between 1 and 100.\n")
            continue

        # Core logic
        if guess < target_number:
            print("Too low! Try a higher number.\n")
        elif guess > target_number:
            print("Too high! Try a lower number.\n")
        else:
            print("=" * 40)
            print(f"🎉 Congratulations! You guessed the number {target_number}!")
            print(f"It took you {attempts} attempt(s).")
            print("=" * 40)
            break

if __name__ == "__main__":
    number_guessing_game()