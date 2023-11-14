import pytest
from index_access import IndexAccess

class TestIndexAccess:
    def test_store_index():
        index_access = IndexAccess(indexDB="mock_database")
        index_access.storeIndex(object())  # Replace object() with a suitable test object
        # Add assertions here if needed

    def test_retrieve_index():
        index_access = IndexAccess(indexDB="mock_database")
        result = index_access.retrieveIndex()
        assert isinstance(result, list)
