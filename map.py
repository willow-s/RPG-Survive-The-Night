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


# create a class for the map that defines the tile types and the
# difficulty
class Map:
    """Class for the map tiles' types and enemies"""
    def __init__(self, tile_type, tile_name):
        """Initialize the tile types and enemies on each tile."""
        self.tile_type = tile_type
        self.tile_name = tile_name


class Describe_tile(Map):
    def __init__(self, tile_type, tile_name):
        """copy the Map class"""
        super().__init__(tile_type, tile_name)

    def __str__(self):
        """show the type of tile that each tile is."""
        tt = (f"Welcome to the {self.tile_name} tile!\n\
This tile is a {self.tile_type} tile.")
        # return tt
        return tt


# define each tile type and enemy for the map
mountains_tile = Describe_tile('danger', 'mountains')
forest_tile = Describe_tile('supply and danger', 'forest')
clearing_tile = Describe_tile('camp', 'clearing')
river_tile = Describe_tile('food', 'river')
bear_cave_tile = Describe_tile('supply and danger', 'bear cave')
