import random


def roll_dice(num_dice, num_sides):
    """Rolls the specified number of dice with the specified number of sides."""
    rolls = [random.randint(1, num_sides) for i in range(num_dice)]
    return rolls


def main():
    print("Welcome to Karina's Dice Roller!")

    while True:
        # Get inputs values from user
        num_dice = int(input("Enter the number of dice: "))
        num_sides = int(input("Enter the number of sides on the dice: "))

        # Roll the dice and display the results
        rolls = roll_dice(num_dice, num_sides)
        print("Rolls values:", rolls)

        # Ask the user if they want to roll again
        answer = input("Do you want to roll again? (y/n) ")
        if answer.lower() != 'y':
            break


if __name__ == "__main__":
    main()

"""
                Message for Later :
    Possible features to add on my Dice Roller Project :

        Allow the user to input their own roll values instead of generating them randomly
        Keep track of the user's roll history and display it
        Allow the user to save their roll history to a file
        Add a graphical user interface (GUI) to the program
"""
