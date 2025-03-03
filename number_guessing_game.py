import random

def number_guessing_game():
    print("Welcome to number guessing game")
    lower_bound = int(input("Enter the lower bound: "))
    upper_bound = int(input("Enter the upper bound: "))

    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess the number"))
            attempts+= 1

            if guess < lower_bound or guess > upper_bound:
                print(f"Please enter a number between {lower_bound} and {upper_bound}.")
            elif guess < secret_number:
                print(f"Too low! Try again")
            elif guess > secret_number:
                print(f"Too high! Try again")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")


if __name__ == "__main__":
    number_guessing_game()
                