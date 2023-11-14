import pytest
from matching_engine import MatchingEngine

class TestMatchingEngine:
    def test_find_matching_image(self):
        engine = MatchingEngine()
        result = engine.findMatchingImage(None)  # Replace None with a mock Image object
        assert isinstance(result, list)

    def test_compute_cosine_similarity(self):
        engine = MatchingEngine()
        similarity = engine.computeCosineSimilarity(None, None)  # Replace None with mock Image objects
        assert isinstance(similarity, float)
