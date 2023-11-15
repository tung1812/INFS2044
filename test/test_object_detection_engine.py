import pytest
from object_detection_engine import ObjectDetectionEngine

class TestObjectDetectionEngine:
    def test_initialization():
        engine = ObjectDetectionEngine()
        assert engine is not None
        assert isinstance(engine.detectedObjects, list)
        assert len(engine.detectedObjects) == 0  # Assuming it starts empty

    def test_analyze_image():
        engine = ObjectDetectionEngine()
        test_image = "path/to/test/image.jpg"  # Replace with a suitable test image path
        engine.analyzeImage(test_image)
        assert isinstance(engine.detectedObjects, list)
        # Additional assertions can be added based on the expected output

    def test_analyze_image_with_different_inputs():
        engine = ObjectDetectionEngine()
        test_images = ["path/to/test/image1.jpg", "path/to/test/image2.jpg"]  # List of test image paths
        for test_image in test_images:
            engine.analyzeImage(test_image)
            assert isinstance(engine.detectedObjects, list)
            # Additional assertions for each test image

    def test_invalid_input():
        engine = ObjectDetectionEngine()
        with pytest.raises(Exception):  # Replace with the expected exception once known
            engine.analyzeImage(None)  # Testing with None as an invalid input
