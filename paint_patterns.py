from os.path import join
import numpy as np
from PIL import Image

def save_rgb_as_png(red, green, blue, filename):
    """
    Saves three numpy arrays as red, green, and blue channels in a PNG file.

    Parameters:
    - red, green, blue: numpy arrays of the same shape representing the RGB channels.
    - filename: the name of the PNG file to save.
    """
    # Stack arrays along the third dimension
    image_array = np.stack((red, green, blue), axis=-1)
    
    # Convert to PIL Image and save
    img = Image.fromarray(image_array.astype('uint8'))
    img.save(filename)
