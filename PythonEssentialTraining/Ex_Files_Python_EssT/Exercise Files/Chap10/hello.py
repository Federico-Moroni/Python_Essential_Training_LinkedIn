#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys # To use it en line 17 and get more info about an unexpected error.

def main():
    try: 
        # x = int('foo')
        x = float('sad')
    # except ValueError:
    #     print('Caught a value error')
    #     x = 5
    #     print(x)
    except ZeroDivisionError:
        print('Don\'t divide by 0') # Escape with the \
    except:
        print(f'Unknown error: {sys.exc_info()[1]}')
    else:
        print('Good job')

if __name__ == '__main__': main()
