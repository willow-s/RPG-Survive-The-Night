"""This is for the forest tile, where the player can fight a bear and
also collect a stick to help them build a shelter"""

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
# import randint
from random import randint


def forest_bear():
    """This is where the bear in the forest attacks the player"""
    t.sleep(1)
    print("\nYou walk through an archway of broken and rotting trees "
          "into a vast, dense forest. You notice some movement ahead "
          "and take a closer look. It is a baby bear.")
    # player is attacked by bear
    t.sleep(2)
    print(adult_bear)
    t.sleep(1)
    print("\nIt's the baby's mother! This is bad.")

    # ask the player if they want to run, fight, or give up
    while True:
        bear_fight = input("\nWill you run, fight, or give up?")
        t.sleep(1)

        # player runs, dies
        if bear_fight.lower() == 'run':
            print("\nThe bear is much faster than you.")
            death_ending()

        # player fights
        elif bear_fight.lower() == 'fight':
            # random number, 1 or 2
            b_a2 = randint(1, 2)

            # player does not kill bear
            if b_a2 == 1:
                print("\nThe bear lunges at you and claws a massive "
                      "gash across your torso.")
                t.sleep(1)
                # health -3
                print("\nYour health has gone down by 3")
                # player health - 3
                ph.player_health -= 3
                # if the player's health is 0, die
                if ph.player_health <= 0:
                    # player dies
                    t.sleep(2)
                    print("\nYour health is at 0.")
                    death_ending()
                # show the player their health
                print(f"Your health is now at {ph.player_health}")
                t.sleep(1)
                # using a loop, print the in-game inventory
                print("\n\nOpened your inventory.\n")
                for item, desc in items.items():
                    print(f"{item}:")
                    print(f"\tdescription: {desc['description']}")
                    print(f"\teffect on health: {desc['health']}\n")

                # ask player what weapon to use
                while True:
                    weapon = input("\nWhich weapon would you like to "
                                   "use?")

                    # player uses shank
                    if weapon.lower() == 'shank' and 'shank' in items:
                        print("\nAfter stabilizing yourself, you "
                              "weakly swing your arm at the bear, "
                              "stabbing it in the eye. It roars in "
                              "pain, retreating with the baby bear "
                              "following shortly behind. You scramble"
                              " backwards, blood seeping from your "
                              "chest")
                        t.sleep(1)
                        # player health -2
                        ph.player_health -= 2
                        # if the player's health is 0, die
                        if ph.player_health <= 0:
                            # player dies
                            t.sleep(2)
                            print("\nYour health is at 0.")
                            death_ending()
                        print("\nYour health has gone down another "
                              "2.\nYou should probably eat before it "
                              "gets dark.")
                        t.sleep(1)
                        # show player their health
                        print(f"\nYour health is now at "
                              f"{ph.player_health}")
                        # append the adult bear to defeated enemies
                        defeated_enemies.append('adult bear')
                        # return to game
                        return

                    # player chooses sword
                    elif weapon.lower() == 'sword' and 'sword' in items:
                        print("\nAfter stabilizing yourself, you "
                              "weakly swing your arm at the bear, "
                              "slicing it across the face. It roars "
                              "in pain, retreating with the baby bear"
                              " following shortly behind. You "
                              "scramble backwards, blood seeping from"
                              " your chest")
                        t.sleep(1)
                        # player health -2
                        ph.player_health -= 2
                        # if the player's health is 0, die
                        if ph.player_health <= 0:
                            # player dies
                            t.sleep(2)
                            print("\nYour health is at 0.")
                            death_ending()
                        print("\nYour health has gone down another "
                              "2.\nYou should probably eat before it "
                              "gets dark.")
                        t.sleep(1)
                        # show player their health
                        print(f"\nYour health is now at "
                              f"{ph.player_health}")
                        # append the adult bear to defeated enemies
                        defeated_enemies.append('adult bear')
                        # return to game
                        return

                    elif weapon.lower() == 'fists':
                        t.sleep(1)
                        print("\nYou are weak and attempt to punch "
                              "the bear, but only anger it more.")
                        death_ending()

                    else:
                        print("That is not a valid weapon.")
                        continue

            # player kills the bear
            elif b_a2 == 2:
                print("\nThe bear lunges at you and claws a massive "
                      "gash across your torso.")
                t.sleep(1)
                # player health -3
                print("\nYour health has gone down by 3")
                ph.player_health -= 3
                # if the player's health is 0, die
                if ph.player_health <= 0:
                    # player dies
                    t.sleep(2)
                    print("\nYour health is at 0.")
                    death_ending()
                # show the player their health
                print(f"\nYour health is now at {ph.player_health}")
                t.sleep(1)
                # using a loop, print the in-game inventory
                print("\n\nOpened your inventory.\n")
                for item, desc in items.items():
                    print(f"{item}:")
                    print(f"\tdescription: {desc['description']}")
                    print(f"\teffect on health: {desc['health']}\n")

                # ask player what weapon to use
                while True:
                    weapon = input("\nWhich item would you like to "
                                   "use?")

                    # player uses shank
                    if weapon.lower() == 'shank' and 'shank' in items:
                        print("\nAfter stabilizing yourself, you "
                              "weakly swing your arm at the bear, "
                              "stabbing it in the eye. It roars in "
                              "pain and you swing again, stabbing it "
                              "in the side. Its health has decreased"
                              " to zero.")
                        t.sleep(1)
                        # player killed bear
                        print("\nYou have defeated the bear.")
                        # player health -2
                        ph.player_health -= 2
                        # if the player's health is 0, die
                        if ph.player_health <= 0:
                            # player dies
                            t.sleep(2)
                            print("\nYour health is at 0.")
                            death_ending()
                        t.sleep(1)
                        print("\nYour health has gone down another "
                              "2.\nYou should probably eat before it "
                              "gets dark.")
                        t.sleep(1)
                        # show player their health
                        print(f"Your health is now at "
                              f"{ph.player_health}")
                        # append the bear to defeated enemies
                        defeated_enemies.append('adult bear')
                        # append the bear to killed enemies
                        killed_enemies.append('adult bear')
                        # return to game
                        return

                    # player chooses sword
                    elif weapon.lower() == 'sword' and 'sword' in items:
                        print("\nAfter stabilizing yourself, you "
                              "weakly swing your arm at the bear, "
                              "slicing it across its chest. It roars"
                              " in pain and you swing again, stabbing"
                              " it in the side. Its health has "
                              "decreased to zero")
                        t.sleep(1)
                        # player killed bear
                        print("\nYou have defeated the bear.")
                        # player health -2
                        ph.player_health -= 2
                        # if the player's health is 0, die
                        if ph.player_health <= 0:
                            # player dies
                            t.sleep(2)
                            print("\nYour health is at 0.")
                            death_ending()
                        t.sleep(1)
                        print("\nYour health has gone down another "
                              "2.\nYou should probably eat before it "
                              "gets dark.")
                        t.sleep(1)
                        # show player their health
                        print(f"Your health is now at "
                              f"{ph.player_health}")
                        # append the bear to defeated enemies
                        defeated_enemies.append('adult bear')
                        # append the bear to killed enemies
                        killed_enemies.append('adult bear')
                        # return to game
                        return

                    elif weapon.lower() == 'fists':
                        t.sleep(1)
                        print("\nYou are weak and attempt to punch "
                              "the bear, but only anger it more.")
                        death_ending()

                    else:
                        print("\nThat is not a valid weapon.")
                        continue

        elif bear_fight.lower() == 'give up':
            give_up_ending()

        else:
            t.sleep(1)
            print("\nSorry, I didn't understand that.")
            continue
