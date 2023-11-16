import pytest
import numpy as np
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from matching_engine import MatchingEngine

class TestMatchingEngine:
    def test_compute_cosine_similarity(self):
        engine = MatchingEngine()
        vector1 = np.array([1, 0, 1, 0, 1])  # Example vector
        vector2 = np.array([1, 1, 0, 0, 1])  # Example vector
        similarity = engine.compute_cosine_similarity(vector1, vector2)
        assert isinstance(similarity, float)
        # Optionally, assert expected similarity value
        # assert similarity == expected_value
