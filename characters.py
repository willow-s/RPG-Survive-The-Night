"""This is for everything having to do with characters and entities in
the game, including lists of defeated and/or killed enemies, as well
as classes to accurately describe each entity"""

# list of defeated enemies
defeated_enemies = []

# list of killed enemies
killed_enemies = []

"""Create classes to describe each entity"""


class Characters:
    """Make each character and create it's characteristics"""
    def __init__(self, ent_type, strength, speed):
        """Initialize the aspects of the enemy"""
        self.ent_type = ent_type
        self.strength = strength
        self.speed = speed


class Show_Characters(Characters):
    """Show each character and it's attributes"""
    def __init__(self, ent_type, strength, speed):
        """Initialize the same arguments as class Characters"""
        super().__init__(ent_type, strength, speed)

    def __str__(self):
        """Write a sentence about each enemy"""
        sentence = (f"You have been attacked by a {self.ent_type}! "
                    f"A {self.ent_type} has {self.strength} strength "
                    f"and {self.speed} speed.")
        # return the sentence about each character
        return sentence


class Show_Characters2(Characters):
    """Show each character and it's attributes"""
    def __init__(self, ent_type, strength, speed):
        """Initialize the same arguments as class Characters"""
        super().__init__(ent_type, strength, speed)

    def __str__(self):
        """Write a sentence about each enemy"""
        sentence = (f"You have been attacked by an {self.ent_type}! "
                    f"An {self.ent_type} has {self.strength} strength "
                    f"and {self.speed} speed.")
        # return the sentence about each character
        return sentence


"""Describe each entity by creating instances of the child class
Show_Characters"""
# instance for adult bear
adult_bear = Show_Characters2('adult bear', 6, 6)
# instance for baby bear
baby_bear = Show_Characters('baby bear', 1, 5)
# instance for sasquatch
sasquatch = Show_Characters('sasquatch', 8, 5)
# instance for monster
monster = Show_Characters('monster', 10, 10)
