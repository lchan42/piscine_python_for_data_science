from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name, is_alive=True):
        """ Initialize a new Baratheon character."""

        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __str__(self):
        """Returns a string representation of the character."""
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self):
        """Returns a string representation of the character."""
        return self.__str__()

    def die(self):
        """ Handle the death of character. """
        self.is_alive = False


class Lannister(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name, is_alive=True):
        """ Initialize a new Lannister character."""

        super().__init__(first_name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def __str__(self):
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self):
        return self.__str__()

    def die(self):
        """ Handle the death of character. """
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        return cls(first_name, is_alive)
