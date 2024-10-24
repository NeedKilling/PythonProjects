import cv2
import numpy as np
from PIL import Image

img = Image.open('img/1.png')

width, height = img.size
print(width, height)

############################################

# new_image = img.resize((600, 1000))

# new_image.save('img/1(resize).png')


greenLights = cv2.imread('img/1(resize).png')

hsv_greenLights = cv2.cvtColor(greenLights, cv2.COLOR_BGR2HSV)
###############      ДИАПОЗОНЫ        ########################



# lower_red1 = np.array([0, 100, 100])
# upper_red1 = np.array([10, 255, 255])
# lower_red2 = np.array([160, 100, 100])
# upper_red2 = np.array([180, 255, 255])

# lower_yellow = np.array([20, 100, 100])
# upper_yellow = np.array([30, 255, 255])



lower_green = np.array([50, 100, 100])
upper_green = np.array([100, 255, 255])



lower_green2 = np.array([160, 100, 100])
upper_green2 = np.array([220, 255, 255])

#######################        МАСКИ        ################################

mask_green1 = cv2.inRange(hsv_greenLights, lower_green, upper_green)
# mask_green2 = cv2.inRange(hsv_greenLights, lower_green2, upper_green2)


filt_green = cv2.bitwise_and(greenLights, greenLights, mask = mask_green1) 

#filt_green = cv2.bitwise_or(mask_green1, mask_green2) не работает как надо

contours_green, _ = cv2.findContours(mask_green1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for contur in contours_green:
    x,y,w,h = cv2.boundingRect(contur)
    cv2.rectangle(greenLights, (x, y), (x + w, y + h), (0, 255, 0), 2)


cv2.imshow('img/1(resize).png', filt_green)

cv2.waitKey(0)                         
