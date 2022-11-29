#!/usr/bin/env python3

# Created by: Marcus Wehbi
# Created on: Nov 28 2022
# This program gets the users grade as a level,
# It then returns the middle percentage.


# This function uses a 'switch case' to
# Display the middle percentage
def calc_mark(level):
    # Use a switch case to display the middle percentage for each level
    match level:
        case "4+":
            print("Level {} has a middle percentage of 98%".format(level))
        case "4":
            print("Level {} has a middle percentage of 91%".format(level))
        case "4-":
            print("Level {} has a middle percentage of 83%".format(level))
        case "3+":
            print("Level {} has a middle percentage of 78%".format(level))
        case "3":
            print("Level {} has a middle percentage of 75%".format(level))
        case "3-":
            print("Level {} has a middle percentage of 71%".format(level))
        case "2+":
            print("Level {} has a middle percentage of 68%".format(level))
        case "2":
            print("Level {} has a middle percentage of 65%".format(level))
        case "2-":
            print("Level {} has a middle percentage of 61%".format(level))
        case "1+":
            print("Level {} has a middle percentage of 58%".format(level))
        case "1":
            print("Level {} has a middle percentage of 55%".format(level))
        case "1-":
            print("Level {} has a middle percentage of 51%".format(level))
        case _:
            print("Level {} is a -1 and has a middle percentage of 25%".format(level))


# this function gets the users input which is a grade level
# It then calls the percentage function to get the middle percentage
def main():

    # Get the users input (users grade level)
    level_user = input("Enter the level you want as a percentage: ")
    print("")
    # call the function to display the percent according to what level the user
    # inputs
    calc_mark(level_user)


if __name__ == "__main__":
    main()
