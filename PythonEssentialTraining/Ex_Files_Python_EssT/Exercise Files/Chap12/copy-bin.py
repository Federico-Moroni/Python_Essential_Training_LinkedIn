#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    infile = open('berlin.jpg', 'rb') # File type should be opened in binary for images.
    outfile = open('berlin-copy.jpg', 'wb')
    while True:
        buf = infile.read(10240) # 10240 is the size of the chunks that i'm reading and writing. Is a safe size for mobile if space is limited. We have to choose our buffer size carefully, considering the target enviroment for my code.  
        if buf:
            outfile.write(buf)
            print('.', end='', flush=True)
        else: break
    outfile.close()
    print('\ndone.')

if __name__ == '__main__': main()
