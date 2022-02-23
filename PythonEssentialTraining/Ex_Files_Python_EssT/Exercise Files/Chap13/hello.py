#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class bunny:
    def __init__(self, n):
        self._n = n
    def __repr__(self): #It will print the value returned by the special __repr__ method. This prints a string although 47 is a number!
        return f'the number of bunnies is {self._n}'
    def __str__(self): # If I print() the object it will use this string version.
        return f'str:the number of bunnies is {self._n}' 


s = bunny(47)
print(s) #repr stands for representation. It will try to print the best possible string representation of a value. Uses __str__
print(repr(s)) # This will take the __repr__ version. This allow me to customize is going to be representated in different contexts. 

# If I dont have the __str__ it will print it with the __repr__ and if I don't have any, it will print that representation. 

print(ascii(s)) # Works just like repr(). It will escape any special character. If I put an emogi, it will escape it. The repr() will show the emogi. 
print(chr(128406)) # Character function prints the unicode position. 
print(ord(chr(128406))) # I get the number of the character.

#Look for built-in Functions /3/library/functions.html

