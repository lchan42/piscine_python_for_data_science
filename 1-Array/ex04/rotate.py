from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def ft_transpose(matrice: np.ndarray) -> np.ndarray:

    """Transpose a matrix.

    Args:
        matrice (np.ndarray): The input matrix to be transposed.

    Returns:
        np.ndarray: The transposed matrix.

    Example:
        >>> original_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        >>> transposed_matrix = ft_transpose(original_matrix)
        >>> print(transposed_matrix)
        [[1 4 7]
         [2 5 8]
         [3 6 9]]
    """

    # before transpose print
    print(f"The shape of image is: {matrice.shape} or "
          f"({matrice.shape[0]}, {matrice.shape[1]})")

    # transpose
    # creat empty array for transposition
    transposed = np.zeros((len(matrice), len(matrice[0])), dtype=int)

    # add value inside transposed
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            transposed[j][i] = matrice[i][j]

    # after transpose print
    print(f"New shape after Transpose: {transposed.shape}")
    print(transposed)

    return transposed


def main():

    """Load an image, zoom in on a specific region, convert it to grayscale,
    and display the result using Matplotlib.

    Returns:
        None
    """

    try:
        np_img = ft_load("animal.jpeg")
        print(np_img)

        # reshape img
        np_img = (np_img[100: 500, 450:850])

        # convert image from 3D to 2D --> from (x, y, 3) to (x, y, 1)
        np_img = (np.mean(np_img, axis=-1, keepdims=True)).astype(np.uint8)

        np_img = ft_transpose(np_img)

        # show in plt
        plt.imshow(np_img, cmap='gray_r')
        plt.title("Zoomed Image")
        plt.axis('on')
        plt.show()

    except Exception as e:
        print(f"error of type \033[31m{type(e).__name__}\033[0m: {e} ")
        return ""


if __name__ == "__main__":

    main()
