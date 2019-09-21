function J = contrast(RGB)

LAB = rgb2lab(RGB);
L = LAB(:,:,1)/100;
L = adapthisteq(L,'NumTiles',[8 8],'ClipLimit',0.005);
LAB(:,:,1) = L * 100;
J = lab2rgb(LAB);

end