import ctypes
from PIL import Image, ImageFont, ImageDraw
from os import path
import numpy as np
import json
import datetime
import random
import colorsys

for nn in range(5):
    image = Image.open("kebiao/课表-{}.PNG".format(str(nn+1))).convert('RGBA')
    # image.show()
    img_arr = np.asarray(image, dtype=np.double)
    # print(img_arr)
    src_clr=(199., 237., 204.,255.)
    dst_clr=(0,0,0,0)

    dst_arr = img_arr.copy()

    for i in range(img_arr.shape[1]):
        for j in range(img_arr.shape[0]):
            
            if (img_arr[j][i] == src_clr)[0] == True:
                # print('y')
                dst_arr[j][i] = dst_clr

    img_alarr=np.asarray(dst_arr, dtype=np.uint8)
    img_alpha = Image.fromarray(img_alarr.astype('uint8')).convert('RGBA')
    img_alpha.save('kebiao/wallpaper-{}.png'.format(str(nn+1)))
    print(nn)
