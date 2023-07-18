import argparse
import cv2
import os
import shutil

def compare_images(imageA, imageB):
    # Calculate the histograms of the images
    histA = cv2.calcHist([imageA], [0], None, [256], [0, 256])
    histB = cv2.calcHist([imageB], [0], None, [256], [0, 256])

    # Normalize the histograms
    histA = cv2.normalize(histA, histA).flatten()
    histB = cv2.normalize(histB, histB).flatten()

    # Calculate the correlation coefficient between the histograms
    similarity = cv2.compareHist(histA, histB, cv2.HISTCMP_CORREL)
    return similarity

def find_similar_images(input_image_path, folder_path, results_folder_path, move_images=True):
    # Load the input image
    input_image = cv2.imread(input_image_path)
    if input_image is None:
        print(f"Could not load input image: {input_image_path}")
        return

    print("Input image loaded successfully.")

    # Create the results folder if it doesn't exist
    if not os.path.exists(results_folder_path):
        os.makedirs(results_folder_path)

    print("Results folder created.")

    # Loop over the images in the folder
    for filename in os.listdir(folder_path):
        # Skip files that are not JPEG images
        if not (filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg")):
            continue

        # Construct the path to the image
        image_path = os.path.join(folder_path, filename)

        # Load the image
        image = cv2.imread(image_path)
        if image is None:
            print(f"Could not load image: {image_path}")
            continue

        print(f"Processing image: {image_path}")

        # Compare the input image to the image using histogram comparison
        similarity = compare_images(input_image, image)
        print(f"Similarity between {input_image_path} and {image_path}: {similarity}")

        # If the images are similar, move or copy the image to the results folder
        if similarity > 0.7:  # Adjust the threshold as needed
            destination_path = os.path.join(results_folder_path, filename)
            if move_images:
                shutil.move(image_path, destination_path)
                print(f"Moved {filename} to {destination_path}")
            else:
                shutil.copy(image_path, destination_path)
                print(f"Copied {filename} to {destination_path}")

if __name__ == "__main__":
    # Create the CLI parser
    parser = argparse.ArgumentParser(description="Find similar images based on content matching.")
    parser.add_argument("input_image", type=str, help="Path to the input image")
    parser.add_argument("folder_path", type=str, help="Path to the folder containing images to compare")
    parser.add_argument("results_folder", type=str, help="Path to the results folder")
    parser.add_argument("--copy", action="store_true", help="Copy similar images instead of moving them")

    # Parse the CLI arguments
    args = parser.parse_args()

    # Use the function with the CLI parameters
    find_similar_images(args.input_image, args.folder_path, args.results_folder, move_images=not args.copy)
