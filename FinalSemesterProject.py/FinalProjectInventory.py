from FinalProjectItem import Item
from datetime import date


class Inventory:

    #We initilize the inventory with a list of empty elements.
    def __init__(self):
        self.items = []

    #We add items to the inventory
    def addItems(self, item):
        self.items.append(item)


    
    # We find the most expensive item of the specified manufacturer and type.
    def findItems(self, itemManufacturer, itemType):
        validItems = [item for item in self.items if item.itemManufacturer == itemManufacturer and 
                       item.itemType == itemType and not item.damagedItems and item.serviceDate > date.today()]
        if not validItems:
            return None
        return max(validItems, key=lambda item: item.itemPrice)
    

    
    #We will find a similar item based on the specific item chosen
    def findSimilarItems(self, itemsChosen):
        similarItems = [item for item in self.items if item.itemType == itemsChosen.itemType and 
                         item.itemManufacturer != itemsChosen.itemManufacturer and not item.damagedItems and 
                         item.serviceDate > date.today()]
        if not similarItems:
            return None
        return min(similarItems, key=lambda item: abs(item.itemPrice - itemsChosen.itemPrice))
