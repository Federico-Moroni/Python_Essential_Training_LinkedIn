#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Dictionaries {key: value} => key value pair. Keys must be inmutable.
def main():
    # animals = { kitten: meow, puppy: ruff!, lion: grrr, giraffe: I am a giraffe!, dragon: rawr }
    animals = dict(kitten='meow', puppy='ruff!', lion='grrr',
                   giraffe='I am a giraffe!', dragon='rawr')
    print_dict(animals)
    print(animals)
    print('lion' in animals)  # returns boolean
    print('found' if 'turtle' in animals else 'not found')  # CLAVE
    # If is not found, it will return NONE. I use this instead of print(animals['dog']) that would return an error.
    print(animals.get('dog'))


def print_dict(o):
    for k, v in o.items():
        print(f'{k}: {v}')
    for k in o.keys():
        print(k)
    for k in o.values():
        print(k)
    print(o['lion'])  # Returns only the value
    o['lion'] = 'I am a lion'  # Changes lion value
    o['monkey'] = 'haha'  # Adds new key value to the dictionary


if __name__ == '__main__':
    main()
