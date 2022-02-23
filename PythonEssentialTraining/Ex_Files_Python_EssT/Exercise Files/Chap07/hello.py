#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

print('Hello, World.')

# Function1 is a wrapper for Function2. I cannot call Function2 because it only exists in the scope of Function1.. so I can do the following:


def f1(f):
    def f2():
        print("This is before the function call")
        f()
        print("This is after the function call")

    return f2

# x = f1()
# x()

# Decorator


@f1
def f3():
    print("This is f3")


f3()
