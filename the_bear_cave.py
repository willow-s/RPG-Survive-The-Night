# import characters and character classes
from characters import *
# import the endings
from endings import *
# import the inventory
from in_game_inventory import *
# import the map
from map import *
# import randint
from random import randint
# import time
import time as t
# import player health and hours left
import player_health as ph

# ask the user if they would like to pick up an item
pick_up_item_prompt = ("Would you like to pick it up?")


def bear_cave():
    """This will run every time the player goes south"""
    # randomly choose whether or not the bear will attack
    b_attack = randint(1, 2)
    # player successfully sneaks past the bears
    if b_attack == 1:
        t.sleep(1)
        print("\nYou managed to sneak past the bears and are over by "
              "the pile.")
        # ask the user if they would like to look around
        while True:
            t.sleep(2)
            actions = input("\nThese are the possible actions right "
                            "now.\n* look around\n* retreat\n\nWhat would "
                            "you like to do? ")
            # player can find a tarp and add it to inventory
            if actions.lower() == 'look around':
                # player does not find tarp
                if 'tarp' in items:
                    t.sleep(1)
                    print("Looking around!")
                    continue
                # player does not find tarp
                if 'yes' in shelter:
                    t.sleep(1)
                    print("Looking around!")
                    continue
                # add tarp to inventory
                if 'tarp' not in items:
                    t.sleep(1)
                    print(tarp_item)
                    t.sleep(1)
                    pick_up_item = input(pick_up_item_prompt)
                    if pick_up_item.lower() == 'yes':
                        t.sleep(1)
                        print("\nPicking up!")
                        add_tarp()
                        continue
                    # player does not pick up item
                    elif pick_up_item.lower() == 'no':
                        t.sleep(1)
                        print("okay...")
                        continue
                    # not a valid action
                    else:
                        t.sleep(1)
                        print("Sorry. I don't understand.")
                        continue
            # player exits the cave
            elif actions.lower() == 'retreat':
                t.sleep(2)
                print("\nretreating from cave...\n")
                return
            # not a valid action
            else:
                t.sleep(1)
                print("\nThat is not a valid action.")
                continue
    # player wakes up the bears
    elif b_attack == 2:
        while True:
            t.sleep(2)
            # ask if the player wants to run, fight, or give up
            b_a = input("\nYou try to sneak past the bears, but you "
                        "accidentally wake them up. Will you run, "
                        "fight, or give up?")
            # the player runs and escapes
            if b_a.lower() == 'run':
                t.sleep(1)
                print("\nThe bears were sleepy and you managed to "
                      "escape... but only barely... The bear falls "
                      "back asleep.")
                return
            # the player gives up
            elif b_a.lower() == 'give up':
                t.sleep(1)
                death_ending()
            # the player chooses to fight the bear
            elif b_a.lower() == 'fight':
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
                    # ask the player which weapon to use
                    weapon = input("What item would you like to use?")
                    # player chooses shank
                    if weapon.lower() == 'shank' and 'shank' in items:
                        t.sleep(1)
                        print("\nThe bear lunges at you and you dodge"
                              " it but the bear still scratches you, "
                              "leaving a gaping hole in your arm. ")
                        # lower the player's health by 2
                        ph.player_health -= 4
                        t.sleep(1)
                        # if player's health is 0, player dies
                        if ph.player_health <= 0:
                            print("\nYour health is at 0.")
                            death_ending()
                        print("\nYou swing at the bear stabbing it "
                              "in the shoulder, the bear roars. It "
                              "has 1 health left. The bear cowers "
                              "back into the cave, letting you escape"
                              " easily.")
                        t.sleep(1)
                        # show player their health
                        print(f"\nYour health is at {ph.player_health}\n")
                        return
                    # player chooses sword
                    elif weapon.lower() == 'sword' and 'sword' in items:
                        t.sleep(1)
                        print("\nThe bear lunges at you and you dodge"
                              " it but the bear still scratches you, "
                              "leaving a gaping hole in your arm. ")
                        # lower the player's health by 2
                        ph.player_health -= 2
                        if ph.player_health <= 0:
                            print("\nYour health is at 0")
                            death_ending()
                        t.sleep(1)
                        print("\nYou swing at the bear and slice it's"
                              " arm but it's sloppy and only does 5 "
                              "damage. The bear has 1 health left and"
                              "cowers back into the cave, letting you"
                              "escape easily.")
                        # show the player their health
                        print(f"\nYour health is at {ph.player_health}\n")
                        return
                    # player chooses fists
                    elif weapon.lower() == 'fists':
                        t.sleep(1)
                        print("\nYou flail your fist at the bear "
                              "and hit it in the face, but it did "
                              "absolutely nothing. If anything it is "
                              "more angry... The bear slashes at your"
                              "chest.")
                        t.sleep(1)
                        # player dies
                        death_ending()
                    # incorrect input
                    else:
                        t.sleep(1)
                        print("That is not a valid weapon")
                        continue
            # incorrect input
            else:
                t.sleep(1)
                print("\nThat is not a valid action.")
                continue
