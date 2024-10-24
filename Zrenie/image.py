import cv2
from PIL import Image
from PIL import ImageFilter
import numpy as np

image = cv2.imread('PythonProjects/Zrenie/5.png')

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
hsv_image[:, :, 0] = np.clip(hsv_image[:, :, 0] + 30, 0, 180) 
hsv_image[:, :, 1] = np.clip(hsv_image[:, :, 1] * 1.5, 0, 255) 
hsv_image[:, :, 2] = np.clip(hsv_image[:, :, 2] + 50, 0, 255)
cv2.imshow('PythonProjects/Zrenie/5.png', hsv_image)
cv2.waitKey(0)
cv2.destroyAllWindows()




























# imageArray = np.asarray(image)
# for i in imageArray:
#     print(i)
# print(len(imageArray))

# image.crop((len(imageArray)/2-200,len(imageArray)/2-200,len(imageArray)-200,len(imageArray)-200)).show()







