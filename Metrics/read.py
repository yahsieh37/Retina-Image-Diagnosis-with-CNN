import re
import numpy as np
import IOU

F = open("results/set_225_5.txt","r") # Modify the file name to calculate metrics of different image set.
lines = F.readlines()

start_letter = []

W = 1500 # width of image
H = 1152 # height of image

for line in lines:
    # starts with
    # 'E': Enter image path
    # 'Har': Hard_exudates
    # 'O': Optical Disc
    # 'Hae': Haemor
    # 'M': Micro
    # 'S': Soft
    start_letter.append(line[0])

sepidx = []
for i, j in enumerate(start_letter):
    if j == 'E':
        sepidx.append(i)

avg_acc_area = 0
avg_prec_area = 0
avg_acc_case = 0
avg_prec_case = 0
for i in range(len(sepidx)-1):
    #print(sepidx[i])
    # cut a piece of the whole txt that related one image
    newimg = lines[sepidx[i]:sepidx[i+1]]

    optic_target_frame = np.array([[0, 0, 0, 0]])
    hard_target_frame = np.array([[0, 0, 0, 0]])
    Haemor_target_frame = np.array([[0, 0, 0, 0]])
    Micro_target_frame = np.array([[0, 0, 0, 0]])
    Soft_target_frame = np.array([[0, 0, 0, 0]])


    for line in newimg:
        if line[0]=='E':
            # new image
            num = re.findall(r'\d+', line)
            imagenum = num[2]
            #F1 = open(imagenum+".txt", "w")
            print("\nimg: ", imagenum)

            Ref = open('groundtruth\image'+imagenum+'.txt', 'r')
            reflines = Ref.readlines()
            ref_soft = np.array([[0, 0, 0, 0]])
            ref_hard = np.array([[0, 0, 0, 0]])
            ref_hae = np.array([[0, 0, 0, 0]])
            ref_opt = np.array([[0, 0, 0, 0]])
            ref_mic = np.array([[0, 0, 0, 0]])

            for refline in reflines:
                if refline[0]=='0': #Soft_Exudates
                    refnum = refline.split(' ')
                    #print(refnum)
                    x_center = float(refnum[1]) * W
                    y_center = float(refnum[2]) * H
                    width = float(refnum[3]) * W
                    height = float(refnum[4]) * H
                    frame_hae = np.array([[x_center-width/2, y_center-height/2, x_center+width/2, y_center+height/2]])
                    ref_soft = np.append(ref_soft, frame_hae, axis=0)

                if refline[0]=='1': #Microaneurysms
                    refnum = refline.split(' ')
                    x_center = float(refnum[1]) * W
                    y_center = float(refnum[2]) * H
                    width = float(refnum[3]) * W
                    height = float(refnum[4]) * H
                    frame_hae = np.array(
                        [[x_center - width / 2, y_center - height / 2, x_center + width / 2, y_center + height / 2]])
                    ref_mic = np.append(ref_mic, frame_hae, axis=0)

                if refline[0] == '2':  # Haemorrhages
                    refnum = refline.split(' ')
                    x_center = float(refnum[1]) * W
                    y_center = float(refnum[2]) * H
                    width = float(refnum[3]) * W
                    height = float(refnum[4]) * H
                    frame_hae = np.array(
                        [[x_center - width / 2, y_center - height / 2, x_center + width / 2, y_center + height / 2]])
                    ref_hae = np.append(ref_hae, frame_hae, axis=0)

                if refline[0] == '3':  # Hard_Exudates
                    refnum = refline.split(' ')
                    x_center = float(refnum[1]) * W
                    y_center = float(refnum[2]) * H
                    width = float(refnum[3]) * W
                    height = float(refnum[4]) * H
                    frame_hard = np.array(
                        [[x_center - width / 2, y_center - height / 2, x_center + width / 2, y_center + height / 2]])
                    ref_hard = np.append(ref_hard, frame_hard, axis=0)

                if refline[0] == '4':  # Optic
                    refnum = refline.split(' ')
                    x_center = float(refnum[1]) * W
                    y_center = float(refnum[2]) * H
                    width = float(refnum[3]) * W
                    height = float(refnum[4]) * H
                    frame_opt = np.array(
                        [[x_center - width / 2, y_center - height / 2, x_center + width / 2, y_center + height / 2]])
                    ref_opt = np.append(ref_opt, frame_opt, axis=0)


            ref_soft = ref_soft[1:ref_soft.shape[0], :]
            ref_hard = ref_hard[1:ref_hard.shape[0], :]
            ref_hae = ref_hae[1:ref_hae.shape[0], :]
            ref_opt = ref_opt[1:ref_opt.shape[0], :]
            ref_mic = ref_mic[1:ref_mic.shape[0], :]

            # print('ref_soft:', ref_soft)
            # print('ref_hard:', ref_hard)
            # print('ref_hae:', ref_hae)
            # print('ref_opt:', ref_opt)
            # print('ref_mic:', ref_mic)

# target frame starts
        if line[0]=='O':
            num = re.findall(r'\d+', line)
            left_x = int(num[1])
            top_y = int(num[2])
            width = int(num[3])
            height = int(num[4])
            right_x = left_x + width
            bottom_y = top_y + height
            frame = np.array([[left_x, top_y, right_x, bottom_y]])
            optic_target_frame = np.append(optic_target_frame, frame, axis=0)

        if line[0:3]=='Har':
            num = re.findall(r'\d+', line)
            left_x = int(num[1])
            top_y = int(num[2])
            width = int(num[3])
            height = int(num[4])
            right_x = left_x + width
            bottom_y = top_y + height
            frame = np.array([[left_x, top_y, right_x, bottom_y]])
            hard_target_frame = np.append(hard_target_frame, frame, axis=0)

        if line[0:3]=='Hae':
            num = re.findall(r'\d+', line)
            left_x = int(num[1])
            top_y = int(num[2])
            width = int(num[3])
            height = int(num[4])
            right_x = left_x + width
            bottom_y = top_y + height
            frame = np.array([[left_x, top_y, right_x, bottom_y]])
            Haemor_target_frame = np.append(Haemor_target_frame, frame, axis=0)

        if line[0:3]=='Mic':
            num = re.findall(r'\d+', line)
            left_x = int(num[1])
            top_y = int(num[2])
            width = int(num[3])
            height = int(num[4])
            right_x = left_x + width
            bottom_y = top_y + height
            frame = np.array([[left_x, top_y, right_x, bottom_y]])
            Micro_target_frame = np.append(Micro_target_frame, frame, axis=0)

        if line[0]=='S':
            num = re.findall(r'\d+', line)
            left_x = int(num[1])
            top_y = int(num[2])
            width = int(num[3])
            height = int(num[4])
            right_x = left_x + width
            bottom_y = top_y + height
            frame = np.array([[left_x, top_y, right_x, bottom_y]])
            Soft_target_frame = np.append(Soft_target_frame, frame, axis=0)

    optic_target_frame = optic_target_frame[1:optic_target_frame.shape[0], :]
    hard_target_frame = hard_target_frame[1:hard_target_frame.shape[0], :]
    Haemor_target_frame = Haemor_target_frame[1:Haemor_target_frame.shape[0], :]
    Micro_target_frame = Micro_target_frame[1:Micro_target_frame.shape[0], :]
    Soft_target_frame = Soft_target_frame[1:Soft_target_frame.shape[0], :]

    # print('tar optic: ', optic_target_frame)
    # print('tar hard: ', hard_target_frame)
    # print('tar haem: ', Haemor_target_frame)
    # print('tar micro: ', Micro_target_frame)
    # print('tar soft: ', Soft_target_frame)

    A_area_total = 0
    P_area_total = 0
    ref_count = 0
    tar_count = 0
    match_count = 0
    acc_count = 0
    #optic
    A_area, P_area = IOU.IOU(ref_opt[0], optic_target_frame[0])
    A_area_total = A_area_total + A_area
    P_area_total = P_area_total + P_area
    ref_count = ref_count + 1
    tar_count = tar_count + 1
    match_count = match_count + 1
    acc_count = acc_count + 1
    # print("Area_Accuracy of optic: ", A_area)
    # print("Area_Precision of optic: ", P_area)
    #hard
    score_a = 0
    score_p = 0
    avg_a = 0
    avg_p = 0
    num = 0
    for tar in hard_target_frame:
        for ref in ref_hard:
            A_area, P_area = IOU.IOU(ref, tar)
            score_a = score_a + A_area
            score_p = score_p + P_area
        # print("IOU of hard: ", score)
        avg_a = avg_a + score_a
        avg_p = avg_p + score_p
        num = num + 1
        score_a = 0
        score_p = 0

    if num!=0:
        A_area_total = A_area_total + avg_a/num
        P_area_total = P_area_total + avg_p/num
        tar_count = tar_count + 1
        if ref_hard.any():
            ref_count = ref_count + 1
            match_count = match_count + 1
            acc_count = acc_count + 1
        #print("Area_Accuracy of hard: ", avg_a/num)
        #print("Area_Precision of hard: ", avg_p / num)
        num = 0
    elif not ref_hard.any():
        acc_count = acc_count + 1
        #print("No H_Ex in reference.")
    else:
        ref_count = ref_count + 1
        #print("H_Ex_ref not detected.")

    # hae
    score_a = 0
    score_p = 0
    avg_a = 0
    avg_p = 0
    num = 0
    for tar in Haemor_target_frame:
        for ref in ref_hae:
            A_area, P_area = IOU.IOU(ref, tar)
            score_a = score_a + A_area
            score_p = score_p + P_area
        #print("IOU of hae: ", score)
        avg_a = avg_a + score_a
        avg_p = avg_p + score_p
        num = num + 1
        score_a = 0
        score_p = 0

    if num != 0:
        A_area_total = A_area_total + avg_a/num
        P_area_total = P_area_total + avg_p/num
        tar_count = tar_count + 1
        if ref_hae.any():
            ref_count = ref_count + 1
            match_count = match_count + 1
            acc_count = acc_count + 1
        #print("Area_Accuracy of hae: ", avg_a/num)
        #print("Area_Precision of hae: ", avg_p / num)
        num = 0
    elif not ref_hae.any():
        acc_count = acc_count + 1
        #print("No Hea in reference.")
    else:
        ref_count = ref_count + 1
        #print("Hea_ref not detected.")

    # soft
    score_a = 0
    score_p = 0
    avg_a = 0
    avg_p = 0
    num = 0
    for tar in Soft_target_frame:
        for ref in ref_soft:
            A_area, P_area = IOU.IOU(ref, tar)
            score_a = score_a + A_area
            score_p = score_p + P_area
        #print("IOU of soft: ", score)
        avg_a = avg_a + score_a
        avg_p = avg_p + score_p
        num = num + 1
        score_a = 0
        score_p = 0

    if num != 0:
        A_area_total = A_area_total + avg_a/num
        P_area_total = P_area_total + avg_p/num
        tar_count = tar_count + 1
        if ref_soft.any():
            ref_count = ref_count + 1
            match_count = match_count + 1
            acc_count = acc_count + 1
        print("Area_Accuracy of soft: ", avg_a/num)
        print("Area_Precision of soft: ", avg_p / num)
        num = 0
    elif not ref_soft.any():
        acc_count = acc_count + 1
        #print("No S_Ex in reference.")
    else:
        ref_count = ref_count + 1
        #print("S_Ex_ref not detected.")

    # micro
    score_a = 0
    score_p = 0
    avg_a = 0
    avg_p = 0
    num = 0
    for tar in Micro_target_frame:
        for ref in ref_mic:
            A_area, P_area = IOU.IOU(ref, tar)
            score_a = score_a + A_area
            score_p = score_p + P_area
        #print("IOU of micro: ", score)
        avg_a = avg_a + score_a
        avg_p = avg_p + score_p
        num = num + 1
        score_a = 0
        score_p = 0

    if num != 0:
        A_area_total = A_area_total + avg_a/num
        P_area_total = P_area_total + avg_p/num
        tar_count = tar_count + 1
        if ref_mic.any():
            ref_count = ref_count + 1
            match_count = match_count + 1
            acc_count = acc_count + 1
        print("Area_Accuracy of Micro: ", avg_a/num)
        print("Area_Precision of Micro: ", avg_p / num)
        num = 0
    elif not ref_mic.any():
        acc_count = acc_count + 1
        #print("No Mic in reference.")
    else:
        ref_count = ref_count + 1
        #print("Mic_ref not detected.")


    Acc_area = A_area_total/ref_count
    Prec_area = P_area_total/tar_count
    Acc_case = acc_count/5
    Prec_case = match_count/tar_count
    print("Area_Accuracy: ", Acc_area)
    print("Area_Precision: ", Prec_area)
    print("Case_Accuracy: ", Acc_case)
    print("Case_Precision: ", Prec_case)
    avg_acc_area = avg_acc_area + Acc_area
    avg_prec_area = avg_prec_area + Prec_area
    avg_acc_case = avg_acc_case + Acc_case
    avg_prec_case = avg_prec_case + Prec_case

print("\nAverage Area_Accuracy: ", avg_acc_area/20)
print("Average Area_Precision: ", avg_prec_area/20)
print("Average Case_Accuracy: ", avg_acc_case/20)
print("Average Case_Precision: ", avg_prec_case/20)
