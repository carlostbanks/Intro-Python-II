# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def pick_up_item(self, item_name):
        for i in range(len(self.items)):
            if self.items[i].name == item_name:
                return self.items.pop(i)

        return None


