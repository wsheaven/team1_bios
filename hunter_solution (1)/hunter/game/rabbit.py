import random

class Rabbit:
    """A code template for a cute little fuzzy-tailed animal. The 
    responsibility of this class of objects is to watch the hunter and give 
    hints.
    
    Stereotype:
        Information Holder

    Attributes:
        location (integer): The location of the Rabbit (1-1000).
        distance (list): The distance from the hunter.
    """

    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Rabbit): An instance of Rabbit.
        """
        self.location = random.randint(1, 1000)
        self.distance = [0, 0] # start with two so get_hint always works
    
    def get_hint(self):
        """Gets a hint for the hunter.

        Args:
            self (Rabbit): An instance of Rabbit.
        
        Returns:
            string: A hint for the hunter.
        """
        hint = "(-.-) Maybe I'll take a nap."
        if self.distance[-1] == 0:
            hint = "(;.;) You found me!"
        elif self.distance[-1] > self.distance[-2]:
            hint = "(^.^) Getting colder!"
        elif self.distance[-1] < self.distance[-2]:
            hint = "(>.<) Getting warmer!"
        return hint
        
    def watch(self, location):
        """Watches the given location by keeping track of how far away it is.

        Args:
            self (Rabbit): An instance of Rabbit.
        """
        distance = abs(self.location - location)
        self.distance.append(distance)