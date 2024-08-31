import numpy as np
from PIL import Image


def ft_load(path: str) -> list:
    """
    Load an image from the specified path and return it as a NumPy array.

    Args:
    - path (str): The path to the image file.

    Returns:
    - np.ndarray: The image represented as a NumPy array.

    Raises:
    - Exception: If there is an error while loading the image.

    Note:
    - The function uses the Pillow (PIL) library to open and load the image.
    - The resulting image is converted to a NumPy array for further processing.
    - If an error occurs during the loading process, an exception is raised
        and an error message is printed.
    """

    try:
        img = Image.open(path)
        np_img = np.array(img)
        print(f"The shape of image is: {np_img.shape}")
        return np_img
    except Exception as e:
        print(f"error of type \033[31m{type(e).__name__}\033[0m: {e} ")
        return ""
