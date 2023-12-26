# reference link: https://www.tutorialkart.com/opencv/python/opencv-python-resize-image/#gsc.tab=0

# package command: pip install opencv-python

import cv2

source_path = "./demo.jpg"
destination_path = "newImage.png"
scale_percent = 60

# Read the source image
source = cv2.imread(source_path)

# Check if the image was successfully loaded
if source is None:
    print(f"Error: Unable to load the image from {source_path}")
else:
    # Calculate the new dimensions
    width = int(source.shape[1] * scale_percent / 100)
    height = int(source.shape[0] * scale_percent / 100)
    dim = (width, height)

    # Resize the image
    resized = cv2.resize(source, dim, interpolation=cv2.INTER_AREA)

    print('Resized Dimensions:', resized.shape)

    # Save the resized image
    cv2.imwrite(destination_path, resized)

    # Display the resized image
    cv2.imshow("Resized image", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
