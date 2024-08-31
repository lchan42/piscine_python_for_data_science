from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


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

        # print subject requirement
        print(f"New shape after slicing: {np_img.shape} or "
              f"({np_img.shape[0]}, {np_img.shape[1]})")
        print(np_img)

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
