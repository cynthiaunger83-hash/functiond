import random


def get_valid_input():
    # Ask repeatedly until valid input (validation uses != and and)
    user = input('Enter "r", "p", or "s": ').strip().lower()
    while user != "r" and user != "p" and user != "s":
        print("Invalid input")
        user = input('Enter "r", "p", or "s": ').strip().lower()
    return user


def convert_letter_to_word(letter): 
    if letter == "r":
        return "rock"
    elif letter == "p":
        return "paper"
    else: 
        return "scissors"
            

# Show round result
def round_results():
    if outcome == "won":
        print(f'You played "{user_word}", the computer played "{comp_word}" — you WON this round!')
    elif outcome == "lost":
        print(f'You played "{user_word}", the computer played "{comp_word}" — you LOST this round.')
    else:
        print(f'You played "{user_word}", the computer played "{comp_word}" — this round is a TIE.')

    for round_num in range(1, 6):  # 5 rounds
        print(f"\nROUND {round_num}")

user = get_valid_input()

        # Computer move
comp_moves = ["r", "p", "s"]
comp = random.choice(comp_moves)


def determine_outcome(user, comp): #write a function that returns the outcome
    if (user == "r" and comp == "s") or (user == "p" and comp == "r") or (user == "s" and comp == "p"):
        return "won"
        #user_wins += 1
    elif user == comp:
        return "tied"
        #ties += 1
    else:
        return "lost"
#comp_wins += 1
# Determine outcome (won/lost/tied)
       

# Convert letters to words (no dictionary)
user_word = convert_letter_to_word(user)
comp_word = convert_letter_to_word(comp)   


# Show round result
def round_results():
    if outcome == "won":
        print(f'You played "{user_word}", the computer played "{comp_word}" — you WON this round!')
    elif outcome == "lost":
        print(f'You played "{user_word}", the computer played "{comp_word}" — you LOST this round.')
    else:
        print(f'You played "{user_word}", the computer played "{comp_word}" — this round is a TIE.')



def main():
    print("Rock, Paper, Scissors — Best of 5")
    user_wins = 0
    comp_wins = 0
    ties = 0
    outcome = determine_outcome(user, comp)
    user_word = convert_letter_to_word(user)
    comp_word = convert_letter_to_word(comp) # Series summary
    print("\n=== SERIES RESULT ===")
    print(f"You won: {user_wins} round(s)")
    print(f"Computer won: {comp_wins} round(s)")
    print(f"Tied: {ties} round(s)")

    if user_wins > comp_wins:
        print("Series Winner: YOU")
    elif comp_wins > user_wins:
        print("Series Winner: COMPUTER")
    else:
        print("Series Result: TIE")


if __name__ == "__main__": 
    main() 