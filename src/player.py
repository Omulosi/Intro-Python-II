# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def display_room_items(self):
        self.current_room.display_items()

    def add_to_inventory(self, item):
        if not isinstance(item, Item):
            raise ValueError('Invalid type. Should be an item')
        self.inventory.append(item)

    def take_item(self, item_name):
            item_index = None
            for ind, item in enumerate(self.current_room.items):
                if item.name == item_name:
                    item_index = ind
            if item_index is None:
                print(f'${item_name} does not exist in ${self.current_room.name}')
                return
            item = self.current_room.items.pop(item_index)
            self.inventory.append(item)
            item.on_take()

    def drop_item(self, item_name):
            item_index = None
            for ind, item in enumerate(self.inventory):
                if item.name == item_name:
                    item_index = ind
            if item_index is None:
                print(f'${item_name} does not exist in ${self.name}\'s inventory')
                return
            item = self.inventory.pop(item_index)
            item.on_drop()
