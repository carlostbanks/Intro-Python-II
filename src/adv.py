from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Add items to the rooms
room['overlook'].add_item(Item('flashlight'))
room['narrow'].add_item(Item('key'))
room['foyer'].add_item(Item('clock'))


#
# Main
#
def attempt_to_move(direction):
    if direction == "south":
        if player.current_room.s_to is None:
            print("Sorry there is no room to the South here")
        else: 
            player.current_room = player.current_room.s_to

    elif direction == "north":
        if player.current_room.n_to is None:
            print("Sorry there is no room to the North here")
        else: 
            player.current_room = player.current_room.n_to

    elif direction == "west":
        if player.current_room.w_to is None:
            print("Sorry there is no room to the West here")
        else: 
            player.current_room = player.current_room.w_to

    elif direction == "east":
        if player.current_room.e_to is None:
            print("Sorry there is no room to the East here")
        else: 
            player.current_room = player.current_room.e_to

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

print("Do you want to play a game?")
print("Press N, S, E, W to move around")
print("To quit, press Q or type 'quit'")

game_over = False
while not game_over:
    print(player.current_room.name)
    print(player.current_room.description)

    for item in player.current_room.items:
        print("In this room there is a", item.name)

    command = input("Which direction do you want to move?")

    if command in ['q', 'quit']:
        game_over = True

    elif command in ['s', 'south']:
        attempt_to_move("south")

    elif command in ['n', 'north']:
        attempt_to_move("north")

    elif command in ['e', 'east']:
        attempt_to_move("east")

    elif command in ['w', 'west']:
        attempt_to_move("west")

    elif command in ["i", "items"]:
        if len(player.items) == 0:
            print("You don't have any items silly")
        else:
            for item in player.items:
                print("You are holding the following:", item.name)

    elif command[0] in ['get', 'take']:
        item = player.current_room.pick_up_item(commands[1])

        if item == None:
            print(f"There is no {command[1]} in this room")
        else:
            player.items.append(item)
            item.take() 

    elif command[0] in ['drop']:
        player.drop_item(command[1])

    else: 
        print("I do not know what you entered")

print("Thanks for playing my game!")
