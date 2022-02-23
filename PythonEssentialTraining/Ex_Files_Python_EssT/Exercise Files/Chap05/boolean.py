#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# and, or, not, [in, not in] Collection [is, is not] Object

a = True
b = False
x = ('bear', 'bunny', 'tree', 'sky', 'rain')
y = 'bear'

if a and b:
    print('expression is true')
else:
    print('expression is false')

if "bear" in x:
    print("yes in")

if "bear" and "tree" in x:
    print("yes and")

if "run" not in x:
    print("Not")
