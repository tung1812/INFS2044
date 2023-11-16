import pytest
import numpy as np
import sys
import os
print("Current Working Directory:", os.getcwd())

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from image_access import ImageAccess
import matplotlib.image as mpimg

class TestImageAccess:
    def test_read_image_from_file_system(self):
        image_access = ImageAccess()
        image_path = 'example_images/image1.jpg' 
        image = image_access.read_image_from_file_system(image_path)
        expected_image = mpimg.imread(image_path)
        assert isinstance(image, np.ndarray)  # Asserting that the returned object is a NumPy array
        assert np.array_equal(image, expected_image)  # Optionally, assert that the images are the same
