# name : Willow Skagos
# class, period : CS30, period 2
# date created : Jan 27 2021
# description : RPG game.


# import the in game inventory
from in_game_inventory import *

# here is the in-game inventory
items = {'fists': {'description': 'The most basic weapon',
                   'health': '-2'
                   }
         }

# list of found items
found_items = []

# THE MENU DIRECTORIES

# food inventory
food_inventory = {
    'berries': {
                'description': 'A delicious, blue fruit',
                'health': '+2'
                },
    'fish': {
             'description': 'A meaty animal that came from the water',
             'health': '+5'
              },
    'water': {
              'description': 'drink',
              'health': '+2'
              },
    'apple': {
              'description': 'A red fruit',
              'health': '+6'
              }
    }


# weapons inventory
weapons_inventory = {
                      'sword': {
                                'description': 'A long sharp thing',
                                'health': '8'
                                },
                      'shank': {
                                'description': 'A really sharp stick',
                                'health': '5'
                                },
                      'fists': {
                                'description': 'The most basic weapon',
                                'health': '2'
                                },
                      'stick': {
                                'description': 'It is a long wooden '
                                'rod, it could be useful...',
                                'health': 'not applicable'
                                },
                      'tarp': {
                               'description': 'This would be great '
                               'for a shelter...',
                               'health': 'not applicable'
                               }
                      }


# dictionary of locations
locations = {
              'The river': {
                            'Type': 'Food',
                            'description': 'a place to find fresh food \
and water.'
                            },
              'The forest': {
                             'Type': 'Supply and Danger',
                             'description': 'a place to find \
supplies, but also where monsters creep.'
                             },
              'The clearing': {
                               'Type': 'Camp',
                               'description': 'a peaceful place to \
build camp, but watch out for nightfall...'
                               },
              'The mountains': {
                                'Type': 'Danger and Lookout',
                                'description': 'a great place to take \
in your surroundings, but beware of the sasquatch!'
                                },
              'The Bear Cave': {
                                'Type': 'Supply and Danger',
                                'description': 'They tend to collect \
useful things left behind by campers... but be careful not to wake \
them.'
                                }
              }


# dictionary of all entities
characters = {
              'Adult Bear': {
                             'strength': 6,
                             'speed': 6
                             },
              'Baby Bear': {
                            'strength': 1,
                            'speed': 1
                            },
              'Sasquatch': {
                            'strength': 8,
                            'speed': 3
                            },
              'Monster': {
                          'strength': 10,
                          'speed': 10
                          }
              }


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
    instructions = ("\nValid actions for current location:\nGo in \
the following direction:\n* south\nPerform one of these actions:\
\n* look around\n* fight\n* build\n* go fishing\n* eat\n* pick up\n\
* open inventory\n* quit game\n")
    while True:
        # print instructions and input statement
        print(instructions)
        north_menu = input(north_prompt)
        # go back south option
        if north_menu.lower() == 'south':
            print("\nGoing South!\n")
            open_simple_menu()
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
        # Quit the game, open menu
        elif north_menu.lower() == 'quit game':
            # ask if the user really wants to quit
            quit_game = input("\nAre you sure you want to quit? yes or no.\n")
            # the user quits, open menu
            if quit_game == 'yes':
                print("Quitting game.")
                directories()
            # do not quit game, continue game
            elif quit_game == 'no':
                continue
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
    instructions = ("\nValid actions for current location:\nGo in \
the following direction:\n* north\nPerform one of these actions:\
\n* look around\n* fight\n* build\n* go fishing\n* eat\n* pick up\n\
* open inventory\n* quit game\n")
    while True:
        # print instructions and input statement
        print(instructions)
        south_menu = input(south_prompt)
        # go back north option
        if south_menu.lower() == 'north':
            print("\nGoing North!\n")
            open_simple_menu()
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
        # Quit the game, open menu
        elif south_menu.lower() == 'quit game':
            # ask if the user really wants to quit
            quit_game = input("\nAre you sure you want to quit? yes or no.\n")
            # the user quits, open menu
            if quit_game == 'yes':
                print("Quitting game.")
                directories()
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
    instructions = ("\nValid actions for current location:\nGo in \
the following direction:\n* west\nPerform one of these actions:\
\n* look around\n* fight\n* build\n* go fishing\n* eat\n* pick up\n\
* open inventory\n* quit game\n")
    while True:
        # print instructions and input statement
        print(instructions)
        east_menu = input(east_prompt)
        # go back west option
        if east_menu.lower() == 'west':
            print("\nGoing West!\n")
            open_simple_menu()
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
        # Quit the game
        elif east_menu.lower() == 'quit game':
            # ask if the user really wants to quit
            quit_game = input("\nAre you sure you want to quit? yes or no.\n")
            # the user quits, open menu
            if quit_game == 'yes':
                print("Quitting game.")
                directories()
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
    instructions = ("\nValid actions for current location:\nGo in \
the following direction:\n* east\nPerform one of these actions:\
\n* look around\n* fight\n* build\n* go fishing\n* eat\n* pick up\n\
* open inventory\n* quit game\n")
    while True:
        # print instructions and input statement
        print(instructions)
        west_menu = input(west_prompt)
        # go back east option
        if west_menu.lower() == 'east':
            print("\nGoing East!\n")
            open_simple_menu()
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
            # You cannot open the menu
        elif west_menu.lower() == 'quit game':
            # ask if the user really wants to quit
            quit_game = input("\nAre you sure you want to quit? yes or no.\n")
            # the user quits, open menu
            if quit_game == 'yes':
                print("Quitting game.")
                directories()
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
def open_simple_menu():
    # Write a prompt for the user
    menu_prompt = ("\nWhat would you like to do?")
    # write instructions for the user on what actions they can perform
    instructions = ("\nValid actions for current location:\nGo in \
one of the following directions:\n* north\n* south\n* east\n\
* west\nPerform one of these actions:\n* look around\n* fight\n\
* build\n* go fishing\n* eat\n* pick up\n* open inventory\n\
* quit game\n")
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


# THE CODE AND FUNCTIONS FOR THE MAIN MENU DIRECTORY

# The code for exiting all directories
def exit_directory():
    """If the user types to exit, then exit the inventory."""
    exit_dir = ("\n When you are done here, type exit.\n")
    while True:
        ex_dir = input(exit_dir)
        if ex_dir.lower() == 'exit':
            directories()
        else:
            print("Sorry, I didn't understand that.")
            continue


# ALL CODE FOR INVENTORIES DIRECTORY

# make program that will run through either food or weapons inventory
# using interactive unput functions
def open_general_inventory():
    """Ask the user which type of inventory to open. food, tools
    and weapons, or both?"""
    # ask user which inventory to open
    print("\nYou have opened the inventory directory. Here is where \
you can find all of the possible collectible items in the game.")
    which_inventory = (" Which inventory would you like to open? Food, \
Tools and Weapons, or Both? If you would like to exit, type exit.\n")
    while True:
        inventory_open = input(which_inventory)

        # This will be the program to print each inventory
        def print_food_inventory():
            """Open the food inventory"""
            print(f"\n\t{item}:")
            description = f"description: {item_info['description']}"
            health = f"effect on health: {item_info['health']}"
            print(f"\t\t{description}\n\t\t{health}")

        # program to print each weapon
        def print_weapons_inventory():
            """Open the weapons inventory"""
            print(f"\n\t{item}:")
            description = f"description: {item_info['description']}"
            health = f"damage: {item_info['health']}"
            print(f"\t\t{description}\n\t\t{health}")

        # The program to exit each inventory and rerun open_general_inventory
        # in order to ask the user again which inventory to open
        def exit_inventory():
            """Exit the inventory and reenter the inventory directory where
            the user is asked which inventory to open."""
            exit = ("\nWhen you are done, type exit.\n")
            leave = (input(exit))
            if leave.lower() == 'exit':
                print()
                open_general_inventory()
            else:
                print("\nSorry I didn't understand that.")
                exit_inventory()

        # open the food inventory
        if inventory_open.lower() == 'food':
            print("\nYou opened your food inventory, these are it's \
    contents:")
            for item, item_info in food_inventory.items():
                # print the food inventory
                print_food_inventory()
            # tell how to exit the inventory
            exit_inventory()

        # open the weapons inventory
        elif inventory_open.lower() == 'tools and weapons':
            print("\nYou opened your tools and weapons inventory, these are \
    it's contents:")
            for item, item_info in weapons_inventory.items():
                # print the inventory
                print_weapons_inventory()
            # tell how to exit the inventory
            exit_inventory()

        # open both inventories at once
        elif inventory_open.lower() == 'both':
            print("\nYou opened both of your inventories, these are it's \
    contents:")
            # open weapons inventory
            print("\nYour tools and weapons include:")
            for item, item_info in weapons_inventory.items():
                # print the inventory
                print_weapons_inventory()
            # open food inventory
            print("\nYour foods include:")
            for item, item_info in food_inventory.items():
                # print the food inventory
                print_food_inventory()
            # tell how to exit the inventory
            exit_inventory()

        elif inventory_open.lower() == 'exit':
            directories()

        # for if the user types in an unrecognizeable command
        else:
            print("\nSorry I didnt understand that.\n")
            # rerun the whole inventory program
            continue


# ALL CODE FOR LOCATIONS DIRECTORY

# open the locations directory.
def open_locations():
    """Open the list that shows the user all of the locations and their
    properties."""
    print("You opened the locations directory, These are all of the \
possible locations and their information.\n")
    for location, location_info in locations.items():
        # description for the mountains
        if location == 'The mountains':
            print(f"{location} are a {location_info['Type']} tile. It is \
{location_info['description']}\n")
        # description for the bear cave
        elif location == 'The Bear Cave':
            print(f"{location} is a {location_info['Type']} tile. \
{location_info['description']}\n")
        # description for all locations other than mountains or bear cave
        else:
            print(f"{location} is a {location_info['Type']} tile. It is \
{location_info['description']}\n")

    # to exit locations
    exit_directory()


# ALL CODE FOR CHARACTERS DIRECTORY

# print the information on the characters in the game.
def characters_directory():
    """Opens the directory that shows the user all of the characters and
    their properties."""
    print("\nYou opened the character directory. These are all of the \
types of significant entities in the game and the information about \
them.\n")
    for character, character_info in characters.items():
        # print info about the Adult bear
        if character == 'Adult Bear':
            print(f"An {character} has a strength of \
{character_info['strength']} and a speed of {character_info['speed']}")
        # print info on all entities except the adult bear
        else:
            print(f"A {character} has a strength of \
{character_info['strength']} and a speed of {character_info['speed']}")
    # for exiting the directory
    exit_directory()


# ALL CODE FOR GENERAL DIRECTORIES DIRECTORY

# print an introduction to the directories
def directories():
    """Will ask the user whether they want to look at their inventories,
    the characters, or the locations."""
    which_directory = ("\nOpened the menu.\nWhich directory would you \
like to open? Inventories, Locations, or Characters?\nIf you would like \
to start the game, type 'start game'.")
    while True:
        directory = input(which_directory)
        # open inventories
        if directory.lower() == 'inventories':
            print("\n\n")
            open_general_inventory()
        # open locations
        elif directory.lower() == 'locations':
            print("\n\n")
            print()
            open_locations()
        # open characters
        elif directory.lower() == 'characters':
            print("\n\n")
            characters_directory()
        # return to actions
        elif directory.lower() == 'start game':
            print("\nStarting game...\n\nWelcome to the game!\n")
            open_simple_menu()
        # print input error
        else:
            print("\nSorry, I didn't understand that.")
            continue


# START THE GAME
print("Welcome to the game!\n")
open_simple_menu()
