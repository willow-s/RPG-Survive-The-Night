"""This is where all of the different endings are defined"""

# import time
import time as t


def death_ending():
    """The ending where the player dies"""
    t.sleep(1)
    print("\nYou tried as hard as you could, but unfortunately your "
          "efforts were matched by your enemy and you have been "
          "defeated.")
    t.sleep(1)
    # tell player they lost the game, but there are more endings
    print("\nYou lost the game... But this is only one of several "
          "endings! Better luck next time!\n\nThank you for playing!")
    # terminate the program completely
    exit("Program has been terminated")


def morning_ending():
    """This will run when it is morning"""
    t.sleep(1)
    # show that it is morning
    print("\nThe birds chirp as the sun rises in the distance. "
          "You look to the sky and see a small object, that is "
          "slowly getting bigger.")
    t.sleep(1)
    # object comes near
    print("\nIt is coming closer to you... fast.")
    t.sleep(1)
    # the object is a helicopter
    print("\nIt is a helicopter! You are being rescued!")
    t.sleep(1)
    # player is saved
    print("\nWhen the helicopter touches down, you are greeted "
          "by several smiling faces...")
    t.sleep(1)
    # player won the game, but there are more endings
    # thank the player for playing
    print("Congratulations! You survived the night! This is only"
          " one of multiple endings, so feel free to play again!"
          "\n\nThank you for playing!")
    # terminate the program completely
    exit("Program has been terminated")


def tree_fall():
    """The player falls from tree and dies"""
    print("You slip a little but just barely catch yourself. You look"
          " down quickly and become dizzy.")
    t.sleep(1)
    print("You slip again but can't catch grip this time.")
    t.sleep(1)
    print("\n\nYou fall to your death.")
    t.sleep(1)
    # tell player they lost the game, but there are more endings
    print("\nYou lost the game... But this is only one of several "
          "endings! Better luck next time!\n\nThank you for playing!")
    # terminate the program completely
    exit("Program has been terminated")


def give_up_ending():
    """This will run when the player gives up"""
    print("You have given up and you lost the battle.")
    t.sleep(1)
    # tell player they lost the game, but there are more endings
    print("\nYou lost the game... But this is only one of several "
          "endings! Better luck next time!\n\nThank you for playing!")
    # terminate the program completely
    exit("Program has been terminated")
