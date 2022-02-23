#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# This is a method of the string object itself, not of the print() function. The f means Format that would be written the following:

x = 2

y = "Hello, World. {}".format(x)

print("Hello, World. {}".format(x))

# This is the best
print(f'Hello, World. {x}')

print(y)
