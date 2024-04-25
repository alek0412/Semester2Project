
#We create a class where the ID, manufacturer, item type, price, service date and damaged items are stored for future use

class Item:
    def __init__(self, itemID, itemManufacturer, itemType, itemPrice, serviceDate, damagedItems):
        self.itemID = itemID
        self.itemManufacturer = itemManufacturer
        self.itemType = itemType
        self.itemPrice = itemPrice
        self.serviceDate = serviceDate
        self.damagedItems = damagedItems