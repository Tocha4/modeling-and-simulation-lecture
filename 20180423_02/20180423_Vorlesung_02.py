import numpy as np
import matplotlib.pyplot as plt
import time
import imageio
import cv2
import os

a = np.random.rand(100,200)*255
a = np.array(a, dtype=np.uint8)
images = []

for i in range(len(a[0])):
    a[:,i] = 2
#    plt.cla()
#    plt.imshow(a , cmap='Greys' )
#    plt.pause(0.0001)
    
    if i % 10 == 0:
        cv2.imwrite('./images/2d_{}.png'.format(i+100), a)
        


files = os.listdir('./images')
files = sorted(files)
for f in files:
    img = imageio.imread('./images/{}'.format(f))
    images.append(img)

imageio.mimsave('2D_mold.gif', images, duration=1)


