import cv2
import numpy as np

def stitch_images(images):
    stitcher = cv2.createStitcher() if int(cv2.__version__[0]) < 4 else cv2.Stitcher_create()
    status, stitched = stitcher.stitch(images)
    if status == 0:
        return stitched
    else:
        print("Error during stitching")
        return None

images = [cv2.imread(f) for f in ['d_result_r0.jpg', 'd_result_r1.jpg']]
stitched_image = stitch_images(images)

if stitched_image is not None:
    cv2.imwrite('stitched_image.jpg', stitched_image)
