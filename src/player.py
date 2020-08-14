# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, original_room):
        self.current_room = original_room

    def move_to(self, new_room):
        self.current_room = new_room
