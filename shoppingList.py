import os

shoppingList = []


def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")


def showHelp():
    clearScreen()
    print("what should we pick up at the store")
    print("""
"enter 'DONE' to stop"
"enter 'HELP' to show help"
"enter 'SHOW' to display current list"
"enter 'REMOVE' to delete an item from the list"
""")


def showList():
    clearScreen()
    print("here it's your shopping list:")

    for index, item in enumerate(shoppingList, start=1):
        print("{}. {}".format(index + 1, item))
    print("-" * 10)


def addToList(item):
    showList()
    if len(shoppingList):
        position = input("where should I add {}\n"
                         "press enter to add to the end of the list"
                         "> ".format(item))
    else:
        position = 0

    try:
        position = abs(int(position))
    except ValueError:
        position = None

    if position is not None:
        shoppingList.insert(position - 1, item)
    else:
        shoppingList.append(newItem)

    showList()

def removeFromList():
    showList()

    whatToRemove = input("what yould you like to remove ?\n>")

    try:
        shoppingList.remove(whatToRemove)
    except ValueError:
        pass

    showList()



showHelp()

while True:
    newItem = input("> ")

    if newItem.upper() == 'DONE' or newItem.upper() == 'QUIT':
        break
    elif newItem.upper() == 'HELP':
        showHelp()
        continue
    elif newItem.upper() == 'SHOW':
        showList()
        continue
    elif newItem.upper() == 'REMOVE':
        removeFromList()
        continue
    else:
        addToList(newItem)

showList()
