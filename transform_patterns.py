import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def fourier_transform_2D(data):
    # Compute the 2D Fourier transform of the data
    f_transform = np.fft.fft2(data)

    # Shift the zero-frequency component to the center
    f_shift = np.fft.fftshift(f_transform)

    # Compute magnitude spectrum
    magnitude_spectrum = np.abs(f_shift)

    return magnitude_spectrum


def process_image(input_image_path, output_image_path):
    img = Image.open(input_image_path).convert("L")
    magnitude_spectrum = fourier_transform_2D(img)
    plt.imshow(np.log(1 + magnitude_spectrum), cmap='gray')
    plt.title('Magnitude Spectrum')
    plt.colorbar()
    if os.path.exists(output_image_path):
        os.remove(output_image_path)
    plt.savefig(output_image_path)
    plt.clf()


def main():
    directory_path = os.path.join("input")

    for root, _, files in os.walk(directory_path):
        for f in files:
            if f.endswith(".png"):
                input_image_path = os.path.join(root, f)
                base = f.replace(".png", "")
                output_image_path = os.path.join("output", f'{base}_ft.png')
                process_image(input_image_path, output_image_path)
                print("done!", input_image_path, output_image_path)


if __name__ == "__main__":
    main()
