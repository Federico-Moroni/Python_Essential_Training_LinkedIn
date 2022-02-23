#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# List. Mutable. [].
x = [1, 2, 3, 4, 5]
x[2] = 42
for i in x:
    print(f'i is {i}')

# Tuple. Inmutable. ().
z = (1, 2, 3, 4, 5)
# z[2] = 42 # This is not going to work and throw error "Tuple" object doen not support item assigment.
for s in z:
    print(f'i is {s}')

# Range. Inmutable. If I want to mutate an item from the range, I'll construct a list from the range output and then mutate the items.

n = range(10)  # starts from 0 and ends in 9.. so n-1.
for i in n:
    print(i)

h = range(10, 20)  # starts from 10 and ends in 20
for i in h:
    print(i)

# Dictionarie is a sercheable sequence of key : value pairs. Mutable.

d = {"one": 1, "two": 2, "three": 3}
d[2] = 12  # Will change the value.
for k, v in d.items():  # d.items() will return a 2 tuple with each of the items.
    print(f"Key: {k} Value: {v}")

#Type() and id()

x = (1, "two", 3, [4, "four"], 5)
y = (1, "two", 3, [4, "four"], 5)
print(f"x is {x}")
print(type(x[4]))
# Although they are the same tuples, their ID's are different because they are different OBJECTS.
print(id(x), id(y))
# Now, ID's are the same for the same items beacause their is only ONE literal number 1 object.
print(id(x[1]), id(y[1]))

if x is y:  # It compares if they are the same object.
    print("yes")
else:
    print("no")

# Function isinstance()

if isinstance(x, tuple):
    print("tuple")
elif isinstance(x, list):
    print("list")
else:
    print("no")
