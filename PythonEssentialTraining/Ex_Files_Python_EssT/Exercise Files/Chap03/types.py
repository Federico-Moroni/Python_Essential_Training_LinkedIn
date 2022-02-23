#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

from decimal import *

x = True
print('x is {}'.format(x))
print(type(x))

x = ''' 
This 3 quotes allow me to write code
in different lines
'''

# Strings are objects.

print(x)

# I can swap them
j = "Seven {1} {0}".format(8, 9)
print(j)
print(type(j))

# I can put some space between them with :> (Left) or :< (Right)
z = "Seven '{1:<9}' '{0:>9}'".format(8, 9)
print(z)
print(type(z))

# I can also put leading ceros. It only works with ceros. Any other number will increment the spaces
z = "Seven '{1:<09}' '{0:>09}'".format(8, 9)
print(z)
print(type(z))

# If I feel in the ceros spaces with a bigger number. # This is great to set up an quantity of spaces for something.
z = "Seven '{1:<09}' '{0:>09}'".format(8, 9295198)
print(z)
print(type(z))

# Don't use floating numbers for money. As you can see, x should be equal to 0, but python sacrifices accuracy for precision. So, to solve this, we IMPORT decimal * [from decimal import *]
a = Decimal(".10")
b = Decimal(".30")
c = a + a + a - b
print(c)

# Boolean type. The value of None is False. Any empty string("") is False. The number 0 (cero) is False.
