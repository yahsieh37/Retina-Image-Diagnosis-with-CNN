# -*- coding: utf-8 -*-


def IOU(Reframe,GTframe):
    """
    计算两矩形 IOU，传入为均为矩形对角线，（x,y）  坐标。
    """
    x1 = Reframe[0]
    y1 = Reframe[1]
    width1 = Reframe[2]-Reframe[0]
    height1 = Reframe[3]-Reframe[1]

    x2 = GTframe[0]
    y2 = GTframe[1]
    width2 = GTframe[2]-GTframe[0]
    height2 = GTframe[3]-GTframe[1]

    endx = max(x1+width1,x2+width2)
    startx = min(x1,x2)
    width = width1+width2-(endx-startx)

    endy = max(y1+height1,y2+height2)
    starty = min(y1,y2)
    height = height1+height2-(endy-starty)

    if width <=0 or height <= 0:
        Acc_area = 0 # 重叠率为 0
        Prec_area = 0
    else:
        Area = width * height  # 两矩形相交面积
        Area1 = width1 * height1  # REF面积
        Area2 = width2 * height2  # TAR面积
        Acc_area = Area*1./(Area1+Area2-Area) # IOU公式
        Prec_area = Area * 1. / Area2  # 更改后的IOU
    # return IOU
    return Acc_area, Prec_area


if __name__ == "__main__":
    Reframe1 = [0, 0, 10, 10]
    Reframe2 = [10, 10, 100, 100]
    GTframe = [5, 5, 15, 15]
    IOU1 = IOU(Reframe1, GTframe)
    IOU2 = IOU(Reframe2, GTframe)
    print(IOU1)
    print(IOU2)

    # 更改后的总IOU
    IOU_all = IOU1 + IOU2
    print(IOU_all)