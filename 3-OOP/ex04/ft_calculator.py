class calculator:
    """
    A class to perform vector operations.

    Static Methods:
    - dotproduct: Calculates the dot product of two vectors.

    - add_vec: Adds corresponding elements of two vectors.

    - sous_vec: Subtracts corresponding elements of V2 from V1.
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """ dotproduct: Calculates the dot product of two vectors. """
        result = 0
        for i in range(len(V1)):
            result += V1[i] * V2[i]
        print(result)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """add_vec: Adds corresponding elements of two vectors."""
        result = []
        for i in range(len(V1)):
            result.append(float(V1[i] + V2[i]))
        print(result)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """sous_vec: Subtracts corresponding elements of V2 from V1."""
        result = []
        for i in range(len(V1)):
            result.append(float(V1[i] - V2[i]))
        # result = "{:f}".format(result)
        print(f"Sous Vector is: {result}")
