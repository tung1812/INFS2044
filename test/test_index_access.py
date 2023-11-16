import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from index_access import IndexAccess
from unittest.mock import patch, mock_open

class TestIndexAccess:
    @patch("builtins.open", new_callable=mock_open, read_data='{}')
    def test_store_index(self, mock_file):
        index_access = IndexAccess()
        test_image_path = "example_images/image1.jpg"
        test_detected_objects = ["object1", "object2"]
        index_access.store_index(test_image_path, test_detected_objects)

        # Check if any file was opened in write mode
        mock_file.assert_called()

        # Check if the file write method was called at least once
        assert mock_file().write.called

    @patch("builtins.open", new_callable=mock_open, read_data='{"example_images/image1.jpg": ["label1", "label3"]}')
    def test_retrieve_index(self, mock_file):
        index_access = IndexAccess()
        result = index_access.retrieve_index()

        assert isinstance(result, dict)
        assert "example_images/image1.jpg" in result
        # Add more assertions as needed
