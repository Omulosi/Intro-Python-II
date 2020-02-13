# Implement a class to hold room information. This should have name and
# description attributes.

from item import Item

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def add_item(self, item):
        if not isinstance(item, Item):
            raise ValueError('Invalid type. Should be an item')
        self.items.append(item)

    def display_items(self):
        if not self.items:
            print('No items in this room to display')
        else:
            print([item for item in self.items])

