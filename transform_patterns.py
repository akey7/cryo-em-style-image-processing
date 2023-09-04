import os
import numpy as np
from PIL import Image


def fourier_transform_2D(data):
    # Compute the 2D Fourier transform of the data
    f_transform = np.fft.fft2(data)

    # Shift the zero-frequency component to the center
    f_shift = np.fft.fftshift(f_transform)

    # Compute magnitude spectrum
    magnitude_spectrum = np.abs(f_shift)

    return magnitude_spectrum


def main():
    directory_path = os.path.join('input')

    for root, _, files in os.walk(directory_path):
        for f in files:
            if f.endswith(".png"):
                file_path = os.path.join(root, f)
                print("File:", file_path)



if __name__ == '__main__':
    main()
