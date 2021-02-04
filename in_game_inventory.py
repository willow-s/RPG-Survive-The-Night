# here is the in-game inventory
items = {'fists': {'description': 'The most basic weapon',
                   'health': '-2'
                   }
         }

# list of all found items (empty)
found_items = []


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
                      'health': '5'
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
    items['stick'] = {'description': 'This would be great for a '
                                     'shelter...',
                      'health': 'not applicable'
                      }
