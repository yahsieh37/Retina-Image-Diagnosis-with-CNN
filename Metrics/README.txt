### read.py
Run this file for calculating metrics of different sets of retina image detection results.

The result folder contains the result files of retina image detection using YOLO network. The file name indicates the image set that is used for detection. The first three numbers indicated the pre-processing weight, e.g. 100 indicates 1*(Original)+0*(Color)+0*(Edge) and 225 indicates 0.25*(Original)+0.25*(Color)+0.5*(Edge) (more information about pre-processing weights can be found in the paper). The last number indicates the image set for cross-validation. To calculate the metrics of different set of images, simply change the file name in the code.

The code will calculate and show four different metrics value for every images (more information about the metrics can be found in the paper).