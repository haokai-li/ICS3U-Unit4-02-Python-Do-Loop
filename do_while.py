#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Sept 2021
# This Program calculate factorial with while loops


def main():
    # This function calculate factorial with while loops
    loop_number = 0
    answer_number = 1

    # input
    user_string = input("Please enter an positive integer: ")
    print("")

    # process
    try:
        user_number = int(user_string)
        while loop_number < user_number:
            loop_number = loop_number + 1
            answer_number = answer_number * loop_number
        # output
        print(
            "The factorial of all positive number from 1 to {0} is {1}".format(
                user_number, answer_number
            )
        )
    except Exception:
        # output
        print("{} is not a valid input.".format(user_string))

    print("\nDone.")


if __name__ == "__main__":
    main()
