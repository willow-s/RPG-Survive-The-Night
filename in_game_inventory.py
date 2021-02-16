# here is the in-game inventory
items = {'fists': {'description': 'The most basic weapon',
                   'health': '-2'
                   }
         }

# make a variable for the number of hours left
hours_left = 12

# list of all found items (empty)
found_items = []


# make a list if the player has created a shelter
shelter = []


# add berries to the inventory
def add_berries():
    items['berries'] = {'description': 'A delicious, blue fruit',
                        'health': '+2'
                        }


# add fish to the inventory
def add_fish():
    items['fish'] = {'description': 'A meaty animal that came '
                     'from the water',
                     'health': '+5'
                     }


# add water to the inventory
def add_water():
    items['water'] = {'description': 'drink',
                      'health': '+2'
                      }


# add apple to the inventory
def add_apple():
    items['apple'] = {'description': 'The most basic weapon',
                      'health': '+3'
                      }


# add sword to the inventory
def add_sword():
    items['sword'] = {'description': 'A long sharp thing',
                      'health': '-8'
                      }


# add shank to the inventory
def add_shank():
    items['shank'] = {'description': 'A really sharp stick',
                      'health': '-5'
                      }


# add stick to the inventory
def add_stick():
    items['stick'] = {'description': 'It is a long wooden rod, '
                      'it could be useful...',
                      'health': 'not appicable'
                      }


# add tarp to the inventory
def add_tarp():
    items['tarp'] = {'description': 'This would be great for a '
                     'shelter...',
                     'health': 'not applicable'
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
        found = (f"\nYou found {self.item}!")

        return found


fish_item = Add_to_inventory('fish')
berries_item = Add_to_inventory('berries')
water_item = Add_to_inventory('water')
apple_item = Add_to_inventory('apple')
sword_item = Add_to_inventory('sword')
shank_item = Add_to_inventory('shank')
stick_item = Add_to_inventory('stick')
tarp_item = Add_to_inventory('tarp')
