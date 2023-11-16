import matplotlib.image as mpimg
class ImageAccess:
    def __init__(self):
        self.fileSystem = None  # Assuming FileSystem is a class or a placeholder for file system access

    def read_image_from_file_system(self, filePath):
        """
        Reads an image from the file system using matplotlib and returns it as a NumPy array.

        Args:
            filePath (str): The path to the image file.

        Returns:
            np.ndarray: An image represented as a NumPy array.
        """
        try:
            # Read the image file and return it as a NumPy array
            return mpimg.imread(filePath)
        except IOError as e:
            # Handle exceptions (e.g., file not found, unsupported format)
            print(f"Error reading image from {filePath}: {e}")
            return None
