import glob
import numpy as np
import cv2
import os
x=os.listdir("silh/")
y=len(x)

path = "ad/001-nm-01-036-*.png"
X=np.zeros((128, 88))
GEI = np.zeros((128,88), np.uint8)
for bb,file in enumerate (glob.glob(path)):
    image = cv2.imread(file)
    image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    img_resize = cv2.resize(image, dsize=(88, 128), interpolation=cv2.INTER_CUBIC)
    height, width = img_resize.shape
    for j in range(height):
        for i in range(width):
            X[j,i]=X[j,i]+img_resize[j,i]
    cv2.imwrite('AB/{}.png'.format(bb),img_resize)

for j in range(height):
    for i in range(width):
        GEI[j,i]=X[j,i]/y

cv2.imwrite('A.png',GEI)