#!/usr/bin/env python
"""
Command line utility to add Roman numerals together.

"""

import sys
import argparse
import roman_add.src.roman_maths as rm


def main(in_args):
    out_num = rm.rom_add(in_args.numeral_a, in_args.numeral_b)
    print(out_num)

if __name__ == '__main__':
    # parse the user input
    parser = argparse.ArgumentParser(description="Add two Roman numerals\
    together.", epilog="The numbers must be positive, in all capitals, and in\
    the substractive Roman style (e.g. 4 is expressed IV instead of IIII). An\
    example input would be 'add_roman.py IV V'. The output would be 'IX'.")
    parser.add_argument("numeral_a", help="First Roman numeral to be added")
    parser.add_argument("numeral_b", help="Second Roman numeral to be added")

    user_input = sys.argv[1:]
    args = parser.parse_args(user_input)

    main(args)
