#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Duck:
    sound = 'Quack quack.'
    movement = 'Walks like a duck.'

    def quack(self):
        print(self.sound)

    def move(self):
        print(self.movement)


def main():
    donald = Duck()  # We instantiate the object from the class Duck
    donald.quack()  # We invoke the object method
    donald.move()


if __name__ == '__main__':
    main()