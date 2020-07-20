from room import Room
from player import Player
from item import Item
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [Item('Longsword', 'A very long sword')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item('Cookie', 'A delicious chocolate chip cookie')]),

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

#
# Main
#


def get_item(item_list, name):
    for item in item_list:
        try:
            item_name = getattr(item, 'name')
            if item_name == name:
                return item
        except AttributeError:
            return None


# Make a new player object that is currently in the 'outside' room.
player = Player('Jimmique', room['outside'])

# Write a loop that:

selection = None
while selection != 'q':
    current_room = player.current_room

# * Prints the current room name
print(current_room)
# * Waits for user input and decides what to do.
selection = input('''
     ****
     Select:\n
     A cardinal direction: 'n', 's', 'w', 'e' \n
     An item to get: 'get' or 'take' <item name> \n
     An item to drop: 'drop' <item name> \n
     or 'q' to quit \n
     ****
     ''')

selection_args = selection.split(' ')
command = selection_args[0]
item = None

if len(selection_args) > 1:
    item = selection_args[1]

# If the user enters "q", quit the game.
if command == 'q':
    print("Thanks for playing!")
# If the user enters a cardinal direction, attempt to move to the room there.
if selection in ['n', 's', 'w', 'e']:

    direction = f'{command}_to'
    try:
        player.current_room = getattr(current_room, direction)
        print('\n')

# Print an error message if the movement isn't allowed.
    except AttributeError:
        print('\n*****\nNot able to move in that direction!\n*****\n')
elif command in ['get', 'take'] and item is not None:
    wanted_item = get_item(current_room.items, item)

    if wanted_item is not None:
        current_room.items.remove(wanted_item)
        player.items.append(wanted_item)
        print(wanted_item.on_take())
    else:
        print('\n*****\n Item not available!\n*****\n')
elif command == 'drop' and item is not None:
    item_to_drop = get_item(player.items, item)

    if item_to_drop is not None:
        player.items.remove(item_to_drop)
        current_room.items.append(item_to_drop)
        print(item_to_drop.on_drop())
else:
    print('\n*****\nInvalid selection!\n*****\n')
