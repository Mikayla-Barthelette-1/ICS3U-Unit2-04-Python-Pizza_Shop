#!/usr/bin/env python3

# Created by: Mikayla Barthelette
# Created on: Sept 2021
# This program calculates the cost of a pizza

import constants


def main():
    # this function calculates the cost of a pizza

    # input
    diameter = int(input("Enter the diameter of your pizza (inch): "))

    # process
    sub_total = (
        constants.LABOR + constants.RENT + (diameter * constants.COST_PER_INCH)
    )
    total = sub_total + (sub_total * constants.HST)

    # output
    print("")
    print(
        "The cost for a(n) {0} inch pizza is: ${1:,.2f}".format(
            diameter, total
        )
    )
    print("\nDone.")


if __name__ == "__main__":
    main()
