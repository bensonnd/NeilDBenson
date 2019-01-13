stuff = {'rope': 1, 'torch': 1, 'gold coin': 42, 'dagger': 1, 'arrow': 12, 'bus': 1, 'tax': 100, 'rash': 2}

def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        item_total = item_total + v
        if v > 1 and (k[-1] in ['s', 'x'] or k[-2:] in ['ch', 'sh']): #pluralize keys greater than 1
            print(str(v) + ' ' + str(k) + 'es')
        elif v > 1:
            print(str(v) + ' ' + str(k) + 's')
        else:
            print(str(v) + ' ' + str(k))

    print('Total number of items: ' + str(item_total))

displayInventory(stuff)

dragonLoot = ['gold coin', 'dagger', 'torch', 'gold coin', 'ruby', 'rope', 'rope', 'rope', 'bus']

def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i,0) #if the item doesn't exist add to dict and set value to 0
        inventory[i] = inventory.get(i,0) + 1 #increment each item in dict by 1
    return inventory

stuff = addToInventory(stuff,dragonLoot)
displayInventory(stuff)