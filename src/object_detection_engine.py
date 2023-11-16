import numpy as np
import tensorflow as tf
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from object_detector import ALL_LABELS, DETECTION_MODEL_DIR, detect_objects

class ObjectDetectionEngine:
    def __init__(self):
        self.model = self.load_model()

    def load_model(self):
        """Loads the detection model from directory DETECTION_MODEL_DIR"""
        model = tf.saved_model.load(DETECTION_MODEL_DIR)    
        return model.signatures['serving_default']

    def detect_objects_in_image(self, image):
        """Detects objects in image and returns the set of labels for the objects"""
        image = np.asarray(image)
        input_tensor = tf.convert_to_tensor(image)
        input_tensor = input_tensor[tf.newaxis, ...]
        
        output_dict = self.model(input_tensor)

        num_detections = int(output_dict['num_detections'])
        detected_classes = output_dict['detection_classes'][0,:num_detections]

        # Check if 'detected_classes' is a TensorFlow tensor and convert it to a NumPy array if it is
        if hasattr(detected_classes, 'numpy'):
            detected_classes = detected_classes.numpy()

        detected_classes = detected_classes.astype(int)

        labels = set(ALL_LABELS[cls] for cls in detected_classes)
        return labels
