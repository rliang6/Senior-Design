import imageio
import math
import numpy as np
from scipy import ndimage

fname = ''; //Type in the name of the video file that will be analyzed
vid = imageio.get_reader(fname);

for i, image in enumerate(vid): //Iterates through the frames of the video
    lp = ndimage.gaussian_filter(image, 3); //Creates a gaussian low-pass-filtered image
    g_hp = image - lp; //subtracts the gaussian filtered image with the frame to create a high pass filtered image
    g_hpsum = (g_hp.sum() - 255000000)/55000000; //uses the image values to estimate the number of cars
    g_hpsum = math.ceil(g_hpsum);
    print('Number of cars is %1.1f' % (g_hpsum)); // Need to make this save to a file
