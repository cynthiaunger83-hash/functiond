import random
def main():
    print("welome to game")
    number = random.randint(0,100)
    guess = -1
    tries = 0
    while guess != number:
        guess = int(input("input a number 0-100 -> ")) 
        if guess > 100:
            print("invaild input- too high above guess range")
            guess = int(input("input a number 0-100 -> "))
        if guess < 0:
            print("invaild input- too low below range")
            guess = int(input("input a number 0-100 -> "))
        if guess > number:
            print(f"too high")
        if guess < number:
            print(f"too low")
        tries += 1
    print(f"you got it in {tries} tries!")
    print(f"the number was {number}")
    playagain = input("would you like to play again? yes or no -> ")
    if playagain == "yes":
        number = random.randint(0,100)
        main()
    if playagain == "no":
        print(f"have a good day")
        exit
if __name__ == "__main__":

    main()