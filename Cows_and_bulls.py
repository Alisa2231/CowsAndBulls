import random

print("Let's play Cows and Bulls game!")
print("Game rules:")
print("The computer will generate a random 4-digit number with no duplicate digits and you have to guess it.")
print("Each correct digit in your quess which is in the correct position means a bull.")
print("Each correct digit in your guess which is in the wrong position means a cow.")
print()
play = "y"

while play == "y":
    #generating a random 4-digits number with no duplicate digits

    first_digit = str(random.randint(0, 9))

    second_digit = str(random.randint(0, 9))
    while second_digit == first_digit:
        second_digit = str(random.randint(0, 9))

    third_digit = str(random.randint(0, 9))
    while third_digit == first_digit or third_digit == second_digit:
        third_digit = str(random.randint(0, 9))

    forth_digit = str(random.randint(0, 9))
    while forth_digit == first_digit or forth_digit == second_digit or forth_digit == third_digit:
        forth_digit = str(random.randint(0, 9))

    number = first_digit + second_digit + third_digit + forth_digit

    guess = input("Enter your first guess: ")
    attempts = 1

    while True:

        #checking the guess is a number

        try:
            guess_number = int(guess)
        except:
            print("The game works with numbers only!")
            guess = input("Please enter a 4-digit number: ")
            continue

        #making sure it has exactly 4 digits

        if len(guess) != 4:
            print("You entered an invalid number!")
            guess = input("Please enter a 4-digit number: ")
            continue

        #making sure there are no duplicate digits in the guess

        first_guessed_digit = guess[0]
        second_guessed_digit = guess[1]
        third_guessed_digit = guess[2]
        forth_guessed_digit = guess[3]

        error_message = ""

        if first_guessed_digit in [second_guessed_digit, third_guessed_digit, forth_guessed_digit] or \
            second_guessed_digit in [third_guessed_digit, forth_guessed_digit] or \
            third_guessed_digit == forth_guessed_digit:
            error_message = "The number you entered contains duplicate digits!"

        if error_message:
            print(error_message)
            guess = input("Enter a number with 4 different digits: ")
            continue

        #calculating the number of bulls and cows

        cows = 0
        bulls = 0
        i = 0

        for digit in guess:
            if digit in number:
                if digit == number[i]:
                    bulls += 1
                else:
                    cows += 1
            i += 1

        if bulls == 4:
            if attempts == 1:
                attempts_output = "attempt"
            else:
                attempts_output = "attempts"
            print(f"Congratulations, you guessed the number {number} in {attempts} {attempts_output}!")
            break

        if bulls == 1:
            bulls_output = "bull"
        else:
            bulls_output = "bulls"

        if cows == 1:
            cows_output = "cow"
        else:
            cows_output = "cows"

        print(f"Your guess {guess} has {bulls} {bulls_output} and {cows} {cows_output}.")
        attempts += 1
        guess = input(f"Enter your guess {attempts}: ")

    play = input("Wanna play again? y/n ")
    while play not in ["y", "n"]:
        play = input("Invalid input, please enter 'y' or 'n': ")
    if play == "n":
        print("Thank you for playing!")
        break
    print()