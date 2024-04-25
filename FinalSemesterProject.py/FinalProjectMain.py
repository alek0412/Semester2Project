from FinalProjectInventory import Inventory
from FinalProjectItem import Item
from datetime import date





# Stored items for our inventory in our main function
def main():
    inventory = Inventory()
    inventory.addItems(Item("001", "Apple", "Phone", 1000, date(2025, 5, 4), False))
    inventory.addItems(Item("002", "Apple", "Computer", 2000, date(2024, 7, 28), False))
    inventory.addItems(Item("003", "Samsung", "Phone", 900, date(2025, 8, 7), False))
    inventory.addItems(Item("004", "Google", "Phone", 500, date(2025, 2, 24), False))
    inventory.addItems(Item("005", "Google", "Computer", 700, date(2025, 4, 12), False))
    inventory.addItems(Item("006", "Microsoft", "Computer", 1300, date(2024, 7, 19), False))

    # We print all items to check their affiliations
    for item in inventory.items:
        print(f"Item ID: {item.itemID}, Manufacturer: {item.itemManufacturer}, Type: {item.itemType}, Price: ${item.itemPrice}, Service Date: {item.serviceDate}, Damaged: {item.damagedItems}")
        print()

    while True:
        inputUser = input("Enter the manufacturer and item type or 'q' to quit: ")
        if inputUser.lower() == 'q':
            break

        userWords = inputUser.split()
        manufacturer, itemType = extractManufacturerAndType(userWords)
        if manufacturer is None or itemType is None:

            print()
            print()
            print(f"Invalid input. Detected Manufacturer: {manufacturer}, Detected Item Type: {itemType}. Please try again.")
            print()
            print()

            continue
        
        itemsChosen = inventory.findItems(manufacturer, itemType)
        if itemsChosen:

            print()
            print()
            print(f"User Selection: ID Number - {itemsChosen.itemID}, Brand - {itemsChosen.itemManufacturer}, Product Type - {itemsChosen.itemType}, Price: ${itemsChosen.itemPrice}")
            print()

            similarItems = inventory.findSimilarItems(itemsChosen)
            if similarItems:

                print(f"You may also consider: ID Number - {similarItems.itemID}, Brand - {similarItems.itemManufacturer}, Product Type - {similarItems.itemType}, Price: ${similarItems.itemPrice}")
                print()
                print()
        else:
            print()
            print("No such item in inventory")


# We use this function to extract the words from the user to match with the stored items.
def extractManufacturerAndType(userWords):
    knownManufacturers = ['Apple', 'Samsung', 'Google', 'Microsoft']
    knownItemTypes = ['Computer', 'Phone']

    manufacturer = None
    itemType = None

    normalizedWords = [word.capitalize() for word in userWords]
    
    print()
    print()
    print(f"User Input: {normalizedWords}")


    for word in normalizedWords:
        if word in knownManufacturers and manufacturer is None:
            manufacturer = word
        elif word in knownItemTypes and itemType is None:
            itemType = word

    print(f"Selected manufacturer: {manufacturer}, Selected item: {itemType}")

    if manufacturer is None or itemType is None:
        return None, None
    return manufacturer, itemType

if __name__ == '__main__':
    main()
