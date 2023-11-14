import pytest
from image_access import ImageAccess

class TestImageAccess:
    def test_find_matching_image():
        engine = MatchingEngine()
        result = engine.findMatchingImage(None)  # Replace None with a mock Image object
        assert isinstance(result, list)

    def test_compute_cosine_similarity():
        engine = MatchingEngine()
        similarity = engine.computeCosineSimilarity(None, None)  # Replace None with mock Image objects
        assert isinstance(similarity, float)