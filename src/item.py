class Item():

    def __init__(self, name):
        self.name = name

    def take(self):
        print("You picked up a", self.name)

    def drop(self):
        print("You just dropped a", self.name)