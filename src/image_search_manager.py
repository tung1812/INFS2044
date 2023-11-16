from object_detection_engine import ObjectDetectionEngine
from index_access import IndexAccess

class ImageSearchManager:
    def __init__(self):
        self.object_detection_engine = ObjectDetectionEngine()
        self.index_access = IndexAccess()

    def execute_search(self, search_query, match_mode):
        """
        Executes an image search based on the provided query and match mode.

        Args:
            search_query (list): A list of object types to search for.
            match_mode (str): The match mode ('ALL' or 'SOME').

        Returns:
            list: A list of image paths that match the search criteria.
        """
        # Retrieve all indexed images
        indexed_images = self.index_access.retrieve_index()

        # Filter images based on the match mode and search query
        matching_images = []
        for image_path, detected_objects in indexed_images.items():
            if match_mode == 'ALL' and all(obj in detected_objects for obj in search_query):
                matching_images.append(image_path)
            elif match_mode == 'SOME' and any(obj in detected_objects for obj in search_query):
                matching_images.append(image_path)

        return matching_images

    def process_image_for_search(self, image_path):
        """
        Processes an image for search by detecting objects and updating the index.

        Args:
            image_path (str): The path to the image file.
        """
        # Detect objects in the image
        detected_objects = self.object_detection_engine.detect_objects_in_image(image_path)

        # Update the index with the detected objects
        self.index_access.store_index(image_path, detected_objects)

        return detected_objects
