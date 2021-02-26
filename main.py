# name : Willow Skagos
# class, period : CS30, period 2
# date created : Jan 27 2021
# description : RPG game Survive The Night

# import time
import time as t
# import the main gameplay on tiles
from tile_maneuver import *
# import the map
from map import *
# import the inventory
from in_game_inventory import *
# import the player health and hours left
import player_health as ph

"""This is an introduction to the program, explaining to the player
how to play the game, as well as maneuvering, the rules, how the hours
go by, and how player health works"""


# Write an introduction to the game
print("Welcome to Survive The Night!")
t.sleep(2)
# explain what the game is
print("\nThis is a survival adventure game where you will have to "
      "survive through one night in the woods all alone. Currently, "
      "the only item in your inventory are your fists, but don't "
      "worry, you can easily find more items to collect and use!")
t.sleep(4)
# explain enemies and tiles
print("\nIn the game, you will be able to move north, south, east, "
      "and west to explore all 5 tiles efficiently. You will also be "
      "given several other possible actions in all 5 tiles, as well "
      "as several enemies to fight, and potentially defeat, or be "
      "defeated by.")
t.sleep(5)
# talke about health
print("\nSpeaking of health, you have 15 total health points, which "
      "can be regained by eating food or drinking water.")
t.sleep(5)
print_map()
t.sleep(1)
print("\nThis is the map. You will be able to access this at almost "
      "any point in the game.")
t.sleep(3)
print("\nYou will start the game on the clearing tile. You have 5 "
      "hours until midnight, at midnight you will be forced onto the "
      "clearing tile and then you will play for another 7 hours until"
      " dawn. Good luck!")
t.sleep(3)
# start game countdown
print(f"\nStarting game in 5...")
t.sleep(1)
print("4...")
t.sleep(1)
print("3...")
t.sleep(1)
print("2...")
t.sleep(1)
print("1...\n\n\n")

"""Run the actual game, so the player can play"""
t.sleep(2)
the_clearing_menu()
