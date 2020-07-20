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

# Make a new player object that is currently in the 'outside' room.
player = Player('Jimmique', room['outside'])

# Write a loop that:

selection = None
while selection != 'q':
    current_room = player.current_room

# * Prints the current room name
print(current_room)
# * Waits for user input and decides what to do.
selection = input('\nSelect a cardinal direction: n, s, w, e, or q to quit \n')
# If the user enters a cardinal direction, attempt to move to the room there.
if selection in ['n', 's', 'w', 'e', 'q']:

    direction = f'{selection}_to'
    try:
        player.current_room = getattr(current_room, direction)
        print('\n')

# Print an error message if the movement isn't allowed.
    except AttributeError as a:
        print('\nNot able to move in that direction!\n')
else:
    print('\nPlease enter a valid selection\n')

# If the user enters "q", quit the game.
print("Thanks for playing!")
