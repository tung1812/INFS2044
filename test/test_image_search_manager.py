import pytest
from image_search_manager import ImageSearchManager

class TestImageSearchManager:
    def test_execute_search(self):
        # Test executeSearch method
        manager = ImageSearchManager()
        manager.executeSearch()  # Assuming no return value; adjust as needed
        # Add assertions here if there are any expected side effects or state changes
