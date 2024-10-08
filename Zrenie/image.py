from PIL import Image
import numpy as np
image = Image.open('cat.png')
image.rotate(45,expand=True).show()



























# imageArray = np.asarray(image)
# for i in imageArray:
#     print(i)
# print(len(imageArray))

# image.crop((len(imageArray)/2-200,len(imageArray)/2-200,len(imageArray)-200,len(imageArray)-200)).show()







