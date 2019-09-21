import dippykit as dip
import numpy as np
import matplotlib.pyplot as plt
import os
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

path = "/Users/chuchu/Dropbox/gt_exp/set2/train/image/"  # Change the path to where you store the images

#modes = ['sobel', 'sobel_h', 'sobel_v', 'canny', 'scharr', 'prewitt', 'roberts', 'laplace']
modes = ['sobel']
for mode in modes:
    dir = 'edge/'+mode;
    if not os.path.exists(dir):
        os.makedirs(dir)
    dir = 'enhance_edge/' + mode;
    if not os.path.exists(dir):
        os.makedirs(dir)

dir = 'edge/';
if not os.path.exists(dir):
    os.makedirs(dir)

dir = 'enhance/';
if not os.path.exists(dir):
    os.makedirs(dir)

for mode in modes:
    for filename in os.listdir(path):
        file_path = path + filename
        f = dip.im_read(file_path)           #read icmage
        f = dip.im_to_float(f)
        f_g = rgb2gray(f)
        f_edge = dip.transforms.edge_detect(f_g, mode = mode, as_bool=False);
        edgename = 'edge/' + filename[:-4] +  '.png';
        if mode is not 'canny':
            f_edge *= 1/f_edge.max()
        save_im = dip.float_to_im(f_edge)
        dip.im_write(save_im, edgename)

        f[:,:,0] += f_edge
        f[:, :, 1] += f_edge
        f[:, :, 2] += f_edge
        enhance_img = 'enhance/' + filename[:-4] +  '.png';
        save_im = dip.float_to_im(f)
        dip.im_write(save_im, enhance_img)

####combine all
#
# for filename in os.listdir(path):
#     file_path = path + filename
#     f = dip.im_read(file_path)  # read icmage
#     f = dip.im_to_float(f)
#     f_g = rgb2gray(f)
#     f_edge_all = np.zeros(f_g.shape)
#     for mode in modes:
#         f_edge = dip.transforms.edge_detect(f_g, mode=mode, as_bool=False);
#         if mode is not 'canny':
#             f_edge *= 1 / f_edge.max()
#         f_edge_all += f_edge
#
#     f[:, :, 0] += f_edge_all
#     f[:, :, 1] += f_edge_all
#     f[:, :, 2] += f_edge_all
#     enhance_img = 'enhance_all_img/' + filename[:-4] + '_' + mode + '.jpg'
#     save_im = dip.float_to_im(f)
#     dip.im_write(save_im, enhance_img)
