import numpy as np


def check_array_type(array, allowed_types: type):
    """_summary_
    Check if all element in NumPy array are of the same data type

    Parameters:
    - array: numpy.ndarray
          the array to be checked.
    - data_type: type
        the expected type for all elements in the array.

    Raises:
    - AssertionError: if array contains elements not matching allowed_types.

    Usage:
        check_array_type(np_array, (int, float)

    Note:
    - function uses dtype attribute to determine data type of elem in array
    """

    if not np.all(np.isin(array.dtype, allowed_types)):
        raise AssertionError("array[int | float] only is supported")


def check_equal_row_sizes(array):
    """
    Check if all rows in a 2D NumPy array have the same size.

    Parameters:
    - array: np.ndarray
        The 2D NumPy array to be checked.

    Raises:
    - AssertionError: If not all rows have the same size.

    Note:
    - Function uses len() to check the size of each row.
    - An AssertionError is raised if not all rows have the same size.
    """

    if not all(len(row) == len(array[0]) for row in array):
        raise AssertionError("all row from array should have same size")


def slice_me(family: list, start: int, end: int) -> list:

    """_summary_
    Slice a list based on start and end

     Parameters:
    - family: list
        A 2D list or NumPy array to be sliced.
    - start: int
        The starting index of the slice.
    - end: int
        The ending index of the slice.

    Returns:
    - list
        The sliced portion of the input, converted to a list.

    Raises:
    - AssertionError: If issues with input parameters, such as incorrect types.
    """

    try:
        # validity checker
        assert isinstance(start, int) and isinstance(end, int), \
            "start/end have unexpected type"
        check_equal_row_sizes(family)
        # convertion into numpy array
        np_array = np.array(family)
        check_array_type(np_array, (int, float))

        print(f"My shape is : {np_array.shape}")

        # perfome slicing
        np_array = np_array[start:end]

        print(f"My new shape is : {np_array.shape}")

        # convert np_array back to list
        return np_array.tolist()

    except Exception as e:
        print(f"error of type \033[31m{type(e).__name__}\033[0m: {e} ")
        return ""
