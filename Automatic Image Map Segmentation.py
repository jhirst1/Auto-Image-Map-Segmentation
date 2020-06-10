"""
=====================================
Automatic Image Map Segmentation
=====================================
:Author: kingboop
:Date: Sat Apr 13 15:05:02 2019

=====================================
Purpose
=====================================

In HTML, the <map> tag defines an image-map. An image-map
is an image with clickable areas. The idea behind
the image map is you should be able to perform different
actions depending on where in the image you click.

To create an image map you need an image and a map
containing some rules that describe the clickable areas.

Traditionally, users have to define coordinates themselves to 
be able to place the clickable areas onto the image.

However, depending on the size of the image and the number of
areas a user needs, this can be a time-consuming exercise. By
using the skimage library, some of that work can be automated.

By supplying an image to the 'image' variable and specifying 
the number of segments needed in the 'num_segments' variable, 
the coordinates of the image countours can be extracted and
the subsequent HTML map coorindates produced automatically.

"""

####Packages####

from skimage.segmentation import slic
from skimage import io
import numpy as np
import cv2
import imutils # pip install imutils
import os

####Custom Functions####

def convert2list(x): 
    res = (",".join(map(str, x))) 
    return res 

####Variable Assignment & initialisation####
    
loc= os.environ['USERPROFILE'] + r'\Desktop\\'
fn=r'sloth.png'
fn_out = r"Image Map Coords.txt"

image = io.imread(loc+fn)
numSegments = 40
coords = []

####Variable Assignment####

# apply SLIC and extract (approximately) the supplied number of segments
    #SLIC identifies numSegements shapes within the image
segments = slic(image, n_segments = numSegments, sigma = 0.5, compactness=50, max_iter=3)

# loop over the unique segment values
    #to extract the countours
for (i, segVal) in enumerate(np.unique(segments)):
    mask = np.zeros(image.shape[:2], dtype = "uint8")
    mask[segments == segVal] = 255 # the area that matches the original image, set area to white
    im2 = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
    cnts = imutils.grab_contours(im2)
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
    coords.append(cnts[0].flatten())

outF = open(loc+fn_out, "w")

for i in range(0,len(coords)):
    # write line to output file
        outF.write("<area shape='poly' coords='" + str(convert2list(coords[i].tolist())) + "' href=''>")
        outF.write("\n")
outF.close()