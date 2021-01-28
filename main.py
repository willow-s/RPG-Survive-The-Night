# name : Willow Skagos
# class, period : CS30, period 2
# date created : Jan 27 2021
# description : RPG game.


# The code for exiting all directories
def exit_directory():
    exit_dir = ("\n When you are done here, type exit.\n")
    ex_dir = input(exit_dir)
    if ex_dir.lower() == 'exit':
        directories()
    else:
        print("Sorry, I didn't understand that.")
        exit_directory()


# ALL CODE FOR INVENTORIES DIRECTORY

# create food inventory
food_inventory = {
                'pizza': {
                        'description': 'A cheesy, consumable \
masterpiece',
                        'health': '+2'
                        },
                'pumpkin pie': {
                              'description': 'Pumpkin infused pastry',
                              'health': '+5'
                              },
                'banana': {
                          'description': 'A yellow fruit',
                          'health': '+2'
                          },
                'apple': {
                        'description': 'A red fruit',
                        'health': '+6'
                        }
                }
# make weapons inventory
weapons_inventory = {
                  'sword': {
                          'description': 'A long sharp thing',
                          'health': '2'
                          },
                  'grenade': {
                            'description': 'An explosive weapon',
                            'health': '8'
                            },
                  'katana': {
                            'description': 'A cooler sword',
                            'health': '5'
                            }
                  }


# make program that will run through either food or weapons inventory
# using interactive unput functions
def open_general_inventory():
    # ask user which inventory to open
    print("\nYou have opened the inventory directory.")
    which_inventory = (" Which inventory would you like to open? Food, \
Weapons, or Both? If you would like to exit, type exit.\n")
    inventory_open = input(which_inventory)

    # This will be the program to print each inventory
    def print_food_inventory():
        print(f"\n\t{item}:")
        description = f"description: {item_info['description']}"
        health = f"effect on health: {item_info['health']}"
        print(f"\t\t{description}\n\t\t{health}")

    # program to print each weapon
    def print_weapons_inventory():
        print(f"\n\t{item}:")
        description = f"description: {item_info['description']}"
        health = f"damage: {item_info['health']}"
        print(f"\t\t{description}\n\t\t{health}")

    # The program to exit each inventory and rerun open_general_inventory
    # in order to ask the user again which inventory to open
    def exit_inventory():
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
    elif inventory_open.lower() == 'weapons':
        print("\nYou opened your weapons inventory, these are it's \
contents:")
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
        print("\nYour weapons include:")
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
        open_general_inventory()


# ALL CODE FOR LOCATIONS DIRECTORY

# make the dictionary of locations
locations = {
            'The river': {
                        'Type': 'Food',
                        'description': 'a place to find fresh food and \
water.'
                        },
            'The forest': {
                          'Type': 'Supply and Danger',
                          'description': 'a place to find supplies, but \
also where monsters creep.'
                          },
            'The clearing': {
                            'Type': 'Camp',
                            'description': 'a peaceful place to build \
camp, but watch out for nightfall...'
                            },
            'The mountains': {
                            'Type': 'Danger and Lookout',
                            'description': 'a great place to take in \
your surroundings, but beware of the sasquatch!'
                            },
            'The Bear Cave': {
                            'Type': 'Supply and Danger',
                            'description': 'They tend to collect useful \
things left behind by campers... but be careful not to wake them.'
                            }
            }


# open the locations directory.
def open_locations():
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


# print the information on the characters in the game.
def characters_directory():
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
    which_directory = ("\nWhich directory would you like to open? \
Inventories, Locations, or Characters?\n")
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
    # print input error
    else:
        print("\nSorry, I didn't understand that.")
        directories()


# RUN THE PROGRAM
directories()
