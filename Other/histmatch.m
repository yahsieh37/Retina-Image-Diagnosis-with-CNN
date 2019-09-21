close all
clc
clear

ref = imread('image008.png');

path = fullfile('C:\Users\Kevin\Desktop\frcnn_matlab\diaretdb1_v_1_1\resources\images\ddb1_fundusimages');
files = dir(path);
files(1:2) = [];
totalfiles = numel(files);

im = {};
im_nor = {};
for i = 1:totalfiles
    im_path = fullfile(path, files(i).name);
    I = imread(im_path);
    J = imhistmatch(I,ref);
    
    J = imadjust(J,[0,0.9],[0,1]);
    J1 = contrast(J);
    
    writepath = fullfile('C:\Users\Kevin\Desktop\color_contrast',files(i).name);
    imwrite(J1,writepath);
end


