from random import randint


def guess_the_game():
    name = input("Hello! What is your name?\n")
    print()
    x = randint(1, 20)
    print("Well, KBTU, I am thinking of a number between 1 and 20.")
    guesses = 0
    while(True):
        num = int(input("Take a guess.\n"))
        print()
        guesses += 1
        if num == x:
            break
        elif num < x:
            print("Your guess is too low.")
        else:
            print("Your guess is too big.")
    print(f"Good job, KBTU! You guessed my number in {guesses} guesses!")

if __name__ == "__main__":
    guess_the_game()
