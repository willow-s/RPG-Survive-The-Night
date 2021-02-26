"""This will be for night time in the clearing"""

# import time
import time as t
# import the in-game inventory
from in_game_inventory import *
# import player health and hours left
import player_health as ph
# import the endings
from endings import *
# import the characters
from characters import *
# import randint
from random import randint
# import the monster and animal attacks for night time
from night_attacks import *


# this is the start of the night time, the player can build shelter
# if they haven't already and they have the materials
def clearing_night():
    """This will run the night time scenarios"""
    # introduction to the night
    print("...")
    t.sleep(3)
    print("\nIt is midnight...")
    t.sleep(3)
    print("\nYou walk into the centre of the clearing, looking around"
          " trying to see through the deep darkness of the forest...")
    t.sleep(1)
    print("\nYou can't see anything...")
    t.sleep(3)
    print("\nA loud roar rings out through the forest, though it "
          "isn't exactly a roar, kind of a scream.\nIt is followed by"
          " low growls, reverberating through your bones.")
    # if a shelter has been built
    if 'yes' in shelter:
        t.sleep(1)
        yes_shelter()
    # if a shelter has not yet been built, ask if the player wants to
    # build one.
    elif 'tarp' in items and 'stick' in items:
        while True:
            t.sleep(1)
            print("\nYou have not yet made a shelter, yet you have "
                  "all of the materials to do so...")
            shelt = input("\nWould you like to build a shelter?")
            # if the player says yes to building a shelter
            if shelt.lower() == 'yes':
                t.sleep(1)
                print("\nYou pull out the stick and stick it into the"
                      " ground, sticking straight up into the air. "
                      "Then you pull out the tarp and drape it over "
                      "the stick, causing the tarp to make a loud "
                      "crinkling noise.")
                # append yes to shelter, shelter has been made
                shelter.append('yes')
                # run the yes shelter function
                yes_shelter()
            # the player says no to building a shelter
            elif shelt.lower() == 'no':
                # ask if player is sure
                t.sleep(1)
                print("You will not get another chance to build a "
                      "shelter...")
                no_s = input("Are you sure you don't want to build a "
                             "shelter?")
                # player does not build shelter
                if no_s.lower() == 'yes':
                    # run function for no shelter
                    no_shelter()
                # player is not sure
                elif no_s.lower() == 'no':
                    continue
                # incorrect input
                else:
                    print("Sorry, I didn't understand that.")
                    continue
            # incorrect input
            else:
                t.sleep(1)
                print("Sorry, I didn't understand that.")
                continue
    # If a shelter has not already been built, and the player does
    # not have the materials to build a shelter
    else:
        t.sleep(1)
        no_shelter()


# this will run if the player builds their shelter, the monster attacks
def yes_shelter():
    """This will run if a shelter is built. A monster attack happens here"""
    print("\nThe leaves rustle with your movement. You hear a grunt "
          "come from the forest behind you and whirl around, putting "
          "your back toward the shelter. A pair of small, vertically "
          "slit eyes glow through the dark at you...")
    t.sleep(2)
    print("\nAnd then a crunch...")
    t.sleep(2)
    print("\nMovement...")
    t.sleep(1)
    print("\nThe eyes begin moving...")
    t.sleep(1)
    print("\nYou panic as the eyes move closer toward you, so you "
          "turn away.")
    t.sleep(1)
    print("\nYou turn around once more as you slip inside the tarp. "
          "Catching the glowing eyes surrounded by what could only be"
          "described as an incarnation of the forest itself;")
    t.sleep(1)
    print("A body of twisted branches and vines that tear and snap "
          "with every move. A cloud of dust, dirt and leaves that "
          "fall and cloud the vision and fill the lungs, "
          "suffocating every one of its victims with ease. A "
          "demented creature full of insects and darkness.")
    t.sleep(1)
    print("\nYou pause, captivated by terror as a wide smile fills "
          "its face. But it is not a friendly face... it is a "
          "manic face, the face of a merciless, moralless monster "
          "whose only purpose is to torment the souls of anyone with "
          " a luck so unfortunate as to come face-to-face with such a"
          " terrible beast.")
    t.sleep(1)
    print("The creature lunges toward you, a million snaps and cracks"
          " ensue and you can only hope that they aren't your bones. "
          "A deep and terrible pain covers your cheek as you duck "
          "inside the tarp. The creature roars loudly and it sounds "
          "as if it is fleeing. Once the low grumble of the beast has"
          " faded, you see a giant gash covering your arm.")
    t.sleep(1)
    # player health -3
    ph.player_health -= 3
    # if player health <= 0, player dies
    if ph.player_health <= 0:
        t.sleep(2)
        print("\nYour health is at 0.")
        death_ending()
    print("\nYou have lost 3 health")
    # show player their health
    print(f"Your health is at {ph.player_health}")
    night_clearing_yes()


# this will run after the player completes yes-shelter
def night_clearing_yes():
    """These are all of the possible actions for
    the night time clearing"""
    # show the player possible actions
    instructions = ("\nThis is the clearing tile.\nValid actions "
                    "for current location:\n* feel around\n* build"
                    " a fire\n* look outside\n* eat\n* open "
                    "inventory\n* view health\n* sleep")

    # prompt
    prompt = ("\nWhat would you like to do?")
    # loop to ask player what they want to do
    while True:
        t.sleep(1)
        # ask the user what they would like to do
        print(instructions)
        night_menu = input(prompt)

        # user chooses to feel around
        if night_menu.lower() == 'feel around':
            # player can't pick up sticks
            if 'fire' in shelter:
                t.sleep(1)
                print("\nFeeling around!")
                print("There is nothing to find here at the moment.")
                continue
            # user can't pick up sticks
            if 'dry sticks' in items:
                t.sleep(1)
                print("\nFeeling around!")
                print("There is nothing to find here at the moment.")
                continue
            # user picks up sticks
            if 'dry sticks' not in items:
                t.sleep(1)
                print("Feeling around!\n")
                t.sleep(1)
                print(dry_sticks_item)
                # ask if user wants to pick up sticks
                pick_up = input("\nWould you like to pick them up?")
                # user picks up sticks
                if pick_up.lower() == 'yes':
                    t.sleep(1)
                    print("Picking them up!")
                    # append sticks to inventory
                    add_sticks()
                # user does not pick up sticks
                elif pick_up.lower == 'no':
                    t.sleep(1)
                    print("\nokay...")
                    continue
                # invalid input
                else:
                    t.sleep(1)
                    print("\nSorry, I didn't understand that.")
                    continue

            # there is nothing to find
            else:
                print("\nThere is nothing to find at the moment.")

        # player eats
        elif night_menu.lower() == 'eat':
            t.sleep(1)
            eat_food()

        # player views health
        elif night_menu.lower() == 'view health':
            print(f"\nYour health is at {ph.player_health}")

        # player chooses to sleep
        elif night_menu.lower() == 'sleep':
            # if the player has already slept
            if 'sleep' in player_sleep:
                print("\nYou can only sleep once.")
                continue
            # if the player has not slept yet
            if 'sleep' not in player_sleep:
                t.sleep(1)
                print("You lay down in the dry leaves under the "
                      "tarp and slowly drift off to sleep...")
                # player cannot sleep again
                player_sleep.append('sleep')
                # hours left -3
                ph.hours_left -= 3
                # if hours left <= 0, morning
                if ph.hours_left <= 0:
                    morning_ending()
                t.sleep(5)
                # player wakes up
                print("\nThree hours later, you have woken up.")
                # show the player the number of hours left
                if ph.hours_left == 1:
                    print(f"There is {ph.hours_left} hour until dawn.")
                else:
                    print(f"There are {ph.hours_left} hours until dawn.")
                continue

        # player chooses to build a fire
        elif night_menu.lower() == 'build a fire':
            # player already built a fire
            if 'fire' in shelter:
                t.sleep(1)
                print("\nYou have already built a fire!")
                continue
            # player does not have the materials
            if 'dry sticks' not in items:
                t.sleep(1)
                print("\nYou don't have the materials you need"
                      " to build a fire...")
                continue
            # player builds a fire
            if 'dry sticks' in items:
                t.sleep(1)
                print("\nBuilding a fire!")
                print("That took a very long time to do..."
                      "\n\nOne hour has passed.")
                # append fire to shelter so the player can't make 2
                shelter.append('fire')
                # hours left -1
                ph.hours_left -= 1
                # if hours left <= 0, morning
                if ph.hours_left <= 0:
                    morning_ending()
                # show the player the number of hours left
                if ph.hours_left == 1:
                    print(f"There is {ph.hours_left} hour until dawn.")
                else:
                    print(f"There are {ph.hours_left} hours until dawn.")
                continue

        # player opens inventory
        elif night_menu.lower() == 'open inventory':
            t.sleep(1)
            # using a loop, print the in-game inventory
            print("\n\nOpened your inventory.\n")
            for item, desc in items.items():
                print(f"{item}:")
                print(f"\tdescription: {desc['description']}")
                print(f"\teffect on health: {desc['health']}\n")

        # player chooses to look outside
        elif night_menu.lower() == 'look outside':
            t.sleep(1)
            print("You look outside of your shelter and peer "
                  "through the darkness. You see nothing.")
            t.sleep(1)
            # ask if the player would like to go outside
            outside = input("\nWould you like to go outside?")
            # player does not go outside
            if outside.lower() == 'no':
                t.sleep(1)
                print("\nYou return inside the shelter.")
                continue
            # player does go outside
            elif outside.lower() == 'yes':
                # randomly choose a number that will determine if
                # the player meets the monster or not
                look = randint(1, 2)
                # player is attacked by the monster
                if look == 1:
                    t.sleep(1)
                    print("\nYou carefully crawl out from under the "
                          "tarp and stand with your back to the "
                          "shelter.")
                    t.sleep(1)
                    print("\nsilence...")
                    t.sleep(2)
                    print("You take another step out into the "
                          "clearing... nothing... more silence. "
                          "It seems the monster is gone... ")
                    t.sleep(2)
                    print("\nfor now...")
                    the_outdoors1()
                # player is not attacked by the monster
                elif look == 2:
                    t.sleep(1)
                    print("\nYou carefully crawl out from under the "
                          "tarp and stand with your back to the "
                          "shelter.")
                    t.sleep(1)
                    print("\nsilence...")
                    t.sleep(2)
                    print("You take another step out into the "
                          "clearing... nothing... more silence. "
                          "It seems the monster is gone... ")
                    the_outdoors2()

            # invalid input
            else:
                t.sleep(1)
                print("\nSorry, I didn't understand that.")
                continue
        # invalid input
        else:
            t.sleep(1)
            print("\nThat is not a valid action.")
            continue


# this will run the main function for outside the shelter if the player
# will be attacked by the monster (determined in night_clearing_yes)
def the_outdoors1():
    """This is for when the player exits the shelter and is attacked
    by the monster"""
    # the monster attacks the player
    t.sleep(1)
    monster_fight()

    # instructions for what actions can be taken
    instructions = ("\nValid actions for current location:\n* look "
                    "for food\n* climb a tree\n* eat\n* return to "
                    "shelter\n* open inventory\n* view health\n"
                    "* quit game\n\nWhat would you like to do? ")

    # use a loop to display all actions to the player and ask them
    # what to do
    while True:
        t.sleep(1)
        action = input(instructions)

        # player looks for food
        if action.lower() == 'look for food':
            t.sleep(1)
            print("Looking around!")
            t.sleep(1)
            # player finds mysterious meat
            if 'mysterious meat' not in items:
                print(mysterious_meat_item)
                # ask player if they want to pick up the mysterious
                # meat
                pu = input("Would you like to pick it up?")
                # player picks up the mysterious meat
                if pu.lower() == 'yes':
                    t.sleep(1)
                    print("\nPicking up!")
                    add_mysterious_meat()
                # player does not pick up the mysterios meat
                elif pu.lower() == 'no':
                    t.sleep(1)
                    print("okay...")
                    continue
                # invalid input
                else:
                    t.sleep(1)
                    print("\nSorry, I didn't understand that.")
                    continue

            # There is nothing to find
            else:
                print("\nThere is nothing to find at the moment.")

        # player climbs a tree
        elif action.lower() == 'climb a tree':
            t.sleep(1)
            print("\nYou walk up to the tallest tree you can see and "
                  "start to climb.")
            t.sleep(3)
            print("You finally reach the top and look out. The trees "
                  "shake in the distance. The monster seems far"
                  "enough away now, so you might be safe for a bit.")
            t.sleep(1)
            print("\nYou begin to climb down the tree slowly...")
            # choose a random number from 1 to 3
            tf = randint(1, 3)
            # player falls from tree and dies
            if tf == 1:
                t.sleep(1)
                tree_fall()
            # player gets down safely
            elif tf == 2 or 3:
                t.sleep(1)
                print("You safely return to the ground")
                t.sleep(1)
                print("\nOne hour has passed.")
                # hours left -1
                ph.hours_left -= 1
                # if hours left <= 0, morning
                if ph.hours_left <= 0:
                    morning_ending()
                # show the player the number of hours left
                if ph.hours_left == 1:
                    print(f"There is {ph.hours_left} hour until dawn.")
                else:
                    print(f"There are {ph.hours_left} hours until dawn.")

                # if the adult bear was not killed, the player is
                # attacked by a bear
                if 'adult bear' not in killed_enemies:
                    print(adult_bear)
                    print("\nYou thought that if you were going to be "
                          "attacked by anything, it would be the monster"
                          "... But it's the same bear from the forest!"
                          " And it is super angry!")
                    bear_fight()

                # monster attack instead of bear attack
                else:
                    t.sleep(2)
                    monster_fight2()
                continue

        # player eats
        elif action.lower() == 'eat':
            t.sleep(1)
            eat_food()

        # player tries to move east:
        elif action.lower() == 'east':
            print("You can't go that way. You can't see far enough.")

        # player tries to move west:
        elif action.lower() == 'west':
            print("You can't go that way. You can't see far enough.")

        # player tries to move east:
        elif action.lower() == 'north':
            print("You can't go that way. You can't see far enough.")

        # player tries to move east:
        elif action.lower() == 'south':
            print("You can't go that way. You can't see far enough.")

        # player views health
        elif action.lower() == 'view health':
            print(f"\nYour health is at {ph.player_health}")

        # player quits the game
        elif action.lower() == 'quit game':
            t.sleep(1)
            # ask if the user really wants to quit
            quit_game = input("\nAre you sure you want to quit? yes or no.\n")
            # the user quits, open menu
            if quit_game.lower() == 'yes':
                t.sleep(1)
                print("\nQuitting game.")
                exit("Program has been terminated")
            # do not quit game, continue game
            elif quit_game.lower() == 'no':
                continue
            # input error
            else:
                print("\nSorry, I didn't understand that.")

        # player opens inventory
        elif action.lower() == 'open inventory':
            t.sleep(1)
            # using a loop, print the in-game inventory
            print("\n\nOpened your inventory.\n")
            for item, desc in items.items():
                print(f"{item}:")
                print(f"\tdescription: {desc['description']}")
                print(f"\teffect on health: {desc['health']}\n")

        # player returns to shelter
        elif action.lower() == 'return to shelter':
            t.sleep(1)
            return

        # invalid input
        else:
            t.sleep(1)
            print("That is not a valid action.")


# this will run the main function for outside the shelter if the player
# will not be attacked by the monster (determined in night_clearing_yes)
def the_outdoors2():
    """This is for when the player exits the shelter and is not
    attacked by the monster"""
    # instructions for what actions can be taken
    instructions = ("\nValid actions for current location:\n* look "
                    "for food\n* climb a tree\n* eat\n* return to "
                    "shelter\n* open inventory\n* view health\n"
                    "* quit game\n\nWhat would you like to do? ")

    # use a loop to display all actions to the player and ask them
    # what to do
    while True:
        t.sleep(1)
        action = input(instructions)

        # player looks for food
        if action.lower() == 'look for food':
            t.sleep(1)
            print("Looking around!")
            t.sleep(1)
            # player finds mysterious meat
            if 'mysterious meat' not in items:
                print(mysterious_meat_item)
                # ask player if they want to pick up the mysterious
                # meat
                pu = input("Would you like to pick it up?")
                # player picks up the mysterious meat
                if pu.lower() == 'yes':
                    t.sleep(1)
                    print("\nPicking up!")
                    add_mysterious_meat()
                # player does not pick up the mysterios meat
                elif pu.lower() == 'no':
                    t.sleep(1)
                    print("okay...")
                    continue
                # invalid input
                else:
                    t.sleep(1)
                    print("\nSorry, I didn't understand that.")
                    continue

            # there is nothing to find
            else:
                print("\nThere is nothing to find at the moment.")

        # player climbs a tree
        elif action.lower() == 'climb a tree':
            t.sleep(1)
            print("\nYou walk up to the tallest tree you can see and "
                  "start to climb.")
            t.sleep(3)
            print("You finally reach the top and look out. The trees "
                  "shake in the distance. The monster seems far"
                  "enough away now, so you might be safe for a bit.")
            t.sleep(1)
            print("\nYou begin to climb down the tree slowly...")
            # choose a random number from 1 to 3
            tf = randint(1, 3)
            # player falls from tree and dies
            if tf == 1:
                t.sleep(1)
                tree_fall()
            # player gets down safely
            elif tf == 2 or 3:
                t.sleep(1)
                print("You safely return to the ground")
                t.sleep(1)
                print("\nOne hour has passed.")
                # hours left -1
                ph.hours_left -= 1
                # if hours left <= 0, morning
                if ph.hours_left <= 0:
                    morning_ending()
                # show the player the number of hours left
                if ph.hours_left == 1:
                    print(f"There is {ph.hours_left} hour until dawn.")
                else:
                    print(f"There are {ph.hours_left} hours until dawn.")
                t.sleep(2)

                # player is attacked by a bear
                print(adult_bear)
                print("\nYou thought that if you were going to be "
                      "attacked by anything, it would be the monster"
                      "... But it's the same bear from the cave!"
                      " And it is super angry!")
                bear_fight()
                continue

        # player eats
        elif action.lower() == 'eat':
            t.sleep(1)
            eat_food()

        # player tries to go north
        elif action.lower() == 'north':
            print("You can't go that way. You can't see far enough.")

        # player tries to go south
        elif action.lower() == 'south':
            print("You can't go that way. You can't see far enough.")

        # player tries to go east
        elif action.lower() == 'east':
            print("You can't go that way. You can't see far enough.")

        # player tries to go west
        elif action.lower() == 'west':
            print("You can't go that way. You can't see far enough.")

        # player views health
        elif action.lower() == 'view health':
            print(f"\nYour health is at {ph.player_health}")

        # player opens inventory
        elif action.lower() == 'open inventory':
            t.sleep(1)
            # using a loop, print the in-game inventory
            print("\n\nOpened your inventory.\n")
            for item, desc in items.items():
                print(f"{item}:")
                print(f"\tdescription: {desc['description']}")
                print(f"\teffect on health: {desc['health']}\n")

        # player quits the game
        elif action.lower() == 'quit game':
            t.sleep(1)
            # ask if the user really wants to quit
            quit_game = input("\nAre you sure you want to quit? yes or no.\n")
            # the user quits, open menu
            if quit_game.lower() == 'yes':
                t.sleep(1)
                print("\nQuitting game.")
                exit("Program has been terminated")
            # do not quit game, continue game
            elif quit_game.lower() == 'no':
                continue
            # input error
            else:
                print("\nSorry, I didn't understand that.")

        # player returns to shelter
        elif action.lower() == 'return to shelter':
            t.sleep(1)
            return

        # invalid input
        else:
            t.sleep(1)
            print("That is not a valid action.")


# this will run anytime the player wants to eat food
def eat_food():
    """The player eats food"""
    # using a loop, print the in-game inventory
    print("\n\nOpened your inventory.\n")
    for item, desc in items.items():
        print(f"{item}:")
        print(f"\tdescription: {desc['description']}")
        print(f"\teffect on health: {desc['health']}\n")
    what_to_eat = ("\nWhat would you like to eat?")

    # Use a loop to ask the player what they want to eat
    while True:
        wte = input(what_to_eat)

        # player eats mysterious meat
        if wte.lower() == 'mysterious meat' and 'mysterious meat' in items:
            print("\nEating the mysterious meat...")
            # delete mysterious meat from the inventory
            del items['mysterious meat']
            # player health = 15
            ph. player_health = 15
            # show the player their health
            print(f"\nYour health is now at {ph.player_health}")
            return

        # player eats fish
        if wte.lower() == 'fish' and 'fish' in items:
            print("\nEating the fish...")
            # delete fish from the inventory
            del items['fish']
            # player health + 5
            ph.player_health += 5
            # if the player's health is bigger than 15, make it 15
            if ph.player_health > 15:
                ph.player_health = 15
            # show the player their health
            print(f"\nYour health is now at {ph.player_health}")
            return

        # player eats the berries
        elif wte.lower() == 'berries' and 'berries' in items:
            print("\nEating the berries...")
            # delete berries from the inventory
            del items['berries']
            # player health + 2
            ph.player_health += 2
            # if player's health is above 15, make it 15
            if ph.player_health > 15:
                ph.player_health = 15
            # show the player their health
            print(f"\nYour health is now at {ph.player_health}")
            return

        # player eats the apple
        elif wte.lower() == 'apple' and 'apple' in items:
            print("\nEating the apple...")
            # remove apple from the inventory
            del items['apple']
            # player health + 3
            ph.player_health += 3
            # if player health is above 15, make it 15
            if ph.player_health > 15:
                ph.player_health = 15
            # show the player their health
            print(f"\nYour health is now at {ph.player_health}")
            return

        # player drinks water
        elif wte.lower() == 'water' and 'water' in items:
            print("\nDrinking water")
            # remove water from inventory
            del items['water']
            # player health + 2
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


"""ALL OF THE CODE BELOW HERE IS FOR IF NO SHELTER IS BUILT"""


# this will run if the player does not build a shelter
def no_shelter():
    """This will run if a shelter is not built"""
    # the player is attacked by the monster
    t.sleep(1)
    print("\nThe leaves rustle with your movement. You hear a grunt "
          "come from the forest behind you and whirl around. A pair of small, "
          "vertically slit eyes glow through the dark at you...")
    t.sleep(2)
    print("\nAnd then a crunch...")
    t.sleep(2)
    print("\nMovement...")
    t.sleep(1)
    print("\nThe eyes begin moving...")
    t.sleep(1)
    print("\nYou panic as the eyes move closer toward you, so you "
          "turn away.")
    t.sleep(1)
    print("\nYou turn around once more, catching the glowing eyes "
          "surrounded by what could only be described as an "
          "incarnation of the forest itself;")
    t.sleep(1)
    print("A body of twisted branches and vines that tear and snap "
          "with every move. A cloud of dust, dirt and leaves that "
          "fall and cloud the vision and fill the lungs, "
          "suffocating every one of its victims with ease. A "
          "demented creature full of insects and darkness.")
    t.sleep(1)
    print("\nYou pause, captivated by terror as a wide smile fills "
          "its face. But it is not a friendly face... it is a "
          "manic face, the face of a merciless, moralless monster "
          "who's only purpose is to torment the souls of anyone with "
          " a luck so unfortunate as to come face-to-face with such a"
          " terrible beast.")
    t.sleep(1)
    print("The creature lunges toward you, a million snaps and cracks"
          " ensue and you can only hope that they aren't your bones. "
          "A deep and terrible pain covers your cheek as you duck. "
          "The creature roars loudly.")
    monster_fight_no()


# this will run after no_shelter
def monster_fight_no():
    """This is the first monster fight for no shelter"""
    # use a loop to ask the player if they want to run, fight, or
    # give up
    while True:
        # ask the player if they want to run, fight, or give up
        m_a = input("\nWill you run, fight, or give up?")

        # player runs, dies
        if m_a.lower() == 'run':
            t.sleep(1)
            death_ending()

        # player gives up, dies
        elif m_a.lower() == 'give up':
            t.sleep(1)
            give_up_ending()

        # player fights
        elif m_a.lower() == 'fight':
            t.sleep(1)
            # using a loop, print the in-game inventory
            print("\n\nOpened your inventory.\n")
            for item, desc in items.items():
                print(f"{item}:")
                print(f"\tdescription: {desc['description']}")
                print(f"\teffect on health: {desc['health']}\n")

            # use a loop to ask the player which weapon to use
            while True:
                ww = input("\nWhich weapon do you want to use?")

                # player uses shank
                if ww.lower() == 'shank' and 'shank' in items:
                    t.sleep(1)
                    print("You pull out your shank and attempt to stab "
                          " the monster, and you succeed, but sprain your "
                          "wrist in the process, and you only dented one "
                          "of the monster's branches.")
                    t.sleep(1)
                    print("\nYour health has decreased by 1")
                    # player health - 1
                    ph.player_health -= 1
                    # if player health <= 0, die
                    if ph.player_health <= 0:
                        t.sleep(2)
                        print("Your health is at 0.")
                        death_ending()
                    print(f"Your health is at {ph.player_health}\n")
                    # monster knocks player out
                    t.sleep(1)
                    print("\nYou charge at the monster, screaming, "
                          "pointing the shank directly at its face. You "
                          "stab it in the same spot that would be its "
                          "nose. It roars and hits you in the head with "
                          "one of its large branches.")
                    t.sleep(1)
                    print("You have been knocked out.")
                    t.sleep(2)
                    print("\nOne hour has passed")
                    # hours left -1
                    ph.hours_left -= 1
                    # if there are no hours left, end game
                    if ph.hours_left <= 0:
                        morning_ending()
                    # show the player the number of hours left
                    if ph.hours_left == 1:
                        print(f"There is {ph.hours_left} hour until dawn.")
                    else:
                        print(f"There are {ph.hours_left} hours until dawn.")
                    clearing_no()

                # player chooses sword
                elif ww.lower() == 'sword' and 'sword' in items:
                    t.sleep(1)
                    print("You pull out your sword and swing at the "
                          "monster, you cut several of its branches. It "
                          "roars and hits you in the head with one of its "
                          "largest branches.")
                    t.sleep(1)
                    print("You have been knocked out.")
                    t.sleep(2)
                    print("\nOne hour has passed")
                    # hours left -1
                    ph.hours_left -= 1
                    # if there are no hours left, end game
                    if ph.hours_left <= 0:
                        morning_ending()
                    # show the player the number of hours left
                    if ph.hours_left == 1:
                        print(f"There is {ph.hours_left} hour until dawn.")
                    else:
                        print(f"There are {ph.hours_left} hours until dawn.")
                    clearing_no()

                # player chooses fists
                elif ww.lower() == 'fists':
                    t.sleep(1)
                    print("You attempt to punch the monster but only "
                          "break your harnd on the monster's giant "
                          "branches.")
                    t.sleep(1)
                    death_ending()

                # invalid input
                else:
                    t.sleep(1)
                    print("\nThat is not a valid weapon.")
                    continue

        # invalid input
        else:
            t.sleep(1)
            print("\nThat is not a valid action.")
            continue


# this will run once the player has survived the monster in
# monster_fight_no
# This is the main exploration control for if the player does not build
# shelter
def clearing_no():
    """This is the clearing for when the player does not have a shelter.
    Everything happens from here"""
    # instructions for what actions can be taken
    instructions = ("\nValid actions for current location:\n* look "
                    "for food\n* climb a tree\n* eat\n* sleep on the "
                    "ground\n* build a fire\n* feel around\n* open "
                    "inventory\n* view health\n* quit game\n\nWhat "
                    "would you like to do? ")

    # use a loop to display all actions to the player and ask them
    # what to do
    while True:
        t.sleep(1)
        action = input(instructions)

        # player looks for food
        if action.lower() == 'look for food':
            t.sleep(1)
            print("Looking around!")
            t.sleep(1)
            # player finds mysterious meat
            if 'mysterious meat' not in items:
                print(mysterious_meat_item)
                # ask player if they want to pick up the mysterious
                # meat
                pu = input("Would you like to pick it up?")
                # player picks up the mysterious meat
                if pu.lower() == 'yes':
                    t.sleep(1)
                    print("\nPicking up!")
                    add_mysterious_meat()
                # player does not pick up the mysterios meat
                elif pu.lower() == 'no':
                    t.sleep(1)
                    print("okay...")
                    continue
                # invalid input
                else:
                    t.sleep(1)
                    print("\nSorry, I didn't understand that.")
                    continue

            # there is nothing to find
            else:
                print("\nThere is nothing to find at the moment.")

        # player climbs a tree
        elif action.lower() == 'climb a tree':
            t.sleep(1)
            print("\nYou walk up to the tallest tree you can see and "
                  "start to climb.")
            t.sleep(3)
            print("You finally reach the top and look out. The trees "
                  "shake in the distance. The monster seems far"
                  "enough away now, so you might be safe for a bit.")
            t.sleep(1)
            print("\nYou begin to climb down the tree slowly...")
            # choose a random number from 1 to 3
            tf = randint(1, 3)
            # player falls from tree and dies
            if tf == 1:
                t.sleep(1)
                tree_fall()
            # player gets down safely
            elif tf == 2 or 3:
                t.sleep(1)
                print("You safely return to the ground")
                t.sleep(1)
                print("\nOne hour has passed.")
                # hours left -1
                ph.hours_left -= 1
                # if hours left <= 0, morning
                if ph.hours_left <= 0:
                    morning_ending()
                # show the player the number of hours left
                if ph.hours_left == 1:
                    print(f"There is {ph.hours_left} hour until dawn.")
                else:
                    print(f"There are {ph.hours_left} hours until dawn.")

                # if the adult bear was not killed, the player is
                # attacked by a bear
                if 'adult bear' not in killed_enemies:
                    print(adult_bear)
                    print("\nYou thought that if you were going to be "
                          "attacked by anything, it would be the monster"
                          "... But it's the same bear from the forest!"
                          " And it is super angry!")
                    bear_fight()

                # monster attack instead of bear attack
                else:
                    t.sleep(2)
                    monster_fight()
                continue

        # player eats
        elif action.lower() == 'eat':
            t.sleep(1)
            eat_food()

        # player tries to go north
        elif action.lower() == 'north':
            print("You can't go that way. You can't see far enough.")

        # player tries to go south
        elif action.lower() == 'south':
            print("You can't go that way. You can't see far enough.")

        # player tries to go east
        elif action.lower() == 'east':
            print("You can't go that way. You can't see far enough.")

        # player tries to go west
        elif action.lower() == 'west':
            print("You can't go that way. You can't see far enough.")

        # player views health
        elif action.lower() == 'view health':
            print(f"\nYour health is at {ph.player_health}")

        # player opens inventory
        elif action.lower() == 'open inventory':
            t.sleep(1)
            # using a loop, print the in-game inventory
            print("\n\nOpened your inventory.\n")
            for item, desc in items.items():
                print(f"{item}:")
                print(f"\tdescription: {desc['description']}")
                print(f"\teffect on health: {desc['health']}\n")

        # player quits the game
        elif action.lower() == 'quit game':
            t.sleep(1)
            # ask if the user really wants to quit
            quit_game = input("\nAre you sure you want to quit? yes or no.\n")
            # the user quits, open menu
            if quit_game.lower() == 'yes':
                t.sleep(1)
                print("\nQuitting game.")
                exit("Program has been terminated")
            # do not quit game, continue game
            elif quit_game.lower() == 'no':
                continue
            # input error
            else:
                print("\nSorry, I didn't understand that.")
                continue

        # player chooses to sleep on the ground
        elif action.lower() == 'sleep on the ground':
            # if the player has already slept
            if 'sleep' in player_sleep:
                print("\nYou can only sleep once.")
            # if the player has not slept yet
            if 'sleep' not in player_sleep:
                t.sleep(1)
                print("\nYou lay on the hard and uncomfortable ground, yet"
                      " you find no difficulties falling asleep because "
                      "you're exhausted from the day's events. You drift "
                      "off to sleep...")
                # player cannot sleep again
                player_sleep.append('sleep')
                t.sleep(5)
                # hours left - 2
                ph.hours_left -= 2
                # tell the player how many hours left.
                print("\nYou wake up 2 hours later to the sound of "
                      "growling in the distance.")
                # if hours left <= 0, it is morning and the player won.
                if ph.hours_left <= 0:
                    t.sleep(1)
                    morning_ending()
                # show the player the number of hours left
                if ph.hours_left == 1:
                    print(f"There is {ph.hours_left} hour until dawn.")
                else:
                    print(f"There are {ph.hours_left} hours until dawn.")
                t.sleep(2)
                # player took damage because the ground is uncomfortable
                print("\nYour health has decreased by 2 because the "
                      "ground was uncomfortable.")
                # player health -2
                ph.player_health -= 2
                # if player health <= 0, die
                if ph.player_health <= 0:
                    t.sleep(1)
                    death_ending()
                print(f"Your health is at {ph.player_health}.")
                continue

        # player chooses to build a fire
        elif action.lower() == 'build a fire':
            # player already built a fire
            if 'fire' in shelter:
                t.sleep(1)
                print("\nYou have already built a fire!")
                continue
            # player does not have the materials
            if 'dry sticks' not in items:
                t.sleep(1)
                print("\nYou don't have the materials you need"
                      " to build a fire...")
                continue
            # player builds a fire
            if 'dry sticks' in items:
                t.sleep(1)
                print("\nBuilding a fire!")
                print("That took a very long time to do..."
                      "\n\nOne hour has passed.")
                # append fire to shelter so the player can't make 2
                shelter.append('fire')
                # hours left -1
                ph.hours_left -= 1
                # if hours left <= 0, morning
                if ph.hours_left <= 0:
                    t.sleep(1)
                    morning_ending()
                # show the player the number of hours left
                if ph.hours_left == 1:
                    print(f"There is {ph.hours_left} hour until dawn.")
                else:
                    print(f"There are {ph.hours_left} hours until dawn.")
                continue

        # player chooses to feel around
        elif action.lower() == 'feel around':
            # player can't pick up sticks
            if 'fire' in shelter:
                t.sleep(1)
                print("\nFeeling around!")
                print("There is nothing to find here at the moment.")
                continue
            # user can't pick up sticks
            if 'dry sticks' in items:
                t.sleep(1)
                print("\nFeeling around!")
                print("There is nothing to find here at the moment.")
                continue
            # user picks up sticks
            if 'dry sticks' not in items:
                t.sleep(1)
                print("Feeling around!\n")
                t.sleep(1)
                print(dry_sticks_item)
                # ask if user wants to pick up sticks
                pick_up = input("\nWould you like to pick them up?")
                # user picks up sticks
                if pick_up.lower() == 'yes':
                    t.sleep(1)
                    print("Picking them up!")
                    # append sticks to inventory
                    add_sticks()
                    # hours left - 1
                    print("\nIt took a really long time to find those "
                          "sticks because you're so shaky and it's "
                          "so dark.")
                    t.sleep(1)
                    print("\nOne hour has passed.")
                    # hours left -1
                    ph.hours_left -= 1
                    # If hours left <= 0, it is morning and the player won
                    if ph.hours_left <= 0:
                        t.sleep(1)
                        morning_ending()
                    # show the player the number of hours left
                    if ph.hours_left == 1:
                        print(f"There is {ph.hours_left} hour until dawn.")
                    else:
                        print(f"There are {ph.hours_left} hours until dawn.")
                    continue
                # user does not pick up sticks
                elif pick_up.lower == 'no':
                    t.sleep(1)
                    print("\nokay...")
                    continue
                # invalid input
                else:
                    t.sleep(1)
                    print("\nSorry, I didn't understand that.")
                    continue

            # there is nothing to find
            else:
                print("\nThere is nothing to find at the moment.")

        # invalid input
        else:
            t.sleep(1)
            print("That is not a valid action.")
            continue
