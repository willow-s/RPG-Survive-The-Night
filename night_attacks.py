"""This is where all of the monster and animal attacks from the file
night_time are defined"""

# import player health and hours left
import player_health as ph
# import time
import time as t
# import characters
from characters import *
# import the endings
from endings import *
# import the inventory
from in_game_inventory import *


# monster fight for the outdoors1 and no shelter
def monster_fight():
    """This is the code for the monster fight that happens in
    the_outdoors1"""
    print("\nBehind you, a twig snaps and you spin around to look, "
          "but there is nothing there. You turn around again, and "
          "there's the monster right in front of your face. It growls"
          " and snaps its jaws at you.")
    t.sleep(1)
    print(monster)

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
                    print("\nYou jump at the monster with the shank "
                          "pointed straight forward. Unfortunately, "
                          "because the monster is made out of "
                          "branches, stabbing isn't going to do very "
                          "much good.")
                    t.sleep(1)
                    print("The monster roars and stabs you with its "
                          "giant branches, scratching you "
                          "everywhere")
                    t.sleep(1)
                    print("\nYour health has decreased by 4.")
                    # health -4
                    ph.player_health -= 4
                    # if health <= 0, die
                    if ph.player_health <= 0:
                        t.sleep(2)
                        print("\nYour health is at 0.")
                        death_ending()
                    t.sleep(1)
                    print(f"\nYour health is at {ph.player_health}\n")

                    # monster attacks again
                    t.sleep(1)
                    print("\nYou try swinging the shank this time, "
                          "but it just thuds against the branches.")
                    t.sleep(1)
                    print("\nThe monster bites you this time and you "
                          "kick it so hard that one of its large "
                          "branches snaps. It lets go of your arm.")
                    t.sleep(1)
                    print("\nYour health has decreased by 7")
                    # health -7
                    ph.player_health -= 7
                    # if player health <= 0, die
                    if ph.player_health <= 0:
                        t.sleep(2)
                        print("\nYour health is at 0.")
                        death_ending()
                    t.sleep(1)
                    print(f"\nYour health is at {ph.player_health}\n")

                    # player survives
                    t.sleep(1)
                    print("\nYou weakly swing, but you somehow "
                          "managed to stab the monster in the eye. "
                          "The monster roars painfully and retreats "
                          "into the forest.")
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
                    return

                # player chooses sword
                elif ww.lower() == 'sword' and 'sword' in items:
                    t.sleep(1)
                    print("\nYou swing the sword as hard as you can "
                          "at the monster and manage to cut through "
                          "a few branches")
                    t.sleep(1)
                    print("\nThe monster roars and you swing again, "
                          "breaking more branches. It lunges at you "
                          "and bites your hand.")
                    t.sleep(1)
                    print("\nYour health has decreased by 4.")
                    # health -4
                    ph.player_health -= 4
                    # if player health <= 0, die
                    if ph.player_health <= 0:
                        t.sleep(2)
                        print("\nYour health is at 0.")
                        death_ending()
                    t.sleep(1)
                    print(f"\nYour health is at {ph.player_health}\n")

                    # player survives
                    print("\nYou weakly swing the sword again, "
                          "cutting a few more branches in the "
                          "process. The monster growls and retreats "
                          "into the forest.")
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
                    return

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


# the second monster fight for the outdoors1
def monster_fight2():
    """This will run outside of the shelter when the player climbs
    down the tree, but only if the player hasn't already killed a
    bear"""
    t.sleep(1)
    print("\nYou hear growling behind you and you tense up, turning "
          "around quickly. The monster! But how... it seemed so far "
          "away from the top of the tree...")
    t.sleep(1)
    print("No matter... The monster smiles its creepy smile at you "
          "and you know what you must do.")

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
                    return

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
                    return

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


# bear fight for the outdoors 1 and 2, and clearing no
def bear_fight():
    """This is a bear fight that is universal, so it can be
    used anywhere. It will be used if the player has not killed the bear"""
    print(adult_bear)
    print("\nThe bear jumps at you and lands of top of you. "
          "It scratches you across the face.")
    # player health - 2
    ph.player_health -= 2
    # if player health <= 0, die
    if ph.player_health <= 0:
        t.sleep(2)
        print("Your health is at 0.")
        death_ending()
    t.sleep(1)
    print(f"\nYour health is at {ph.player_health}\n")

    # Use a loop to ask the player if they want to run, fight
    # or give up
    while True:
        # ask player if they want to fight
        fa = input("Do you want to run, fight, or give up?")

        # player runs
        if fa.lower() == 'run':
            t.sleep(2)
            death_ending()

        # player gives up
        elif fa.lower() == 'give up':
            t.sleep(2)
            give_up_ending()

        # player fights
        elif fa.lower() == 'fight':
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

                # player chooses shank
                if ww.lower() == 'shank' and 'shank' in weapons:
                    t.sleep(1)
                    print("\nYou take out your shank and hit the bear"
                          "in the leg. It topples over, but quickly "
                          "gets up and jumps at you again. The bear "
                          "has taken 2 damage. It has 4 health left.")
                    t.sleep(1)
                    print("\nYou have the shank pointed outward "
                          "toward the bear just in time so that "
                          "instead of biting you, the bear only "
                          "scratches you with its teeth.")
                    t.sleep(1)
                    print("\nYour health has decreased by 2.")
                    # player health - 2
                    ph.player_health -= 2
                    # if player health <= 0, die
                    if ph.player_health <= 0:
                        t.sleep(2)
                        print("Your health is at 0.")
                        death_ending()
                    t.sleep(1)
                    print(f"\nYour health is at {ph.player_health}\n")

                    # bear attacks again
                    t.sleep(1)
                    print("As the bear tried to bite you, you stabbed"
                          " it in the shoulder. Its health has "
                          "decreased by another 2. It has 2 health "
                          "left.")
                    t.sleep(1)
                    print("The bear falls back and begins to run at "
                          "you. In fear, you point the shank straight"
                          " out in front of you. The bear runs "
                          "straight into it.")
                    t.sleep(1)
                    # append adult bear to the list of killed enemies
                    killed_enemies.append('adult bear')
                    # player killed the bear
                    print("\nYou have killed the bear.\nOne hour has "
                          "passed.")
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
                    return

                # player chooses sword
                elif ww.lower() == 'sword' and 'sword' in items:
                    t.sleep(1)
                    print("\nYou pull out your sword and swing as "
                          "hard as you can at the bear, slicing open "
                          "its face, blinding it.")
                    t.sleep(1)
                    print("\nThe bear cowers back and claws at you, "
                          "scratching your arm. Your health has "
                          "decreased by 1.")
                    # player health - 1
                    ph.player_health -= 1
                    # if player health <= 0, die
                    if ph.player_health <= 0:
                        t.sleep(2)
                        print("Your health is at 0.")
                        death_ending()
                    t.sleep(1)
                    print(f"\nYour health is at {ph.player_health}\n")
                    t.sleep(1)
                    print("\nYou swing again and impale the bear "
                          "through the head.\nYou have killed the "
                          "bear.\nOne hour has passed.")
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
                    return

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
