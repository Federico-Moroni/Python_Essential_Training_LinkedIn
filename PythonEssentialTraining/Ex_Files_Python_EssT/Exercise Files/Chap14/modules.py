#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys
import os
import random
import datetime

def main():
    # v = sys.version_info # Python version
    # p = sys.platform 
    # s = os.name # Operating system name
    # d = os.getenv('PATH')
    # e = os.getcwd() #Current working directory
    # f = os.urandom(25) # random number 25 bytes long. Return a byte object.
    # fhex = f.hex()
    # print('Python version {}.{}.{}'.format(*v))
    # print(p)
    # print(s)
    # print(d)
    # print(e)
    # print(f)
    # print(fhex)

    # x = random.randint(1, 1000)
    # print(x)
    # y = list(range(25))
    # print(y)
    # random.shuffle(y)
    # print(y)

    now = datetime.datetime.now()
    print(now)
    print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)


if __name__ == '__main__': main()
