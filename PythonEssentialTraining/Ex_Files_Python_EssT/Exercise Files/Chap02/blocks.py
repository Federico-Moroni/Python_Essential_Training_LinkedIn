#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 3
y = 2

if x < y:
    print(f'x < y: x is {x} and y is {y}')
print("y is < than x")

# Blocks do no define scope in python. Functions, objects, modules do.
w = True
s = 100
d = 500
if w == True:
    print(s)
else:
    print(d)
