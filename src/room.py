# Implement a class to hold room information. This should have name and
# description attributes.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return (f"Player Name: {self.name}, Current Room: {self.current_room}")
