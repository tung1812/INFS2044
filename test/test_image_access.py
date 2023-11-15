import pytest
from image_access import ImageAccess

class TestImageAccess:
    def test_read_image_from_file_system():
        image_access = ImageAccess()
        # Assuming readImageFromFileSystem returns an Image object
        image = image_access.readImageFromFileSystem("path/to/image")
        assert isinstance(image, Image)  # Replace 'Image' with the actual class/type of the returned object
