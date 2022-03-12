##########################################################################
# Script to resize all the images in a given folder using the cv2 package
##########################################################################

import cv2
import os 
directory = "C:/Users/C-TNAG897/data_engineering_edu/python_projz/3_image_video_proc/sample_images"

for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        img = cv2.imread(f"./sample_images/{filename}",1)
        resized_img = cv2.resize(img, (100,100))
        cv2.imwrite(f"./sample_images/resized_{filename}", resized_img)


