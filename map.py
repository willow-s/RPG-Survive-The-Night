"""This is for defining and printing out the map of locations as a
grid, as well as the tile types as a grid."""

# create a map using a nested list
from tabulate import tabulate


# create a map using an array and then print it
def print_map():
    """Create a grid-like map using tabulate and arrays"""
    # design the grid-like map
    map = [['', 'mountains', ''],
           ['forest', 'clearing', 'river'],
           ['', 'bear cave', '']]
    # print an introduction for the map
    print("\n\tHere is the map of locations:")
    # print the map
    print(tabulate(map, tablefmt='grid'))


# create a map of the tile types of the regular map
def map_tile_types():
    """Create a grid-like map showing the tile types of each
    location on the regular map"""
    # create the grid of tile types for the map
    map = [['', 'Danger and Lookout', ''],
           ['Supply and Danger', 'Camp', 'Food'],
           ['', 'Supply and Danger', '']]
    # print an introduction for the tile type map
    print("\n\tHere are the tile types of each location on the map:")
    # print the tile type map
    print(tabulate(map, tablefmt='grid'))


"""create a class for the map that defines the tile types and the
difficulty"""


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
        """print a message welcoming the player to the tile and then
        telling them the type of tile that they are on"""
        # print the message
        tt = (f"Welcome to the {self.tile_name} tile!\nThis tile is "
              f"a {self.tile_type} tile.")
        # return tt
        return tt


"""create an instance of Describe_tile for each tile"""
# instance for mountains tile
mountains_tile = Describe_tile('danger', 'mountains')
# instance for forest tile
forest_tile = Describe_tile('supply and danger', 'forest')
# instance for clearing tile
clearing_tile = Describe_tile('camp', 'clearing')
# instance for river tile
river_tile = Describe_tile('food', 'river')
# instance for bear cave tile
bear_cave_tile = Describe_tile('supply and danger', 'bear cave')
