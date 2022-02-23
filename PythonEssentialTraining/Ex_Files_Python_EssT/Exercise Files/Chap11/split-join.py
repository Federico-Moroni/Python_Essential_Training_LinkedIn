#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

s = 'This is a long string with a bunch of words in it.'
# print(s.split()) # Split this to a list.
# print(s.split('i')) # Split every time it reachs to letter 'i'. It will removes it.
l = s.split()
s2 = ' '.join(l) # Join is a string method. It takes a list or tuple and creates a string. 
print(l, s2)