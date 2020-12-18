#!/usr/bin/env python3

# Created by: Wenda Zhao
# Created on: Dec 2020
# This program for Weekly Assessment 05


def main():
    # this function for Weekly Assessment 05

    number_3 = 0
    number_5 = 0
    number = 0

    # process & output
    for number in range(1000):
        if number % 3 == 0:
            number_3 = number_3 + number
        elif number % 5 == 0:
            number_5 = number_5 + number
    print("The answer is {0}".format(number_3 + number_5))


if __name__ == "__main__":
    main()
