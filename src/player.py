# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, original_room):
        self.current_room = original_room
        self.items = []

    def move_to(self, new_room):
        self.current_room = new_room

    def drop_item(self, item_name):
        for i in range(len(self.items)):
            if self.items[i].name == item_name:
                item = self.items.pop()
                item.drop()
                self.current_room.add_item(item)
        print(f"{item_name} does not exist in this room!")
