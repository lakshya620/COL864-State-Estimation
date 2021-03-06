# Taken from https://theailearner.com/2018/10/15/creating-video-from-images-using-opencv-python/
import cv2
import numpy as np
import glob
 
img_array = []
for filename in glob.glob('beliefs/*.png'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
 
 
out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 2, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()