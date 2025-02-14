# Assisting Retina Image Diagnosis with DNN-based Object Detection
## Final project for Gatech ECE 6258 - Digital Image Processing (Fall 2018)

This project aims at developing a CNN-based detector that automatically detect and label diabetic retinopathy symptoms in fundus retinal images. The report of this project can be found [here](https://github.com/yahsieh37/Retina-Image-Diagnosis-with-CNN/blob/master/Final_Report.pdf).

#### This readme file contains the brief introduction of each folder. More information can be found in the README.txt file in each folder.

#### darknet-master
This folder contains the C++ code for object detection training and testing using YOLO algorithm. It also contains the files that are required to train and test on our retina image dataset. See the README.txt file in the folder for usage instructions.

#### Dataset
This folder contains the retina images and the label files for YOLO training that we use in the project. The folder "Original" contains the original images from DIARETDB1 and IDRiD dataset (see the paper for more information about these datasets). The folder "Contrast_Enhanced" contains some retina images that perform color contrast enhancement. The folder "Edge_Enhanced" contains some retina images that perform edge enhancement using sobel filter.

#### Metrics
The folder contains the Python code we used to calculate the four different metrics for our retina images object detection results. More information about the metrics can be found in the paper.

#### Other
This folder contains the remaining codes that we used in our project, which include the tasks of image pre-processing, pre-processed images combining, and background cancellation. The .py files should be run on Python, and the .m files should be run on Matlab.
