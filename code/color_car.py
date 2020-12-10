# color body separately
# Fandi Shan 2020 Nov.
import numpy as np
import os
import re


def isRow(path):
    #sub = 'car(.*).txt'
    sub = 'car(.*).txt'
    a = re.findall(sub, path)
    result = int(a[0])
    return result


cars_path = '/Users/shanfandi/Desktop/car_pts'
cars = os.listdir(cars_path)
print(len(cars))
for car in cars:
    num = isRow(car)
    seg_path = '/Users/shanfandi/Desktop/car_seg' + \
        '/' + str(num) + '_seg.txt'
    car_path = cars_path + '/' + car
    save_path = '/Users/shanfandi/Desktop/rgb' + \
        '/car' + str(num) + '_rgb.txt'
    f = np.loadtxt(car_path)
    seg = np.loadtxt(seg_path)
    add_on = np.zeros_like(f)
    f = np.c_[f, add_on]
    print(f.shape)
    for i in range(0, seg.shape[0]):
        if seg[i] == 0:
            # roof
            # set it to yellow
            f[i][3] = 255
            f[i][4] = 255
            f[i][5] = 0
        if seg[i] == 1:
            # hood
            # set it to blue
            f[i][3] = 65
            f[i][4] = 105
            f[i][5] = 225
        if seg[i] == 2:
            # wheel
            # set it to green
            f[i][3] = 0
            f[i][4] = 255
            f[i][5] = 255
        if seg[i] == 3:
            # body
            # set it to pink
            f[i][3] = 255
            f[i][4] = 192
            f[i][5] = 203
    np.savetxt(save_path, f)
    print(car)
    print('------------- finish --------------')
