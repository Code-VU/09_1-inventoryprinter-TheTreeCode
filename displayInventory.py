stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    print('Inventory:')
    totalinventory = 0
    for item in inventory:
        print(inventory[item], item)
        totalinventory += inventory[item]
    print('Total items: {totalinvetory}')


if __name__ == "__main__":
    displayInventory(stuff)

    # itemlookup = input('Which item would you like to check?: ')
    # result = inventory.get(itemlookup.lower(), 'Item not found!')
    # print('Inventory:\n'+str(result), itemlookup)

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