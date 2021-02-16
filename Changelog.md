# Changelog
Pre-release January 18 2021
- Created changelog
- Added README
- Made README more descriptive
- added numerical lists
  - seen in main.py
  - subject to future changes
- edited README

Pre-release January 27 2021
- Created interactive weapons and food inventories
- Moved inventory v1 to original_inventory.py
- Made locations dictionary
- Made characters dictionary
- Made all dictionaries into an interactive directory system

Pre-release February 2 2021
- added descriptions to all functions

Pre-release February 3 2021
- added a menu of possible actions that the user can take
- make the menu of actions continuous so that the player can repeatedly make choices
- added an in-game inventory that is accessible at any time during the game
- made the game quittable so that the player can quit to enter the main menu of directories
  - locations, full inventories, and characters
- added a list for all found items
- moved all lists and dictionaries to the tops of their respective files
- added more detail to comments
- added header comments that explain a large section of code
- made it so that the ser can restart the game from the main menu portion of the directory
- fixed spacing mistakes

Pre-release February 5 2021
- added while loops to all functions so that it ran smoothly, while also being more organized
- added continue to functions where needed
- made the ENTIRE program quittable with exit()

Pre release February 8 2021
- added a new file called main_menu and moved everything for the directories into there
- removed the function open_simple_menu() and turned it into the main file, which uses return to be returned to.
- replaced all calls to open_simple_menu() with a return statement
- created a new file called map
- added a map that shows each tile and locations
- added a map that shows each tile's type
- added import statements to make each file accessible where they need to be.

Pre-release February 11 2021
- added parent and child classes to map and inventory.
- made it so you can find items and add it to the inventory after looking around
- removed pick up option and only made it available when an item is found.

Pre-release February 12 2021
- changed the quit game process so that you quit the game right away instead of going through the main menu.
- removed the main menu because it is unnecessary.
- added parent and child classes for the characters in a new character module
- started making player and enemy interactions for the tiles.

Pre-release February 15 2021
- Added a player health bar that starts at 15
- remove the fight() function because it is useless and doesn't actually get used
- turned the main file into a separate file and added a function that works for the center tile (the clearing) to make it callable into the main file
- added a welcome screen to the now empty main tile that introduces the game, how it works, and the rules
- made a new module with the player health and hours left so that I can use them as global variables
- added an eat function that will open the inventory and will allow the player to replenish their inventory
- made it so that the player can collect water from the river
- made it so that the player can lose health by being attacked
- made an hours left variable that starts at 12 hours, then once there are 7 hours left, it will start the night time, and then when there are 0 hours left, the game will end.