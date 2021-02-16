# import the in game inventory
from in_game_inventory import *
# import the maps
from map import *
# import everything about characters
from characters import *
# import the mountains
from the_mountains import *
# import the bear cave
from the_bear_cave import *
# import randint from random
from random import randint
# import the endings
from endings import *
# import time
import time as t
# import the night time
from night_time import *
# import the player_health and hours_left
import player_health as ph


# create a list of defeated enemies
defeated_enemies = []

# ask the user if they would like to pick up an item
pick_up_item_prompt = ("Would you like to pick it up?")


# ALL OF THE DIRECTIONS AND ACTIONS THE USER CAN CHOOSE TO TAKE
# THE INVENTORY IS ACCESSIBLE AT ANY TIME


# GO NORTH
# print a message to notify the user that the north input was valid
# run more options for actions
def north():
    """If the user types to go north, go north and then present more
    options for what actions the user can then perform"""
    # Write a prompt for the user
    north_prompt = ("\nWhat would you like to do? ")
    # write instructions for the user on what actions they can perform
    instructions = (f"\n{mountains_tile}\nValid actions for current \
location:\nGo in the following direction:\n* south\nPerform one of \
these actions:\n* look around\n* eat\n* open inventory\n* quit game \
\n* open map\n")
    if 'sasquatch' not in defeated_enemies:
            sasquatch_attack()
            defeated_enemies.append('sasquatch')
    while True:
        t.sleep(1)
        # print instructions and input statement
        print(instructions)
        north_menu = input(north_prompt)
        # go back south option
        if north_menu.lower() == 'south':
            t.sleep(1)
            print("\nGoing South!\n")
            ph.hours_left -= 1
            if ph.hours_left == 7:
                clearing_night()
            t.sleep(1)
            return
        # look around action
        elif north_menu.lower() == 'look around':
            t.sleep(1)
            look_around()
            if 'sword' not in items:
                t.sleep(1)
                print(sword_item)
                pick_up_item = input(pick_up_item_prompt)
                if pick_up_item == 'yes':
                    t.sleep(1)
                    pick_up()
                    add_sword()
                else:
                    t.sleep(1)
                    print("\nSorry. I don't understand.")
                    continue
        # eat action
        elif north_menu.lower() == 'eat':
            eat()
        # open the inventory
        elif north_menu.lower() == 'open inventory':
            t.sleep(1)
            # using a loop, print the in-game inventory
            print("\n\nOpened your inventory.\n")
            for item, desc in items.items():
                t.sleep(1)
                print(f"{item}:")
                print(f"\tdescription: {desc['description']}")
                print(f"\teffect on health: {desc['health']}\n")
        # open the map
        elif north_menu.lower() == 'open map':
            t.sleep(1)
            print_map()
            map_tile_types()
        # Quit the game, open menu
        elif north_menu.lower() == 'quit game':
            t.sleep(1)
            # ask if the user really wants to quit
            quit_game = input("\nAre you sure you want to quit? yes or no.\n")
            # the user quits, open menu
            if quit_game == 'yes':
                t.sleep(1)
                print("Quitting game.")
                exit("Program has been terminated")
                return
            elif quit_game == 'no':
                continue
            # do not quit game, continue game
            # input error
            else:
                t.sleep(1)
                print("Sorry I didn't understand that.")
        # input error
        else:
            t.sleep(1)
            print("\nInvalid action!\n")


# GO SOUTH
# print a message to notify the user that the south input was valid
def south():
    """If the user types to go south, go south and then present more
    options for what actions the user can then perform"""
    # Write a prompt for the user
    print("You enter the cave and see a VERY large bear laying in "
          "front of you, sleeping... hopefully...\nThere is another,"
          " much smaller, a baby, bear laying next to the large one. "
          "Standing on your tippy toes, you look around the bears and"
          " see a giant pile of STUFF, some of which might be useful "
          "to you.")
    south_prompt = ("\nWhat would you like to do? ")
    # write instructions for the user on what actions they can perform
    instructions = (f"\n{bear_cave_tile}\nValid actions \
for current location:\nGo in the following direction:\n* north\n\
Perform one of these actions:\n* sneak past bears\n* eat\n* open \
inventory\n* quit game\n* open map\n")
    while True:
        t.sleep(1)
        # print instructions and input statement
        print(instructions)
        south_menu = input(south_prompt)
        # go back north option
        if south_menu.lower() == 'north':
            t.sleep(1)
            print("\nGoing North!\n")
            ph.hours_left -= 1
            if ph.hours_left == 7:
                clearing_night()
            t.sleep(1)
            return
        # eat action
        elif south_menu.lower() == 'sneak past bears':
            t.sleep(1)
            bear_cave()
        elif south_menu.lower() == 'eat':
            t.sleep(1)
            eat()
        # open the inventory
        elif south_menu.lower() == 'open inventory':
            t.sleep(1)
            # using a loop, print the in-game inventory
            print("\n\nOpened your inventory.\n")
            for item, desc in items.items():
                t.sleep(1)
                print(f"{item}:")
                print(f"\tdescription: {desc['description']}")
                print(f"\teffect on health: {desc['health']}\n")
        # open the map
        elif south_menu.lower() == 'open map':
            t.sleep(1)
            print_map()
            map_tile_types()
        # Quit the game, open menu
        elif south_menu.lower() == 'quit game':
            t.sleep(1)
            # ask if the user really wants to quit
            quit_game = input("\nAre you sure you want to quit? yes or no.\n")
            # the user quits, open menu
            if quit_game == 'yes':
                t.sleep(1)
                print("\nQuitting game.")
                exit("Program has been terminated")
                return
            # do not quit game, continue game
            elif quit_game == 'no':
                continue
            # input error
            else:
                t.sleep(1)
                print("\nSorry I didn't understand that.")
        # input error
        else:
            t.sleep(1)
            print("\nInvalid action!\n")


# GO EAST
# print a message to notify the user that the east input was valid
def east():
    """If the user types to go east, go east and then present more
    options for what actions the user can then perform"""
    # Write a prompt for the user
    east_prompt = ("\nWhat would you like to do? ")
    # write instructions for the user on what actions they can perform
    instructions = (f"\n{river_tile}\nValid actions \
for current location:\nGo in the following direction:\n* west\n\
Perform one of these actions:\n* look around\n* go fishing\n* eat\n\
* collect water\n* open inventory\n* quit game\n* open map\n")
    while True:
        t.sleep(1)
        # print instructions and input statement
        print(instructions)
        east_menu = input(east_prompt)
        # go back west option
        if east_menu.lower() == 'west':
            t.sleep(1)
            print("\nGoing West!\n")
            ph.hours_left -= 1
            if ph.hours_left == 7:
                clearing_night()
            t.sleep(1)
            return
        # look around action
        elif east_menu.lower() == 'look around':
            t.sleep(1)
            look_around()
            if 'berries' not in items:
                t.sleep(1)
                print(berries_item)
                pick_up_item = input(pick_up_item_prompt)
                if pick_up_item == 'yes':
                    t.sleep(1)
                    pick_up()
                    add_berries()
                elif pick_up_item == 'no':
                    t.sleep(1)
                    print("\nokay...")
                    continue
                else:
                    t.sleep(1)
                    print("\nSorry. I don't understand.")
                    continue
        # collect water action
        elif east_menu.lower() == 'collect water':
            # add water to inventory
            if 'water' not in items:
                print("\nCollecting water!")
                add_water()
            elif 'water' in items:
                print("\nYou cannot put more water in your inventory.")
                continue
        # go fishing action
        elif east_menu.lower() == 'go fishing':
            # Add fish to inventory
            if 'fish' not in items:
                n = randint(1, 2)
                if n == 1:
                    t.sleep(1)
                    go_fishing()
                    t.sleep(1)
                    print(fish_item)
                    pick_up_item = input(pick_up_item_prompt)
                    if pick_up_item == 'yes':
                        t.sleep(1)
                        pick_up()
                        add_fish()
                    elif pick_up_item == 'no':
                        t.sleep(1)
                        print("\nokay...")
                        continue
                    else:
                        t.sleep(1)
                        print("\nSorry. I don't understand.")
                        continue
                elif n == 2:
                    t.sleep(1)
                    print("\nYou didn't catch anything.")
                    continue
            elif 'fish' in items:
                t.sleep(1)
                print("\nThere are no fish to catch right now.")
                print("Maybe there will be more if you eat?")
                continue
        # eat action
        elif east_menu.lower() == 'eat':
            eat()
        # open the inventory
        elif east_menu.lower() == 'open inventory':
            # using a loop, print the in-game inventory
            print("\n\nOpened your inventory.\n")
            for item, desc in items.items():
                t.sleep(1)
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
                exit("Program has been terminated")
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


# GO West
# message to notify the user that the west input was valid
def west():
    """If the user types to go west, go west and then present more
    options for what actions the user can then perform"""
    # Write a prompt for the user
    west_prompt = ("\nWhat would you like to do? ")
    # write instructions for the user on what actions they can perform
    instructions = (f"\n{forest_tile}\nValid actions \
for current location:\nGo in the following direction:\n* east\n\
Perform one of these actions:\n* look around\n* eat\n* open \
inventory\n* quit game\n* open map\n")
    while True:
        t.sleep(1)
        # print instructions and input statement
        print(instructions)
        west_menu = input(west_prompt)
        # go back east option
        if west_menu.lower() == 'east':
            t.sleep(1)
            print("\nGoing East!\n")
            ph.hours_left -= 1
            if ph.hours_left == 7:
                clearing_night()
            t.sleep(1)
            return
        # look around action
        elif west_menu.lower() == 'look around':
            t.sleep(1)
            look_around()
            if 'stick' not in items:
                t.sleep(1)
                print(stick_item)
                t.sleep(1)
                pick_up_item = input(pick_up_item_prompt)
                if pick_up_item == 'yes':
                    t.sleep(1)
                    pick_up()
                    add_stick()
                elif pick_up_item == 'no':
                    t.sleep(1)
                    print("\nokay...")
                    continue
                else:
                    t.sleep(1)
                    print("\nSorry. I don't understand.")
                    continue
        # eat action
        elif west_menu.lower() == 'eat':
            t.sleep(1)
            eat()
        # open the inventory
        elif west_menu.lower() == 'open inventory':
            t.sleep(1)
            # using a loop, print the in-game inventory
            print("\n\nOpened your inventory.\n")
            for item, desc in items.items():
                t.sleep(1)
                print(f"{item}:")
                print(f"\tdescription: {desc['description']}")
                print(f"\teffect on health: {desc['health']}\n")
        # open the map
        elif west_menu.lower() == 'open map':
            t.sleep(1)
            print_map()
            map_tile_types()
        # quit game?
        elif west_menu.lower() == 'quit game':
            t.sleep(1)
            # ask if the user really wants to quit
            quit_game = input("\nAre you sure you want to quit? yes or no.\n")
            # the user quits, open menu
            if quit_game == 'yes':
                t.sleep(1)
                print("\nQuitting game.")
                exit("Program has been terminated")
                return
            # do not quit game, continue game
            elif quit_game == 'no':
                continue
            # input error
            else:
                print("\nSorry I didn't understand that.")
        # input error
        else:
            print("\nInvalid action!\n")


# LOOK AROUND
# print a message to notify the user that the look around input was valid
def look_around():
    """Message the user so they know their input was valid"""
    print("\nLooking around!\n")


# BUILD
# print a message to notify the user that the build input was valid
def build():
    """Message the user so they know their input was valid"""
    if 'stick' and 'tarp' in items:
        t.sleep(1)
        print("\nYou have all the right materials to Build your "
              "temporary shelter!\n\nBuilding shelter!")
        t.sleep(3)
        print("You built your shelter here. Now you won't have to be"
              " as afraid of the dark...")
        del items['stick']
        del items['tarp']
        shelter.append('yes')
        return
    elif 'stick' in items and 'tarp' not in items:
        print("\nYou don't have all the materials you need!")
        return
    elif 'tarp' in items and 'stick' not in items:
        print("\nYou don't have all the materials you need!")
        return
    elif 'yes' in shelter:
        print("\nYou already built your shelter!")
        return
    elif 'stick' and 'tarp' not in items:
        print("\nYou don't have all the materials you need!")
        return


# GO FISHING
# print a message to notify the user that the go fishing input was valid
def go_fishing():
    """Message the user so they know their input was valid"""
    print("\nGoing Fishing!\n")


# EAT
# print a message to notify the user that the eat input was valid
def eat():
    """Message the user so they know their input was valid"""
    # using a loop, print the in-game inventory
    print("\n\nOpened your inventory.\n")
    for item, desc in items.items():
        t.sleep(1)
        print(f"{item}:")
        print(f"\tdescription: {desc['description']}")
        print(f"\teffect on health: {desc['health']}\n")
    what_to_eat = ("\nWhat would you like to eat?")
    while True:
        wte = input(what_to_eat)
        # player eats fish
        if wte == 'fish' and 'fish' in items:
            print("\nEating the fish...")
            # delete fish from the inventory
            del items['fish']
            # add 5 to the player's health
            ph.player_health += 5
            # if the player's health is bigger than 15, make it 15
            if ph.player_health > 15:
                ph.player_health = 15
            # show the player their health
            print(f"\nYour health is now at {ph.player_health}")
            return
        # player eats the berries
        elif wte == 'berries' and 'berries' in items:
            print("\nEating the berries...")
            # delete berries from the inventory
            del items['berries']
            # add 2 to player health
            ph.player_health += 2
            # if player's health is above 15, make it 15
            if ph.player_health > 15:
                ph.player_health = 15
            # show the player their health
            print(f"\nYour health is now at {ph.player_health}")
            return
        # player eats the apple
        elif wte == 'apple' and 'apple' in items:
            print("\nEating the apple...")
            # remove apple from the inventory
            del items['apple']
            # add 3 to player health
            ph.player_health += 3
            # if player health is above 15, make it 15
            if ph.player_health > 15:
                ph.player_health = 15
            # show the player their health
            print(f"\nYour health is now at {ph.player_health}")
            return
        # player drinks water
        elif wte == 'water' and 'water' in items:
            print("\nDrinking water")
            # remove water from inventory
            del items['water']
            # add 2 to player health
            ph.player_health += 2
            # if player health is above 15, make it 15
            if ph.player_health > 15:
                ph.player_health = 15
            # show the player their health
            print(f"\nYour health is now at {ph.player_health}")
            return
        # player tries to eat something they currently can't
        else:
            t.sleep(1)
            print("\nYou can't eat that!")
            return


# PICK UP
# print a message to notify the user that the pick up input was valid
def pick_up():
    """Message the user so they know their input was valid"""
    print("\nPicking up!\n")


# OPEN THE CONTINUOUS ACTIONS MENU
# THIS WILL PRINT OUT A LIST OF ALL THE POSSIBLE ACTIONS IN THAT AREA
# THE USER CAN THEN TYPE WHAT ACTION TO TAKE

def the_clearing_menu():
    # Write a prompt for the user
    menu_prompt = ("\nWhat would you like to do? ")
    # write instructions for the user on what actions they can perform
    instructions = (f"\n{clearing_tile}\nValid actions for current \
location:\nGo in one of the following directions:\n* north\n\
* south\n* east\n* west\nPerform one of these actions:\n* look around\
\n* build\n* eat\n* open inventory\n* quit game\n* open map\n")
    # loop that will continue asking the user what action to perform
    while True:
        t.sleep(1)
        # tell player how many hours until dawn
        print(f"You have {ph.hours_left} hours until dawn")
        t.sleep(1)
        print(instructions)
        menu = input(menu_prompt)
        # go north action
        if menu.lower() == 'north':
            print("\nGoing North!\n")
            t.sleep(1)
            north()
        # go south action
        elif menu.lower() == 'south':
            print("\nGoing South!\n")
            t.sleep(1)
            south()
        # go east action
        elif menu.lower() == 'east':
            print("\nGoing East!\n")
            t.sleep(1)
            east()
        # go west action
        elif menu.lower() == 'west':
            print("\nGoing West!\n")
            t.sleep(1)
            west()
        # look around action
        elif menu.lower() == 'look around':
            # add shank to inventory
            if 'shank' not in items:
                t.sleep(1)
                print(shank_item)
                t.sleep(1)
                pick_up_item = input(pick_up_item_prompt)
                if pick_up_item == 'yes':
                    t.sleep(1)
                    pick_up()
                    add_shank()
                elif pick_up_item == 'no':
                    t.sleep(1)
                    print("\nokay...")
                    continue
                else:
                    print("\nSorry. I don't understand.")
                    continue
            # add shank to inventory
            if 'apple' not in items:
                t.sleep(1)
                print(apple_item)
                t.sleep(1)
                pick_up_item = input(pick_up_item_prompt)
                if pick_up_item == 'yes':
                    t.sleep(1)
                    pick_up()
                    add_apple()
                elif pick_up_item == 'no':
                    t.sleep(1)
                    print("\nokay...")
                    continue
                else:
                    t.sleep(1)
                    print("\nSorry. I don't understand.")
                    continue
        # build action
        elif menu.lower() == 'build':
            t.sleep(1)
            build()
        # eat action
        elif menu.lower() == 'eat':
            t.sleep(1)
            eat()
        # open inventory
        elif menu.lower() == 'open inventory':
            t.sleep(1)
            # using a loop, print the in-game inventory
            print("\n\nOpened your inventory.\n")
            for item, desc in items.items():
                t.sleep(1)
                print(f"{item}:")
                print(f"\tdescription: {desc['description']}")
                print(f"\teffect on health: {desc['health']}\n")
                continue
        # open the map
        elif menu.lower() == 'open map':
            t.sleep(1)
            print_map()
            map_tile_types()
        # quit the game
        elif menu.lower() == 'quit game':
            t.sleep(1)
            # ask if the user really wants to quit
            quit_game = input("\nAre you sure you want to quit? yes "
                              "or no.\n")
            # the user quits, open menu
            if quit_game == 'yes':
                t.sleep(1)
                print("\nQuitting game.")
                exit("Program has been terminated")
            # the user does not quit, do not quit
            elif quit_game == 'no':
                continue
            # input error
            else:
                t.sleep(1)
                print("\nSorry I didn't understand that.")
                continue
        # input error
        else:
            t.sleep(1)
            print("\nInvalid action!\n")
            continue
