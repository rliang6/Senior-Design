import imageio
import math
import numpy as np
from scipy import ndimage

fname = '/home/pi/Desktop/video_1.mp4';
vid = imageio.get_reader(fname);

for i, image in enumerate(vid):
    lp = ndimage.gaussian_filter(image, 3);
    g_hp = image - lp;
    g_hpsum = (g_hp.sum() - 255000000)/55000000;
    g_hpsum = math.ceil(g_hpsum);
    print('Mean of edge is %1.1f' % (g_hpsum)); // Need to make this save to a file
