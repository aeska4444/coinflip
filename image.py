"""
Рендер за 300. положить катринку в папку из которой запускаешь, результат в images
"""
import numpy as np
from cv2.cv2 import imwrite
from PIL import Image
import os
from hamming import *

np.set_printoptions(threshold=np.inf, linewidth=np.inf)

exts = '.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tif'
images = []
dir = 'images'
os.makedirs(dir, exist_ok=True)

for file in os.listdir(os.getcwd()):
    if any(file.endswith(ext) for ext in exts):
        images.append(file)

for image in images:

    im_gray = np.array(Image.open(image).convert('L'))
    thresh = 128
    im_bool = im_gray > thresh
    maxval = 255
    im_bin = (im_gray > thresh) * maxval

    imwrite(os.path.join(dir, 'im_gray'+image), im_gray)
    imwrite(os.path.join(dir, 'im_bin'+image),  im_bin)

    maxval = 1
    im_bin = (im_gray > thresh) * maxval
    text_path = os.path.join(dir, image[:-4] + '.txt')
    print(im_bin, file=open(text_path, 'w'))
