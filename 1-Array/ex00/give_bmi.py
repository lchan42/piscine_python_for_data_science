import numpy as np


""" _np_convertion_type_
when converting an array into numpy array, resulting np array will get type
of the bigest element from the array.priority goes generally from
object > str > complex > float > int > bool
this is due to the fact that numpy array are stored in contigues memory
addresses in order to maintain efficiency during array operation
"""


def check_array_type(array, allowed_types: type) -> bool:
    """_summary_
    Check if all element in NumPy array are of the same data type

    Parameters:
    - array: numpy.ndarray
          the array to be checked.
    - data_type: type
        the expected type for all elements in the array.

    Returns:
        bool: True if all elements in array are of type data_type

    Usage:
        check_array_type(np_array, (int, float)

    """
    return np.all(np.isin(array.dtype, allowed_types))


def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    """_summary_

    Parameters:
    - height: List[int | float]
    - weight: List[int | float]

    return:
        list of Bmi for each individual

    Raises:
        AssertionError: if lists have differents size
        AssertionError: if elements in list are different from int and float

    Returns:
        _type_: _description_
    """

    try:
        if len(height) != len(weight):
            raise AssertionError("lists are suppose to have same size")

        np_h = np.array(height)
        np_w = np.array(weight)

        if not check_array_type(np_h, (int, float)) \
                or not check_array_type(np_w, (int, float)):
            raise AssertionError("only int and float element are supported")

        return list(np_w / (np_h ** 2))

    except Exception as e:
        print(f"{type(e).__name__} : {type(e)} an error happened")


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:

    """

    Raises:
        AssertionError: if lists have differents size

    Returns:
        list of boolean

    """

    try:
        if not check_array_type(np.array(bmi), (int, float)):
            raise AssertionError("only int and float element are supported")

        return list(elem > limit for elem in bmi)

    except Exception as e:
        print(f"{type(e).__name__} : {type(e)} an error happened")
