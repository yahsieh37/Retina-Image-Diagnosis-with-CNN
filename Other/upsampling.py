import dippykit as dip
import numpy as np
import matplotlib.pyplot as plt
import os

path = "/Users/chuchu/Dropbox/gt_exp/ddb1_fundusimages/"  # Change the path to where you store the images
modes = [2, 3, 4]
for m in range(len(modes)):
    dir = 'upsample_img/'+str(modes[m]);
    if not os.path.exists(dir):
        os.makedirs(dir)

for m in range(len(modes)):
    for filename in os.listdir(path):
        mode = modes[m]
        file_path = path + filename
        f = dip.im_read(file_path)  # read icmage
        f = dip.im_to_float(f)
        M = np.array([[1/mode, 0],
                      [0, 1/mode]])
        f_up_0 = dip.sampling.resample(f[:,:,0], M, interp= 'bilinear')
        f_up_1 = dip.sampling.resample(f[:, :, 1], M, interp='bilinear')
        f_up_2 = dip.sampling.resample(f[:, :, 2], M, interp='bilinear')
        h, l = f_up_0.shape
        f_up = np.zeros((h, l, 3))
        f_up[:,:,0] = f_up_0
        f_up[:, :, 1] = f_up_1
        f_up[:, :, 2] = f_up_2
        upsample_img = 'upsample_img/' + str(mode)+ '/' +filename[:-4] + '_up' + str(mode) + '.jpg'
        save_im = dip.float_to_im(f_up)
        dip.im_write(save_im, upsample_img)