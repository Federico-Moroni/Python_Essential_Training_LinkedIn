#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    f = open('lines.txt', 'r') # The open function returns a file object. By default, it opens the function in read only mode. ('fileName', mode that can be: 'r = read','w = write','a = append', 'r+ = read and write' , 'b= binary', 't'= text)
    for line in f:
        print(line.rstrip()) # Strip any white space including new lines from the end of the line.

if __name__ == '__main__': main()
