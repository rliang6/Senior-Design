import imageio
import math
import numpy as np
from scipy import ndimage

fname = input('Please entire the video location: '); #Type in the name of the video file that will be analyzed
Car1 = input('What was the max number of cars? '); #For calibration purposes
Car0 = input('What was the min number of cars? '); #In the future this calibration method would be changed
vid = imageio.get_reader(fname);
g_hps = [];
min = 10000000000000;
max = 0;

for i, image in enumerate(vid): #Iterates through the frames of the video
    lp = ndimage.gaussian_filter(image, 3); #Creates a gaussian low-pass-filtered image
    g_hp = image - lp; #subtracts the gaussian filtered image with the frame to create a high pass filtered image
    g_hps.append(g_hp.sum());

for j in g_hps: #Finds the maximum and minimum edge values to calibrate.
    if (j < min):
        min = j;
    if (j > max):
        max = j;
    
x = [int(Car0), int(Car1)];
y = [min, max];
m,b = np.polyfit(x, y, 1); #Finds a linear relationship between number of cars and edges on the screen.

for h in g_hps: #Uses the relationship above to estimate the number of cars in the frame.
    ncar = (h - b)/m;
    ncar = math.ceil(ncar);
    print(ncar); #Change this to save/append the data in a file;
