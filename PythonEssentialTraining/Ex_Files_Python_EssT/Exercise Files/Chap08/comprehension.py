#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# A list comprehension is a list created based on another list or iterator.

def main():
    from math import pi
    seq = range(11)
    seq2 = [x * 2 for x in seq]  # List comprehension
    seq3 = [x for x in seq if x % 3 != 0]
    seq4 = [(x, x**2) for x in seq]  # tuple
    seq5 = [round(pi, i) for i in seq]
    seq6 = {x: x**2 for x in seq}  # dict
    seq7 = {x for x in 'superduper' if x not in 'pd'}  # set
    print_list(seq)
    print_list(seq2)
    print_list(seq3)
    print_list(seq4)
    print_list(seq5)
    print(seq6)
    print_list(seq7)


def print_list(o):
    for x in o:
        print(x, end=' ')
    print()


if __name__ == '__main__':
    main()
