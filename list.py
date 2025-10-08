def main():
    snacks = []
    while True:
        userin = input("Enter a snack or press Q to quit -> ").lower().strip()
        if userin == "q":
            break
        else:
            snacks.append(userin)
    print(snacks)
    for snack in snacks:
        print(snack)
    while True:
        try:
            userin = int(input("Enter an index to see a specific snack (99 to quit) -> "))
            if userin == 99:
                break
            else:
                print(snacks[userin])
        except ValueError:
            print("I said index dummy!")


if __name__ == "__main__":
    main()