import cv2
import numpy as np
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
from django.core.files.uploadedfile import InMemoryUploadedFile

def detect_image(image):
    # Read the file content from the InMemoryUploadedFile object
    file_content = image.read()

    # Convert the file content to a NumPy array
    nparr = np.frombuffer(file_content, np.uint8)

    # Read the image using OpenCV
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Convert the image to BGRA color format (if it's not already)
    img1 = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

    # Display the image using Matplotlib
    plt.figure(figsize=(10, 10))
    plt.axis('off')
    plt.imshow(img)
    plt.show()
