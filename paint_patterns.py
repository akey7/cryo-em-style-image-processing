from os.path import join
import numpy as np
from PIL import Image


def one_rect(rect_width=50, rect_height=50, image_width=100, image_height=100):
    upper_left = ((image_width - rect_width) // 2, (image_height - rect_height) // 2)
    lower_right = (upper_left[0] + rect_width, upper_left[1] + rect_height)    
    grayscale = np.zeros((image_height, image_width)).astype(np.uint8)
    
    for x in range(upper_left[0], lower_right[0]):
        for y in range(upper_left[1], lower_right[1]):
            grayscale[y, x] = 255

    return grayscale


def main():
    grayscale = one_rect()
    img = Image.fromarray(grayscale, 'L')
    img.save(join('output', 'one_rect.png'))


if __name__ == '__main__':
    main()
