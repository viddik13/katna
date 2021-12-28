import argparse

import os.path
import cv2
from Katna.image import Image
from Katna.writer import ImageCropDiskWriter

 # Extract specific number of key frames from video

def main(image_file_path, crop_width, crop_height, output_folder_cropped_image):
    img_module = Image()

    # number of images to be returned
    no_of_crops_to_returned = 3

    # Filters
    # filters = ["text"]
    # Image file path
    # image_file_path = os.path.join(".", "tests", "data", "bird_img_for_crop.jpg")
    print(f"image_file_path = {image_file_path}")

    # diskwriter to save crop data
    diskwriter = ImageCropDiskWriter(location=output_folder_cropped_image)

    # crop the image and process data with diskwriter instance
    if os.path.isfile(image_file_path): # Does bob.txt exist?  Is it a file, or a directory?
        img_module.crop_image(
            file_path=image_file_path,
            crop_width=crop_width,
            crop_height=crop_height,
            num_of_crops=no_of_crops_to_returned,
            writer=diskwriter,
            # filters=filters,
            down_sample_factor=8
        )
    elif os.path.isdir(image_file_path):
        img_module.crop_image_from_dir(
            dir_path=image_file_path,
            crop_width=crop_width,
            crop_height=crop_height,
            num_of_crops=no_of_crops_to_returned,
            writer=diskwriter,
            # filters=<filters>,
            down_sample_factor=8
        )
    else:
        print("Error: input path not a file or directory?")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Image smart crop")
    parser.add_argument("image_file_path", type=str, help="Input image or directory of images path")
    parser.add_argument("crop_width", type=int, help="Crop width")
    parser.add_argument("crop_height", type=int,  help="Crop height")
    parser.add_argument("out_folder", type=str,  help="Crop height")
    parser.add_argument("-n", "--number-of-hints", type=int, default=1,
        help="Number of crops to produce for each image"
    )

    args = parser.parse_args()

    main(args.image_file_path, args.crop_width, args.crop_height, args.out_folder)
