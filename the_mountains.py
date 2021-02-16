# import characters and character classes
from characters import *
# import all endings
from endings import *
# import the inventory
from in_game_inventory import *
# import the map
from map import *
# import time
import time as t
# import player health and hours left
import player_health as ph


def sasquatch_attack():
    """This will run one time when the player goes north"""
    t.sleep(1)
    print(mountains_tile)
    print()
    t.sleep(2)
    print(sasquatch)
    while True:
        t.sleep(2)
        # ask the player if they want to fight, run or give up
        action = input("\nWhat would you like to do? Run, fight, or "
                       "give up?")
        # player runs
        if action == 'run':
            t.sleep(1)
            # player dies
            death_ending()
        # player fights
        elif action == 'fight':
            t.sleep(1)
            # using a loop, print the in-game inventory
            print("\n\nOpened your inventory.\n")
            for item, desc in items.items():
                t.sleep(1)
                print(f"{item}:")
                print(f"\tdescription: {desc['description']}")
                print(f"\teffect on health: {desc['health']}\n")
            while True:
                t.sleep(1)
                # ask the user which weapon to use
                weapon = input("\nWhat item would you like to use?")
                # player chooses shank
                if weapon == 'shank' and 'shank' in items:
                    t.sleep(2)
                    print("\nYou take a swing at your opponent and "
                          "strike the sasquatch in the side. It has "
                          "3 health remaining. The sasquatch lifts "
                          "you and tosses you away with ease. You run"
                          "at the sasquatch and stab it directly in "
                          "the stomach. It falls to the ground. You"
                          " have won this battle.")
                    # lower the player's health by 4
                    ph.player_health -= 4
                    print(f"\nYour health is at {ph.player_health}")
                    # if the player's health is 0, die
                    if ph.player_health <= 0:
                        # player dies
                        t.sleep(2)
                        print("\nYour health is at 0.")
                        death_ending()
                    return
                # player chooses fists
                elif weapon == 'fists':
                    t.sleep(2)
                    print("\nYou flail your fist at the sasquatch "
                          "and hit it in the stomach, but it did "
                          "absolutely nothing. The sasquatch picks "
                          "you up and swings you into a tree.")
                    t.sleep(1)
                    # player dies
                    death_ending()
                # invalid input
                else:
                    t.sleep(1)
                    print("That is not a valid weapon")
                    continue
        # player gives up
        elif action == 'give up':
            t.sleep(1)
            # player dies
            death_ending()
        # invalid input
        else:
            t.sleep(1)
            print("\nThat's not a valid action.")
            continue
