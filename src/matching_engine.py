from sklearn.metrics.pairwise import cosine_similarity

class MatchingEngine:
    def __init__(self):
        """
        Initializes the MatchingEngine.
        """
        # Initialization code here, if needed

    def find_matching_image(self, image_vector, image_database):
        """
        Finds the most similar images to the given image vector in the database.

        Args:
            image_vector (np.ndarray): The vector representation of the image to find matches for.
            image_database (list): A list of image vectors to compare against.

        Returns:
            list: A list of tuples (similarity_score, image_path) sorted by similarity.
        """
        matches = []

        for img_path, img_vector in image_database.items():
            similarity = self.compute_cosine_similarity(image_vector, img_vector)
            matches.append((similarity, img_path))

        # Sort matches based on similarity score in descending order
        matches.sort(reverse=True, key=lambda x: x[0])
        return matches

    def compute_cosine_similarity(self, vector1, vector2):
        """
        Computes the cosine similarity between two vectors.

        Args:
            vector1 (np.ndarray): The first vector.
            vector2 (np.ndarray): The second vector.

        Returns:
            float: The cosine similarity between the two vectors.
        """
        return cosine_similarity([vector1], [vector2])[0][0]
