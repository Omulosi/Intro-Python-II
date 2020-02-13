from room import Room
from player import Player

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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("John", room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#

while True:
    print()
    print(f'Current room: ${player.current_room.name}')
    print(f'Description: ${player.current_room.description}')
    print(f'Items: ${player.display_room_items()}')
    print()

    user_resp = input('What do you want to do? (Press q to quit):  ')
    if user_resp == 'q':
        break
    if len(user_resp.split(' ')) == 1:
        while user_resp not in ('n', 's', 'e', 'w'):
            print('Invalid direction. Enter one of (n,s,e,w) ')
            user_resp = input('Please enter a room direction to move to (n,s,e,w): ')

        try:
            if user_resp == 'n':
                assert  player.current_room.n_to
                player.current_room = player.current_room.n_to
            elif user_resp == 's':
                assert  player.current_room.s_to
                player.current_room = player.current_room.s_to
            elif user_resp == 'e':
                assert  player.current_room.e_to
                player.current_room = player.current_room.e_to
            elif user_resp == 'w':
                assert  player.current_room.w_to
                player.current_room = player.current_room.w_to
        except AssertionError:
            print("Uh oh, you can't move there! Choose another direction")

    elif len(user_resp.split(' ')) == 2:
        action, item_name = user_resp.split(' ')
        if action not in ('get','take', 'drop'):
            print("I don't understand that command")
        else:
            if action in ('get', 'take'):
                player.take_item(item_name)
            if action in ('drop', ):
                player.drop_item(item_name)

    else:
        print('Invalid input')

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
