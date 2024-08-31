class calculator:
    """
    A class to perform arithmetic operations on a vector.

    Attributes:
    - vector (list): The input vector on which operations will be performed.
    """

    def __init__(self, vector: []):
        """
        Initializes a calculator object with the provided vector.

        Parameters:
        - vector (list): vector on which operations will be performed.
        """
        self.vector = vector

# self.vector = [x + object for x in self.vector]
# here we create a new list --> space dimention ++
#

    def __add__(self, object) -> None:
        """  Adds a scalar value to each element of the vector. """
        for i in range(len(self.vector)):
            self.vector[i] += object
        print(self.vector)
        return self.vector

    def __mul__(self, object) -> None:
        """ Multiplies each element of the vector by a scalar value. """
        for i in range(len(self.vector)):
            self.vector[i] *= object
        print(self.vector)
        return self.vector

    def __sub__(self, object) -> None:
        """ Subtracts a scalar value from each element of the vector. """
        for i in range(len(self.vector)):
            self.vector[i] -= object
        print(self.vector)
        return self.vector

    def __truediv__(self, object) -> None:
        """ Divides each element of the vector by a scalar value."""
        try:
            for i in range(len(self.vector)):
                self.vector[i] /= object
            print(self.vector)
            return self.vector
        except Exception as e:
            print(f"from {__name__} \033[31m{type(e).__name__}\033[0m: {e} ")
