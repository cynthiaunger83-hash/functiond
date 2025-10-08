import random

"""Weclomes you to the game, also controls playing again"""
def main():
    print("welome to game")
    while True:
        play_game()
        playagain = input("Do you wanna play again? (yes/no): ")
        if playagain == 'yes':
            continue
        break

def random_number(min=0, max=100):
    """Decides the random number"""
    return random.choice(range(min, max+1))

def get_user_guess(min = 0, max = 100):
    """Gets the users guess"""
    while True:
        guess = int(input(f"input a number (between {min} and {max}): "))
        if min <= guess <= max:
            return guess
        elif guess < min or guess > max:
            print("Enter number within range.")
        else:
            print("invalid")
            continue

"""plays the game, determines winner"""
def play_game():
    target_number = random_number()
    attempts = 0
    while True:
        user_guess = get_user_guess()
        attempts += 1
        if user_guess < target_number:
            print("Guess Higher")
        elif user_guess > target_number:
            print("Guess Lower")
        else:
            print(f"You guessed the number {target_number} in {attempts} attempts!")
            break

    if __name__ == "__main__":
     main()

