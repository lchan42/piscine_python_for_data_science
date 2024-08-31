from abc import ABC, abstractmethod

# https://irma.math.unistra.fr/~franck/cours/Pythonl2/cours7_2021_slides.pdf


class Character(ABC):
    """
    Abstract base class representing a character in a story.

    Attributes:
    - first_name (str): The first name of the character.
    - is_alive (bool): A flag indicating whether the character is alive or not.
    """

    def __init__(self, first_name, is_alive=True):
        """
        Initialize a new character.

        Parameters:
        - first_name (str): The first name of the character.
        - is_alive (bool): A flag indicating whether the character
          is alive or not. Default is True.
        """

        self.first_name = first_name
        self.is_alive = is_alive

    # abstractmethod have to be defined in concrete classes
    @abstractmethod
    def die(self):
        """
        Abstract method to handle the character's death.

        This method must be implemented by concrete subclasses to handle the
        logic of what happens when the character dies.
        """
        pass


# une classe concrete doit re-definir toutes les methodes abstraites
class Stark(Character):
    """
    Concrete subclass representing a character from the Stark family.

    Attributes:
    - first_name (str): The first name of the Stark character.
    - is_alive (bool): A flag representing the Stack character alive status.
    """
    def __init__(self, first_name, is_alive=True):
        """
        Initialize a new Stark character.

        Parameters:
        - first_name (str): The first name of the Stark character.
        - is_alive (bool): Default is True.
        """
        super().__init__(first_name, is_alive)

    def die(self):
        """
        Handle the death of the Stark character.

        This method sets the is_alive flag of the Stark character to False,
        indicating that the character has died.
        """
        self.is_alive = False
