#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Class is a definition and an object is an instance of a class.
class Duck:
    sound = "Quaaaack!"
    walking = "Walks like a duck"

    def quack(self):
        print(self.sound)

    def walk(self):
        print(self.walking)


def main():
    donald = Duck()  # donald is now an object of the class Duck
    donald.quack()
    donald.walk()


if __name__ == '__main__':
    main()
