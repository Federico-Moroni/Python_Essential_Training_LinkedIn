#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# An instance of a class is called an object.

class Animal:
    def __init__(self, type, name, sound): # __init__ is a special name for a class function which operates like an initializer or constructor. 
        self._type = type # Object variables because they are never initialized until the object is defined. The _ is for discouriging the users to access the variables diretly.
        self._name = name
        self._sound = sound

    def type(self): 
        return self._type # This are called getters. They simply return the value of those object variables.

    def name(self):
        return self._name

    def sound(self):
        return self._sound


def print_animal(o):
    # isinstance(variable, data type) returns a boolean after checking if the variable is the data type we specified.
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print('The {} is named "{}" and says "{}".'.format( o.type(), o.name(), o.sound()))


def main():
    # One way to instantiate an object from the class animal
    a0 = Animal('kitten', 'fluffy', 'rwar')
    a1 = Animal('duck', 'donald', 'quack')
    print_animal(a0)
    print_animal(a1)
    # Another way to instantiate an object from the class animal
    print_animal(Animal('velociraptor', 'veronica', 'hello'))


if __name__ == '__main__':
    main()
