stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    total_inventory = 0
    print('Inventory:')
    for item,amount in stuff.items():
        print(amount,item)
        total_inventory += amount
    print('Total number of items:',total_inventory)

if __name__ == "__main__":
    displayInventory(stuff)


'''
Assignment
You are creating a fantasy video game. The data structure to model the player's inventory will be a
dictionary where the keys are string values describing the item in the inventory and the value is an
integer value detailing how many of that item the player has. For example, the dictionary value

{'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

means the player has 1 rope, 6 torches, 42 gold coins, and so on.

Write a function named displayInventory() that would take any possible “inventory” and display it
like the following:

Desired Output
Inventory:
12 apple
42 gold coin
1 rope
6 torch
1 ring
Total number of items: 62
'''