import json
import os

class IndexAccess:
    def __init__(self, index_file='image_index.json'):
        """
        Initializes the IndexAccess class with a file-based index system.

        Args:
            index_file (str): The path to the JSON file used for storing the index.
        """
        self.index_file = index_file
        # Ensure the file exists and is not empty
        if not os.path.exists(self.index_file) or os.path.getsize(self.index_file) == 0:
            with open(self.index_file, 'w') as file:
                json.dump({}, file)

    def store_index(self, image_path, detected_objects):
        try:
            # Read the current index, ensuring the file is not empty
            if os.path.getsize(self.index_file) > 0:
                with open(self.index_file, 'r') as file:
                    index = json.load(file)
            else:
                index = {}

            # Update the index
            index[image_path] = detected_objects

            # Write the updated index back to the file
            with open(self.index_file, 'w') as file:
                json.dump(index, file)
        except json.JSONDecodeError as e:
            print(f"Error reading JSON file: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def retrieve_index(self):
        try:
            # Read the index, ensuring the file is not empty
            if os.path.getsize(self.index_file) > 0:
                with open(self.index_file, 'r') as file:
                    return json.load(file)
            else:
                return {}
        except json.JSONDecodeError as e:
            print(f"Error reading JSON file: {e}")
            return {}
        except Exception as e:
            print(f"An error occurred: {e}")
            return {}
