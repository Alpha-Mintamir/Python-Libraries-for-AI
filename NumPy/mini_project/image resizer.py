import numpy as np
from PIL import Image

image = Image.open('numpy_image.png')

desired_size = (30,200)

resized_image = image.resize(desired_size)

photo = np.array(resized_image)

resized_image.show()
