shoppingList = []

print("what should we pick up at the store")
print("enter 'DONE' to stop")

while True:
    newItem = input("> ")

    if newItem == 'DONE':
        break;
    else:
    shoppingList.append(newItem)

print("here it's your shopping list:")
for item in shoppingList:
    print(item)
