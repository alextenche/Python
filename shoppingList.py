
shoppingList = []

def showHelp():
    print("what should we pick up at the store")
    print("""
"enter 'DONE' to stop"
"enter 'HELP' to show help"
"enter 'SHOW' to display current list"
""")

def showList():
    print("here it's your shopping list:")
    for item in shoppingList:
        print(item)

def addToList(item):
    shoppingList.append(item)
    print("added {}, list now has {} items".format(newItem, len(shoppingList)))
    

showHelp();

while True:
    newItem = input("> ")

    if newItem == 'DONE':
        break;
    elif newItem == 'HELP':
        showHelp()
        continue
    elif newItem == 'SHOW':
        showList()
        continue

    addToList(newItem)


showList()
