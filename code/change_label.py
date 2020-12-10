import os
from os import listdir, path
import numpy as np
import open3d as o3d

# change the label
# shapenet: roof 0, hood 1, wheel 2, body 3
# my dataset: roof 3, hood 1, wheel 2, body 0; exchange the label for body and roof
# Fandi Shan 2020 Nov.

path_str = '/Users/shanfandi/Desktop/scaled_data_labeled'  # your directory path
save_path = '/Users/shanfandi/Desktop/correct_labeled_car'
roof = []
body = []
txts = os.listdir(path_str)
for txt in txts:
    print(txt)
    if 'txt' in txt:
        txt_path = path_str + '/' + txt
        data = np.loadtxt(txt_path)
        # print(type(data[0][3]))
        #a = np.unique(data[:,3])
        # print(a)
        save_txt = save_path + '/' + txt
        new_txt = np.zeros_like(data)
        for i in range(0, data.shape[0]):
            if data[i][3] == 0:
                # xyz
                new_txt[i][0] = data[i][0]
                new_txt[i][1] = data[i][1]
                new_txt[i][2] = data[i][2]
                new_txt[i][3] = 11
                #new_txt[i][4] = data[i][4]
            if data[i][3] == 1:
                new_txt[i][0] = data[i][0]
                new_txt[i][1] = data[i][1]
                new_txt[i][2] = data[i][2]
                new_txt[i][3] = 9
                #new_txt[i][4] = data[i][4]
            if data[i][3] == 2:
                new_txt[i][0] = data[i][0]
                new_txt[i][1] = data[i][1]
                new_txt[i][2] = data[i][2]
                new_txt[i][3] = 10
                #new_txt[i][4] = data[i][4]
            if data[i][3] == 3:
                new_txt[i][0] = data[i][0]
                new_txt[i][1] = data[i][1]
                new_txt[i][2] = data[i][2]
                new_txt[i][3] = 8
                #new_txt[i][4] = data[i][4]
        np.savetxt(save_txt, new_txt)
        print('------ finish ------')
