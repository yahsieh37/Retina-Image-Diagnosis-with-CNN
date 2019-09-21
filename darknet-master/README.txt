##
The YOLO code is downloaded from this link: git@github.com:AlexeyAB/darknet.git
A complete instruction about using the code can be found here: https://github.com/AlexeyAB/darknet

##
We run the code on PACE, an advanced computing environment at Georgia Tech with Linux system.
Below are some instruction for building and running the code on PACE.

### Compile
Module: cuda/9.1, cudnn/7.0.5, gcc/4.9.0, opencv/2.4.11 
Type "make" in the darknet-master directory, then an execution file "darknet" will appear.
The Makefile and several source files that require library paths in the src folder have been modified for the PACE system, they should be modified if building on different system. More detailed instruction about compiling can be found in the address on top of the file.

### Training
Module: cuda/9.1, cudnn/7.0.5
Type the following example instruction for training:
./darknet detector train build/darknet/x64/data/set_100_2.data cfg/yolo-diaretdb5.cfg weight_100_2/yolo-diaretdb5_3000.weights -dont_show

Files:
yolo-diaretdb5.cfg: The network file for training, it has been modified on anchor box number and size for training retina images.
Training image set: The images are seperated into five sets for cross-validation, there are also different image sets with different pre-processing weights. To train on different set of images, simply change the numbers in "set_100_2.data" and "weight_100_2". The first three numbers indicated the pre-processing weight, e.g. 100 indicates 1*(Original)+0*(Color)+0*(Edge) and 225 indicates 0.25*(Original)+0.25*(Color)+0.5*(Edge) (more information about pre-processing weights can be found in the paper). The last number indicates the image set for cross-validation.
yolo-diaretdb5_3000.weights: The training weight file. Each image set has their weight file in the corresponding weight folder, e.g. weight_100_2, make sure that the weight file name is correct when changing training image set. When training, the generated new weight file will be written to corresponding weight folder.

### Testing
Module: cuda/9.1, cudnn/7.0.5
(1) Type the following example instruction for detecting single image:
./darknet detector test build/darknet/x64/data/set_100_2.data cfg/yolo-diaretdb5.cfg weight_100_2/yolo-diaretdb5_3000.weights

After the module is loaded, enter the image file path (e.g. build/darknet/x64/data/set_100/image001.png) for detection. A result image "prediction.png" with detected bounding boxes will appear in the folder.

(2) Type the following example instruction for detecting multiple images:
./darknet detector test build/darknet/x64/data/set_100_2.data cfg/yolo-diaretdb5.cfg weight_100_2/yolo-diaretdb5_3000.weights -dont_show -ext_output < test_paths/test_100_2.txt > results/set_100_2.txt

A result file "set_100_2.txt" with detected bounding boxes coordinates for each image will appear in the folder "results". To test on different image set, change every file name that contain the number "100_2" to other number, e.g. 225_4 for image set 4 with pre-processing weight (0.25,0.25,0.5). Make sure that the weight file name is correct when changing testing image set.
More detailed instruction about training and testing images can be found in the address on top of the file.