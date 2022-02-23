#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# If I don't pass enough arguments, this will throw an error.
def main():
    x = kitten(5, 6, 7)
    print(x)


def kitten(a, b, c):
    print('Meow.')
    print(a, b, c)
    return a, b, c


if __name__ == '__main__':
    main()

# If there is no return statement at the end of a function, the function returns NONE. Always RETURN something if you want to assign the output of one function to another variable outside of that function.
