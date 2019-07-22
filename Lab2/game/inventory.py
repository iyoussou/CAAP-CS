import scenes

class Inventory():

    storage = []

    def __init__(self, item):
        self.item = item

    def store_item(self):
        storage.append(self.item)

    def check_inventory(self):
        for i in range(len(storage)):
            print(storage[i])
