"""Make classes that will print information about an enemy that is
in the process of attacking"""


class Characters:
    """Make each character"""
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
        sentence = (f"You have been attacked by a {self.ent_type}! \
A {self.ent_type} has {self.strength} strength and {self.speed} \
speed.")
        return sentence


# describe each entity
adult_bear = Show_Characters('adult bear', 6, 6)
baby_bear = Show_Characters('baby bear', 1, 5)
sasquatch = Show_Characters('sasquatch', 8, 5)
monster = Show_Characters('monster', 10, 10)
