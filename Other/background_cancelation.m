%% Image files used to generate background
a1 = imread('/Users/chuchu/Dropbox/gt_exp/set2/train/image/image015.png');
a2 = imread('/Users/chuchu/Dropbox/gt_exp/set2/train/image/image016.png');
a3 = imread('/Users/chuchu/Dropbox/gt_exp/set2/train/image/image017.png');
a4 = imread('/Users/chuchu/Dropbox/gt_exp/set2/train/image/image018.png');
a5 = imread('/Users/chuchu/Dropbox/gt_exp/set2/train/image/image019.png');
a6 = imread('/Users/chuchu/Dropbox/gt_exp/set2/train/image/image020.png');

a = cat(4, a1,a2,a3,a4, a5, a6);
aa = mean(a, 4);

%% Image file that is going to perform background cancelation
b = imread('/Users/chuchu/Dropbox/gt_exp/set2/train/image/image016.png');

aaa = im2uint8(aa);
c = aaa - b ;

%% Output image files
imwrite(c, 'canceled_img.jpg');
imwrite(aaa, 'average_img.jpg');