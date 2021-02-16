"""This is where all of the different endings are defined"""


def death_ending():
    """The ending where the player dies"""
    t.sleep(1)
    print("\nYou tried as hard as you could, but unfortunately your \
efforts were matched by your enemy and you have been defeated.")
    t.sleep(1)
    print("\nYou lost the game... But this is only one of several \
endings! Better luck next time!")
    exit("Program has been terminated")
