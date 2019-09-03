#making a function to display a fantasy game inventory

stuff = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total += 1
        print(str(v)+' '+str(k))
    print("Total number of items: "+str(item_total))
    
displayInventory(stuff)

#Write a function named addToInventory(inventory, addedItems),
    #where the inventory parameter is a dictionary representing
    #the player’s inventory (like in the previous project) and the addedItems parameter is a list like dragonLoot.
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] = inventory[item]+1
    return inventory
inv = {'gold coin':42, 'rope':1}
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
