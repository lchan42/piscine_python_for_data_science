import numpy as np
import matplotlib.pyplot as plt


def ft_show_in_plt(array: np.ndarray, title: str):

    """
    Displays an image using the Matplotlib library.

    Parameters:
    - array (np.ndarray): The image represented as a NumPy array.
    - title (str): The title of the image to be displayed.

    """

    if title == "Grey":
        plt.imshow(array, cmap="Greys_r")
    else:
        plt.imshow(array)
    plt.title(title)
    plt.axis('off')
    plt.show()


def ft_invert(array: np.ndarray) -> np.ndarray:

    """
    Inverts the colors of an image by subtracting each pixel value from 255.

    Parameters:
    - array (np.ndarray): The image represented as a NumPy array.

    Returns:
    - np.ndarray: The inverted image as a NumPy array.
    """
    # np.ndarray are passed by reference, thus we need to copy it
    array_cpy = array.copy()
    array_cpy = 255 - array_cpy
    ft_show_in_plt(array_cpy, "Invert")
    return array_cpy


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Extracts the red channel from an image, setting the green and blue to zero.

    Parameters:
    - array (np.ndarray): The image represented as a NumPy array.

    Returns:
    - np.ndarray: The image with only the red color remaining
    """
    array_cpy = array.copy()

    mask = np.zeros(array.shape, dtype=np.uint8)
    mask[:, :, 0] = 1
    array_cpy = array_cpy * mask
    ft_show_in_plt(array_cpy, "Red")
    return array_cpy


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Extracts the green channel from an image, setting the red and blue to zero.

    Parameters:
    - array (np.ndarray): The image represented as a NumPy array.

    Returns:
    - np.ndarray: The image with only the green color remaining
    """
    array_cpy = array.copy()

    array_cpy[:, :, 0] = 0
    array_cpy[:, :, 2] = 0
    ft_show_in_plt(array_cpy, "Green")
    return array_cpy


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Extracts the blue channel from an image, setting the green and red to zero.

    Parameters:
    - array (np.ndarray): The image represented as a NumPy array.

    Returns:
    - np.ndarray: The image with only the blue color remaining
    """
    array_cpy = array.copy()

    array_cpy[:, :, 0] = 0
    array_cpy[:, :, 1] = 0
    ft_show_in_plt(array_cpy, "Blue")
    return array_cpy


# https://blog.finxter.com/how-to-convert-an-image-from-rgb-to-grayscale-in-python/
def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    modify RGB ratio so image is set to grey

    Parameters:
    - array (np.ndarray): The image represented as a NumPy array.

    Returns:
    - np.ndarray: The image with grey color ratio
    """
    # array = \
    #     array[:, :, 0] / 0.299 + \
    #     array[:, :, 1] / 0.587 + \
    #     array[:, :, 2] / 0.114
    array_cpy = array.copy()

    array_cpy = np.dot(array_cpy[..., :3], [0.299, 0.587, 0.144])
    ft_show_in_plt(array_cpy, "Grey")
    return array_cpy
