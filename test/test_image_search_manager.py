import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from image_search_manager import ImageSearchManager
from unittest.mock import patch

class TestImageSearchManager:
    @patch('image_search_manager.IndexAccess.retrieve_index')
    def test_execute_search(self, mock_retrieve_index):
        # Mock data returned by retrieve_index
        mock_retrieve_index.return_value = {
            "example_images/image1.jpg": ["label1", "label3"],
            "example_images/image2.jpg": ["label2", "label4"]
        }

        manager = ImageSearchManager()
        search_query = ["label1", "label2"]
        match_mode = "ALL"
        results = manager.execute_search(search_query, match_mode)

        assert isinstance(results, list)
        # Add more assertions as needed

