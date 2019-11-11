#!/user/bin/env python3

# Created by: Jaeyoon Lee
# Created on: Nov 2019
# This program print out the 0-9 multiplication tables


def main():
    # this function print out the 0-9 multiplication tables

    counter1 = 0
    counter2 = 0

    # process & output
    for counter1 in range(10):
        for counter2 in range(10):
            result = counter1 * counter2
            print("{0} x {1} = {2}".format(counter1, counter2 , result))


if __name__ == "__main__":
    main()
