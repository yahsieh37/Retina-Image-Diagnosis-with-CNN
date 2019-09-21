## Image preprocessing


#### edge_detect.py

In this file, we implement edge detection on the image. Then enhance the image by adding the edge information on to the original image.
User need to provide the path to original image files in the code. The generated new images will be saved to the corresponding folder.

#### upsampling.py

In this file, we provide the method to do upsampling.
User can use this feature as another way of augmented the database.
User need to provide the path to original image files in the code. The generated new images will be saved to the corresponding folder.

#### contrast.m and histmatch.m
These two files are used to perform color normalization and contrast enhancement of images.
Use the following steps to run the code:
1. Open histmatch.m in MATLAB and make sure contrast.m and histmatch.m are in the same folder.
2. choose one image with good lightening condition and vivid color as the reference image from all the images in the dataset. Then write the path of the reference image into: "ref = imread('  ');"
3. Change the path here to your local path of the dataset: "path = fullfile('   ');"
4. The path for output images can be set here: "writepath = fullfile('  ',files(i).name);"
5. Run histmatch.m


## Different image mixed with weighting



#### image_join_adjust_p.py

In this file, we provide the method to mix the image by different weighting of differet source of image.
User can adjust the weighting of three source of images by the variable o_c_e.
e.g.,
o_c_e = (1, 0, 0) means use 100% first source of image.
o_c_e = (0.33, 0.33, 0.33) means we give the same weighting for three different sources.
User need to provide the path to different sources of image, and also the path to save the resulting image files in the code.


## Conventional method: background cancellation


#### background_cancelation.m

In this file, we implement basic background cancellation method to illustrate the bad perofrmance of this method on the retina image object detection task.
Background cancellation can be good if 1) we have moving object or 2) we have pre-set (e.g. green backwall) background.
But in our case we have neither.
User need to provide the path of original images that are used to generate background and perform background cancellation. The cancelled image will be output.