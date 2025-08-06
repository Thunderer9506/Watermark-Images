"""
watermark.py

Provides a function to add a digital watermark to an image using the imwatermark library.

Dependencies:
- cv2 (OpenCV)
- imwatermark

Functions:
- watermark(path, dest_path=""): Adds a watermark to the image at the given path and saves the result.
"""

import cv2
from imwatermark import WatermarkEncoder

def watermark(path, dest_path=""):
    """
    Adds a digital watermark to the image at the specified path.

    Parameters:
        path (str): Path to the input image file.
        dest_path (str, optional): Directory or prefix for saving the watermarked image.
                                   The output will be saved as 'watermarked_image.png' in this location.
                                   Defaults to the current directory.

    Returns:
        True if watermarking is successful.
        Exception object if an error occurs.

    Raises:
        ValueError: If the image cannot be loaded from the given path.
    """
    try:
        # Load the image
        bgr_image = cv2.imread(path)
        if bgr_image is None:
            raise ValueError(f"Could not load image from path: {path}")

        # Define the watermark text
        watermark_text = 'MySecretWatermark'

        # Initialize the encoder
        encoder = WatermarkEncoder()
        encoder.set_watermark('bytes', watermark_text.encode('utf-8'))

        # Encode the watermark using DWT-DCT method
        watermarked_image = encoder.encode(bgr_image, 'dwtDct')

        # Save the watermarked image
        cv2.imwrite(dest_path + 'watermarked_image.png', watermarked_image)
        return True
    except Exception as e:
        return