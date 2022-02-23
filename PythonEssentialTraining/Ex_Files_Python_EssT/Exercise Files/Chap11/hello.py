#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# print(('Hello, World.').upper())
# print(('Hello, World.').swapcase())
# print(('Hello, World. {}').format(4 * 6))
# print(('''
# Hello,
# World. 

# {}
# ''').format(4 * 6))
# s = 'Hello, World. {}'
# print(s.format(4 * 10))

# # str is the original string class. 
# class MyString(str):
#     def __str__(self):
#         return self [::-1]\

# first = MyString("Hello")
# print(first)
# Strings are first class objects.

# METHODS
# A string is inmutable, it cannot change. When I change one, I'm creating a new object. 

# print(('Hello, World.').upper())
# print(('Hello, World.').lower())
# print(('Hello, World.').capitalize())
# print(('Hello, World.').title())
# print(('Hello, World.').swapcase())
# print(('Hello, World.').casefold()) # Similar to lower but more agressive.

# s1 = 'Hello '
# s2 = 'World'
# s3 = s1 + s2
# print(s3)

# FORMAT / I can do everything with the f formatting 
y = 21241
x = 42213
print('Hello, World. {} {}'.format(x, y)) # In some languages this is called string interpolation.
print('Hello, World. {0:<5} {1:+}'.format(x,y)) # To put a sign before or after. 
print('Hello, World. {:,} {:,}'.format(x,y)) # Thousand comma separator.
print('Hello, World. {:,} {:,}'.format(x, y).replace(',', '.'))  # Replace de comma with period.
print('Hello, World. {:.3f} {:f}'.format(x, y))  # Fixed number of decimal places. If I only put f it has a default value. 
# Fixed number of decimal places. If I only put f it has a default value.
print('Hello, World. {:,.3f} {:,f}'.format(x, y)) # Fixed decimal places with thousands comma separator
print('Hello, World. {:x} {:x}'.format(x,y)) # Transforms to hexadecimal
print('Hello, World. {:o} {:o}'.format(x, y))  # Transforms to octal
print('Hello, World. {:b} {:b}'.format(x, y))  # Transforms to binary
print(f'Hello, World. {x:,.3f} {y:b}')  # Example f formatting 







