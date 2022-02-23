#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# LIST
def main():
    game = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    # print(game[2])  # Access to item index 3
    # print(game[1:5:3])  # Start, end and step
    # i = game.index("Paper") # Using index method to search for an item in the list
    # print(game[i])  # Printing if paper was found
    # game.append("Sheldon")  # Append the item at the end of the list
    # game.insert(4, "Leonard")  # Insert an item in a specific place using(index, inserted item)
    # game.remove("Paper") # Remove specified item
    # game.pop() # Removes last item from list
    # game.pop(2)  # Removes the item from index 2
    # del game[3] # Removes index 3
    # del game[1:3]  # Removes that range including start but excluding end index number
    # del game[0:5:2]  # Removes from list stepping by 2. En los index que cae los deja y todos los otros los guarda.
    # print(", ".join(game))
    # print(len(game)) #len is not an object method. It return the length of the specified list, tuple, word, etc.
    print_list(game)


def print_list(x):
    for i in x:
        print(i, end=' ', flush=True)
    print()


if __name__ == '__main__':
    main()
