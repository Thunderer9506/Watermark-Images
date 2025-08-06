import cv2
from imwatermark import WatermarkEncoder

def watermark(path,dest_path = ""):
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
        cv2.imwrite(dest_path+'watermarked_image.png', watermarked_image)
        return True
    except Exception as e:
        return e