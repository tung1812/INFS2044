import click
import tensorflow as tf
import numpy as np
import sys
from src.object_detection_engine import ObjectDetectionEngine
from src.image_access import ImageAccess
from src.index_access import IndexAccess
from src.matching_engine import MatchingEngine

@click.group()
def main():
    pass

#
# Each of the functions below is the entry point of a use case for the command line application.
# Call your code from each of these functions, but do not include all of your code in the functions
# in this file.
#

@main.command()
@click.argument('image_path', type=click.Path(exists=True, dir_okay=False))
def add(image_path):
    """Add an image to the system."""
    # print(f"Received image path: {image_path}")
    engine = ObjectDetectionEngine()
    image_access = ImageAccess()
    index_access = IndexAccess()

    image = image_access.read_image_from_file_system(image_path)
    detected_labels = engine.detect_objects_in_image(image)
    # print(f"Detected labels (before conversion): {detected_labels}")
    # print(f"Type of detected_labels: {type(detected_labels)}")

    # Convert the set of labels to a list before storing
    detected_labels_list = [label for label in detected_labels]
    # print(f"Detected labels (after conversion): {detected_labels_list}")
    index_access.store_index(image_path, detected_labels_list)
    print(f"Image added with labels: {detected_labels}")


@main.command()
@click.option('--all/--some', default=True, show_default=True, help='List images that match all/some query terms')
@click.argument('terms', nargs=-1, required=True)
def search(all, terms):
    """Search for images that match the query terms."""
    index_access = IndexAccess()
    images = index_access.retrieve_index()
    
    matching_images = []

    for image_path, image_data in images.items():
        labels = set(image_data)
        query_terms = set(terms)
        if (all and query_terms.issubset(labels)) or (not all and query_terms.intersection(labels)):
            matching_images.append(image_path)

    for path in matching_images:
        print(path)
    print(f"{len(matching_images)} matches found.")

@main.command()
@click.option('--k', default=1, type=click.IntRange(1), show_default=True, help='Number of matches to return')
@click.argument('image_path', type=click.Path(exists=True, dir_okay=False))
def similar(k, image_path):
    """Find similar images."""
    matching_engine = MatchingEngine()
    image_access = ImageAccess()
    index_access = IndexAccess()

    # Define the target dimensions for the images
    target_height = 128  # Example height
    target_width = 128   # Example width

    target_image = image_access.read_image_from_file_system(image_path)
    # Resize the target image using TensorFlow and then flatten it
    target_image_resized = tf.image.resize(target_image, [target_height, target_width])
    target_image_flattened = np.array(target_image_resized).flatten().astype('float32')

    images = index_access.retrieve_index()
    similarities = []

    for image_path in images:
        current_image = image_access.read_image_from_file_system(image_path)
        # Resize the current image using TensorFlow and then flatten it
        current_image_resized = tf.image.resize(current_image, [target_height, target_width])
        current_image_flattened = np.array(current_image_resized).flatten().astype('float32')

        similarity = matching_engine.compute_cosine_similarity(target_image_flattened, current_image_flattened)
        similarities.append((image_path, similarity))

    similarities.sort(key=lambda x: x[1], reverse=True)
    for path, similarity in similarities[:k]:
        print(f"{similarity:.4f} {path}")


@main.command()
def list():
    """List all images and their associated object types."""
    index_access = IndexAccess()
    images = index_access.retrieve_index()

    for image_path, labels in images.items():
        labels_str = ','.join(labels)
        print(f"{image_path}: {labels_str}")
    print(f"{len(images)} images found.")

if __name__ == '__main__':
    main()