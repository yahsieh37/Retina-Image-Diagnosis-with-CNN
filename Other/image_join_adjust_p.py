import dippykit as dip
import numpy as np
import matplotlib.pyplot as plt
import os

## Change the path to where you store the images
path_orgin = "/Users/chuchu/Dropbox/gt_exp/set2/train/image/"   # Original images
path_contrast = "/Users/chuchu/Dropbox/gt_exp/set2/train/image_contrast/"  # Color contrast enhanced images
path_edge = "/Users/chuchu/Dropbox/GT/1_sem/course/DIP6258/HW7/ch07_noise_estimation/enhance/"  # Edge enhanced images
##

## Change the path to where you want to save the resulting images
path_mix = "/Users/chuchu/Dropbox/gt_exp/set2/image_mix/"
##

o_c_e = [(1,    0,      0),
         (0,    1,      0),
         (0,    0,      1),
         (0.5,  0.25,   0.25),
         (0.25, 0.5,    0.25),
         (0.25, 0.25,   0.5),
         (0.33, 0.33,   0.33)]

dir = path_mix;
if not os.path.exists(dir):
    os.makedirs(dir)

for event in range(3,len(o_c_e)):
    dir = path_mix + 'event_' + str( o_c_e[event][0]) + '_' + str( o_c_e[event][1]) +  '_' + str( o_c_e[event][2]) ;
    if not os.path.exists(dir):
        os.makedirs(dir)
    for filename in os.listdir(path_orgin):
        path_image_origin = path_orgin + filename
        path_image_contrast = path_contrast + filename
        path_image_edge = path_edge + filename
        im_origin = dip.im_read(path_image_origin)  # read icmage
        im_contrast = dip.im_read(path_image_contrast)  # read icmage
        im_edge = dip.im_read(path_image_edge)  # read icmage

        im_mix = (im_origin * o_c_e[event][0] + im_contrast * o_c_e[event][1] + im_edge * o_c_e[event][2]).astype(np.uint8);


        save_name = dir +'/' + filename[:-4] + '.png';

        dip.im_write(im_mix, save_name)