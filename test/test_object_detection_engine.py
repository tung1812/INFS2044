import pytest
import numpy as np
import tensorflow as tf
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from object_detection_engine import ObjectDetectionEngine
from unittest.mock import Mock, patch

class TestObjectDetectionEngine:
    def test_initialization(self):
        """Test the initialization of the ObjectDetectionEngine."""
        engine = ObjectDetectionEngine()
        assert engine is not None
        assert engine.model is not None  # Check if the model is not None

    def test_load_model(self):
        """Test the load_model method."""
        engine = ObjectDetectionEngine()
        model = engine.load_model()
        assert model is not None  # Check if the model is not None

    @patch('object_detection_engine.ObjectDetectionEngine.load_model')
    def test_detect_objects_in_image(self, mock_load_model):
        # Create a mock model with expected output
        mock_model = Mock()
        mock_output_dict = {
            'num_detections': np.array([1]),
            'detection_classes': np.array([[1.0]])
        }
        mock_model.return_value = mock_output_dict

        # Set the mock model as the return value of the load_model method
        mock_load_model.return_value = mock_model

        # Initialize the ObjectDetectionEngine
        engine = ObjectDetectionEngine()
        test_image = np.random.rand(100, 100, 3)  # Replace with a suitable test image array

        # Call the method under test
        detected_objects = engine.detect_objects_in_image(test_image)

        # Assertions
        assert isinstance(detected_objects, set)
        # Additional assertions can be added based on the expected output