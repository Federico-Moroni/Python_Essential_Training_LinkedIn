#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = '47'
y = int(x) #Transforms x string to int. This is the int constructor.
a = float(y)
b = abs(y) # Absolute
c = divmod(y, 3) # Returns a tuple. (cociente, remanente) Ej: divmod(10,3) ==> (3,1)
d = y + 73j
dcomp = complex(y, 73) # Complex function is a type constructor. j instead of i for imaginary part. 

print(f'x is {type(x)}')
print(f'x is {x}')
print(f'y is {type(y)}')
print(f'y is {y}')
print(a)
print(b)
print(c)
print(d, dcomp)