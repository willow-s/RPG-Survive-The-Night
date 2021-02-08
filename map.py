# create a map using a nested list
from tabulate import tabulate


# create a map using an array and then print it
def print_map():
    """Create a grid-like map using tabulate and arrays"""
    map = [['', 'mountains', ''],
           ['forest', 'clearing', 'river'],
           ['', 'bear cave', '']]
    print("\n\tHere is the map of locations:")
    print(tabulate(map, tablefmt='grid'))


# create a map of the tile types of the regular map
def map_tile_types():
    """Create a grid-like map showing the tile types of each
    location on the regular map"""
    map = [['', 'Danger and Lookout', ''],
           ['Supply and Danger', 'Camp', 'Food'],
           ['', 'Supply and Danger', '']]
    print("\n\tHere are the tile types of each location on the map:")
    print(tabulate(map, tablefmt='grid'))
