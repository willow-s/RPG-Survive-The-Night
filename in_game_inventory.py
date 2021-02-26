"""This is for all things involving the inventory, and the player's
shelter and bonfire"""

# here is the in-game inventory
items = {'fists': {'description': 'The most basic weapon',
                   'health': '-2'
                   }
         }

# make a list if the player has created a shelter and a fire
# this will be not be accessible by the player
shelter = []

# make a list that will represent the player's sleep
# this will not be accessible by the player
# this will allow the player to sleep only once
player_sleep = []


# add berries to the inventory
def add_berries():
    """Append berries to the list of items"""
    items['berries'] = {'description': 'A delicious, blue fruit',
                        'health': '+2'
                        }


# add fish to the inventory
def add_fish():
    """Append fish to the list of items"""
    items['fish'] = {'description': 'A meaty animal that came '
                     'from the water',
                     'health': '+5'
                     }


# add water to the inventory
def add_water():
    """Append water to the list of items"""
    items['water'] = {'description': 'drink',
                      'health': '+2'
                      }


# add apple to the inventory
def add_apple():
    """Append apple to the list of items"""
    items['apple'] = {'description': 'yummy fruit',
                      'health': '+3'
                      }


# add sword to the inventory
def add_sword():
    """Append sword to the list of items"""
    items['sword'] = {'description': 'A long sharp thing',
                      'health': '-8'
                      }


# add shank to the inventory
def add_shank():
    """Append shank to the list of items"""
    items['shank'] = {'description': 'A really sharp stick',
                      'health': '-5'
                      }


# add stick to the inventory
def add_stick():
    """Append stick to the list of items"""
    items['stick'] = {'description': 'It is a long wooden rod, '
                      'it could be useful...',
                      'health': 'not appicable'
                      }


# add tarp to the inventory
def add_tarp():
    """Append tarp to the list of items"""
    items['tarp'] = {'description': 'This would be great for a '
                     'shelter...',
                     'health': 'not applicable'
                     }


# add dry sticks to inventory
def add_sticks():
    """Append the dry sticks to the list of items"""
    items['dry sticks'] = {'description': 'These would be '
                           'great for a fire...',
                           'health': 'not applicable'
                           }


# add mysterious meat to inventory
def add_mysterious_meat():
    """Append the mysterious meat to the list of items"""
    items['mysterious meat'] = {'description': 'It is meat and it '
                                'is mysterious',
                                'health': '???'
                                }


"""Classes to collect items and add them to the inventory."""


class Found_item:
    """Declare that an item has been found"""
    def __init__(self, item):
        """Initialize the item"""
        self.item = item


class Add_to_inventory(Found_item):
    def __init__(self, item):
        """Initialize the item"""
        super().__init__(item)

    def __str__(self):
        """Declare the item has been found"""
        found = (f"\nYou found a {self.item}!")
        # return the sentence declaring the player has found an item
        return found


class Add_to_inventory2(Found_item):
    def __init__(self, item):
        """Initialize the item"""
        super().__init__(item)

    def __str__(self):
        """Declare the item has been found"""
        found = (f"\nYou found an {self.item}!")
        # return the sentence declaring the player has found an item
        return found


class Add_to_inventory3(Found_item):
    def __init__(self, item):
        """Initialize the item"""
        super().__init__(item)

    def __str__(self):
        """Declare the item has been found"""
        found = (f"\nYou found {self.item}!")
        # return the sentence declaring the player has found an item
        return found


"""Create instances of Add_to_inventory that will declare an item has
been found"""
# instance for fish
fish_item = Add_to_inventory('fish')
# instance for berries
berries_item = Add_to_inventory3('berries')
# instance for water
water_item = Add_to_inventory3('water')
# instance for apple
apple_item = Add_to_inventory2('apple')
# instance for sword
sword_item = Add_to_inventory('sword')
# instance for shank
shank_item = Add_to_inventory('shank')
# instance for stick
stick_item = Add_to_inventory('stick')
# instance for tarp
tarp_item = Add_to_inventory('tarp')
# instance for dry sticks
dry_sticks_item = Add_to_inventory3('dry sticks')
mysterious_meat_item = Add_to_inventory3('mysterious meat')
