#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# A set is like a list that does not allow duplicated elements. If I print a and b, I will get an unordered list of the unique characters in each strings.

def main():
    a = set("We're gonna need a bigger boat.")
    b = set("I'm sorry, Dave. I'm afraid I can't do that.")
    # print_set(a)
    # print_set(b)
    # Will only show characters that are in set a and not in b.
    print_set(a - b)
    print_set(a | b)  # Will show all characters that are in one o both.
    # Exclusive or. This shows the ones that are in a or b but not both.
    print_set(a ^ b)
    print_set(a & b)  # Are in both


def print_set(o):
    print('{', end='')
    for x in o:
        print(x, end='')
    print('}')


if __name__ == '__main__':
    main()
