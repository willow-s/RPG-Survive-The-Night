# name : Willow Skagos
# class, period : CS30, period 2
# date created : Jan 27 2021
# description : RPG game.

# import the in game inventory
from in_game_inventory import *
# import the main menu of directories
from main_menu import directories
# import the maps
from map import *

# here is the in-game inventory
items = {'fists': {'description': 'The most basic weapon', 'health': '-2'}}

# list of found items
found_items = []


# ALL OF THE DIRECTIONS AND ACTIONS THE USER CAN CHOOSE TO TAKE
# THE INVENTORY IS ACCESSIBLE AT ANY TIME


# GO NORTH
# print a message to notify the user that the north input was valid
# run more options for actions
def north():
    """If the user types to go north, go north and then present more
    options for what actions the user can then perform"""
    # Write a prompt for the user
    north_prompt = ("\nWhat would you like to do?")
    # write instructions for the user on what actions they can perform
    instructions = ("\nYou are on the Mountains tile.\nValid actions \
for current location:\nGo in the following direction:\n* south\nPerform \
one of these actions:\n* look around\n* fight\n* build\n* go fishing\n\
* eat\n* pick up\n* open inventory\n* quit game\n* open map\n")
    while True:
        # print instructions and input statement
        print(instructions)
        north_menu = input(north_prompt)
        # go back south option
        if north_menu.lower() == 'south':
            print("\nGoing South!\n")
            return
        # look around action
        elif north_menu.lower() == 'look around':
            look_around()
        # fight action
        elif north_menu.lower() == 'fight':
            fight()
        # build action
        elif north_menu.lower() == 'build':
            build()
        # go fishing action
        elif north_menu.lower() == 'go fishing':
            go_fishing()
        # eat action
        elif north_menu.lower() == 'eat':
            eat()
        # pick up action
        elif north_menu.lower() == 'pick up':
            pick_up()
        # open the inventory
        elif north_menu.lower() == 'open inventory':
            if items == {}:
                print("\nYour inventory is empty.\n")
            # using a loop, print the in-game inventory
            for item, desc in items.items():
                print("\n\nOpened your inventory.\n")
                print(f"{item}:")
                print(f"\tdescription: {desc['description']}")
                print(f"\teffect on health: {desc['health']}\n")
        # open the map
        elif north_menu.lower() == 'open map':
            print_map()
            map_tile_types()
        # Quit the game, open menu
        elif north_menu.lower() == 'quit game':
            # ask if the user really wants to quit
            quit_game = input("\nAre you sure you want to quit? yes or no.\n")
            # the user quits, open menu
            if quit_game == 'yes':
                print("Quitting game.")
                directories()
                return
            elif quit_game == 'no':
                continue
            # do not quit game, continue game
            # input error
            else:
                print("Sorry I didn't understand that.")
        # input error
        else:
            print("\nInvalid action!\n")


# GO SOUTH
# print a message to notify the user that the south input was valid
def south():
    """If the user types to go south, go south and then present more
    options for what actions the user can then perform"""
    # Write a prompt for the user
    south_prompt = ("\nWhat would you like to do?")
    # write instructions for the user on what actions they can perform
    instructions = ("\nYou are on the Bear Cave tile.\nValid actions \
for current location:\nGo in the following direction:\n* north\nPerform \
one of these actions:\n* look around\n* fight\n* build\n* go fishing\n\
* eat\n* pick up\n* open inventory\n* quit game\n* open map\n")
    while True:
        # print instructions and input statement
        print(instructions)
        south_menu = input(south_prompt)
        # go back north option
        if south_menu.lower() == 'north':
            print("\nGoing North!\n")
            return
        # look around action
        elif south_menu.lower() == 'look around':
            look_around()
        # fight action
        elif south_menu.lower() == 'fight':
            fight()
        # build action
        elif south_menu.lower() == 'build':
            build()
        # go fishing action
        elif south_menu.lower() == 'go fishing':
            go_fishing()
        # eat action
        elif south_menu.lower() == 'eat':
            eat()
        # pick up action
        elif south_menu.lower() == 'pick up':
            pick_up()
        # open the inventory
        elif south_menu.lower() == 'open inventory':
            if items == {}:
                print("\nYour inventory is empty.\n")
            # using a loop, print the in-game inventory
            for item, desc in items.items():
                print("\n\nOpened your inventory.\n")
                print(f"{item}:")
                print(f"\tdescription: {desc['description']}")
                print(f"\teffect on health: {desc['health']}\n")
        # open the map
        elif south_menu.lower() == 'open map':
            print_map()
            map_tile_types()
        # Quit the game, open menu
        elif south_menu.lower() == 'quit game':
            # ask if the user really wants to quit
            quit_game = input("\nAre you sure you want to quit? yes or no.\n")
            # the user quits, open menu
            if quit_game == 'yes':
                print("Quitting game.")
                directories()
                return
            # do not quit game, continue game
            elif quit_game == 'no':
                continue
            # input error
            else:
                print("Sorry I didn't understand that.")
        # input error
        else:
            print("\nInvalid action!\n")


# GO EAST
# print a message to notify the user that the east input was valid
def east():
    """If the user types to go east, go east and then present more
    options for what actions the user can then perform"""
    # Write a prompt for the user
    east_prompt = ("\nWhat would you like to do?")
    # write instructions for the user on what actions they can perform
    instructions = ("\nYou are on the Forest tile.\nValid actions \
for current location:\nGo in the following direction:\n* west\nPerform \
one of these actions:\n* look around\n* fight\n* build\n* go fishing\n\
* eat\n* pick up\n* open inventory\n* quit game\n* open map\n")
    while True:
        # print instructions and input statement
        print(instructions)
        east_menu = input(east_prompt)
        # go back west option
        if east_menu.lower() == 'west':
            print("\nGoing West!\n")
            return
        # look around action
        elif east_menu.lower() == 'look around':
            look_around()
        # fight action
        elif east_menu.lower() == 'fight':
            fight()
        # build action
        elif east_menu.lower() == 'build':
            build()
        # go fishing action
        elif east_menu.lower() == 'go fishing':
            go_fishing()
        # eat action
        elif east_menu.lower() == 'eat':
            eat()
        # pick up action
        elif east_menu.lower() == 'pick up':
            pick_up()
        # open the inventory
        elif east_menu.lower() == 'open inventory':
            if items == {}:
                print("\nYour inventory is empty.\n")
            # using a loop, print the in-game inventory
            for item, desc in items.items():
                print("\n\nOpened your inventory.\n")
                print(f"{item}:")
                print(f"\tdescription: {desc['description']}")
                print(f"\teffect on health: {desc['health']}\n")
        # open the map
        elif east_menu.lower() == 'open map':
            print_map()
            map_tile_types()
        # Quit the game
        elif east_menu.lower() == 'quit game':
            # ask if the user really wants to quit
            quit_game = input("\nAre you sure you want to quit? yes or no.\n")
            # the user quits, open menu
            if quit_game == 'yes':
                print("Quitting game.")
                directories()
                return
            # do not quit game, continue game
            elif quit_game == 'no':
                continue
            # input error
            else:
                print("Sorry I didn't understand that.")
        # input error
        else:
            print("\nInvalid action!\n")


# GO WEST
# print a message to notify the user that the west input was valid
def west():
    """If the user types to go west, go west and then present more
    options for what actions the user can then perform"""
    # Write a prompt for the user
    west_prompt = ("\nWhat would you like to do?")
    # write instructions for the user on what actions they can perform
    instructions = ("\nYou are on the River tile.\nValid actions \
for current location:\nGo in the following direction:\n* east\nPerform \
one of these actions:\n* look around\n* fight\n* build\n* go fishing\n\
* eat\n* pick up\n* open inventory\n* quit game\n* open map\n")
    while True:
        # print instructions and input statement
        print(instructions)
        west_menu = input(west_prompt)
        # go back east option
        if west_menu.lower() == 'east':
            print("\nGoing East!\n")
            return
        # look around action
        elif west_menu.lower() == 'look around':
            look_around()
        # fight action
        elif west_menu.lower() == 'fight':
            fight()
        # build action
        elif west_menu.lower() == 'build':
            build()
        # go fishing action
        elif west_menu.lower() == 'go fishing':
            go_fishing()
        # eat action
        elif west_menu.lower() == 'eat':
            eat()
        # pick up action
        elif west_menu.lower() == 'pick up':
            pick_up()
        # open the inventory
        elif west_menu.lower() == 'open inventory':
            if items == {}:
                print("\nYour inventory is empty.\n")
            # using a loop, print the in-game inventory
            for item, desc in items.items():
                print("\n\nOpened your inventory.\n")
                print(f"{item}:")
                print(f"\tdescription: {desc['description']}")
                print(f"\teffect on health: {desc['health']}\n")
        # open the map
        elif west_menu.lower() == 'open map':
            print_map()
            map_tile_types()
        # quit game?
        elif west_menu.lower() == 'quit game':
            # ask if the user really wants to quit
            quit_game = input("\nAre you sure you want to quit? yes or no.\n")
            # the user quits, open menu
            if quit_game == 'yes':
                print("Quitting game.")
                directories()
                return
            # do not quit game, continue game
            elif quit_game == 'no':
                continue
            # input error
            else:
                print("Sorry I didn't understand that.")
        # input error
        else:
            print("\nInvalid action!\n")


# LOOK AROUND
# print a message to notify the user that the look around input was valid
def look_around():
    """Message the user so they know their input was valid"""
    print("\nLooking around!\n")


# FIGHT
# print a message to notify the user that the fight input was valid
def fight():
    """Message the user so they know their input was valid"""
    print("\nFight!\n")


# BUILD
# print a message to notify the user that the build input was valid
def build():
    """Message the user so they know their input was valid"""
    print("\nBuilding!\n")


# GO FISHING
# print a message to notify the user that the go fishing input was valid
def go_fishing():
    """Message the user so they know their input was valid"""
    print("\nGoing Fishing!\n")


# EAT
# print a message to notify the user that the eat input was valid
def eat():
    """Message the user so they know their input was valid"""
    print("\nEating!\n")


# PICK UP
# print a message to notify the user that the pick up input was valid
def pick_up():
    """Message the user so they know their input was valid"""
    print("\nPicking up!\n")


# OPEN THE CONTINUOUS ACTIONS MENU
# THIS WILL PRINT OUT A LIST OF ALL THE POSSIBLE ACTIONS IN THAT AREA
# THE USER CAN THEN TYPE WHAT ACTION TO TAKE

# Write a prompt for the user
menu_prompt = ("\nWhat would you like to do?")
# write instructions for the user on what actions they can perform
instructions = ("\nYou are on the clearing tile.\nValid actions for \
current location:\nGo in one of the following directions:\n* north\n\
* south\n* east\n* west\nPerform one of these actions:\n* look around\n\
* fight\n* build\n* go fishing\n* eat\n* pick up\n* open inventory\n\
* quit game\n* open map\n")
# loop that will ocntinue asking the user what action to perform
while True:
    print(instructions)
    menu = input(menu_prompt)
    # go north action
    if menu.lower() == 'north':
        print("\nGoing North!\n")
        north()
    # go south action
    elif menu.lower() == 'south':
        print("\nGoing South!\n")
        south()
    # go east action
    elif menu.lower() == 'east':
        print("\nGoing East!\n")
        east()
    # go west action
    elif menu.lower() == 'west':
        print("\nGoing West!\n")
        west()
    # look around action
    elif menu.lower() == 'look around':
        look_around()
    # fight action
    elif menu.lower() == 'fight':
        fight()
    # build action
    elif menu.lower() == 'build':
        build()
    # go fishing action
    elif menu.lower() == 'go fishing':
        go_fishing()
    # eat action
    elif menu.lower() == 'eat':
        eat()
    # pick up action
    elif menu.lower() == 'pick up':
        pick_up()
    # open inventory
    elif menu.lower() == 'open inventory':
        if items == {}:
            print("\nYour inventory is empty.\n")
            open_simple_menu()
        # using a loop, print the in-game inventory
        for item, desc in items.items():
            print("\n\nOpened your inventory.\n")
            print(f"{item}:")
            print(f"\tdescription: {desc['description']}")
            print(f"\teffect on health: {desc['health']}\n")
            open_simple_menu()
    # open the map
    elif menu.lower() == 'open map':
        print_map()
        map_tile_types()
    # quit the game
    elif menu.lower() == 'quit game':
        # ask if the user really wants to quit
        quit_game = input("\nAre you sure you want to quit? yes or no.\n")
        # the user quits, open menu
        if quit_game == 'yes':
            print("Quitting game.")
            directories()
        # the user does not quit, do not quit
        elif quit_game == 'no':
            open_simple_menu()
        # input error
        else:
            print("Sorry I didn't understand that.")
            open_simple_menu()
    # input error
    else:
        print("\nInvalid action!\n")
        continue
