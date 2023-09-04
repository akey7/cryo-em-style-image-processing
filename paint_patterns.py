import os
import numpy as np
from PIL import Image
import math


def one_rect(rect_width=50, rect_height=50, image_width=100, image_height=100):
    upper_left = ((image_width - rect_width) // 2, (image_height - rect_height) // 2)
    lower_right = (upper_left[0] + rect_width, upper_left[1] + rect_height)
    grayscale = np.zeros((image_height, image_width)).astype(np.uint8)

    for x in range(upper_left[0], lower_right[0]):
        for y in range(upper_left[1], lower_right[1]):
            grayscale[y, x] = 255

    return grayscale


def sines(h=1, k=1, image_width=100, image_height=100):
    grayscale = np.zeros((image_height, image_width)).astype(np.uint8)

    for x in range(image_width):
        for y in range(image_height):
            value = (math.sin(2*h*math.pi*x/image_width)/4+math.sin(2*k*math.pi*y/image_height)/4) + 0.5
            grayscale[y, x] = math.floor(value * 255)

    return grayscale


def main():
    grayscale_00 = np.zeros((100, 100)).astype(np.uint8)
    img_00 = Image.fromarray(grayscale_00, "L")
    img_00.save(os.path.join("input", "blackness.png"))
    
    grayscale_01 = one_rect()
    img_01 = Image.fromarray(grayscale_01, "L")
    img_01.save(os.path.join("input", "one_rect.png"))
    
    grayscale_02 = sines(h=3, k=2)
    img_02 = Image.fromarray(grayscale_02, "L")
    img_02.save(os.path.join("input", "sines_h=3_k=2.png"))

    grayscale_99 = (np.ones((100, 100)) * 255).astype(np.uint8)
    img_99 = Image.fromarray(grayscale_99, "L")
    img_99.save(os.path.join("input", "whiteness.png"))


if __name__ == "__main__":
    main()
