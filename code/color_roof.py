import numpy as np
import os
import re


def isRow(path):
    sub = 'car(.*)_roof.txt'
    a = re.findall(sub, path)
    result = int(a[0])
    return result


cars_path = '/Users/shanfandi/Desktop/roof'
cars = os.listdir(cars_path)
print(len(cars))
for car in cars:
    num = isRow(car)
    #seg_path = '/Users/shanfandi/Desktop/seg' + '/car' + str(num) + '_seg.txt'
    car_path = cars_path + '/' + car
    save_path = '/Users/shanfandi/Desktop/roof' + \
        '/car' + str(num) + '_roof_rgb.txt'
    f = np.loadtxt(car_path)
    # add 3 column in wheel.txt
    add_on = np.zeros_like(f)
    f = np.c_[f, add_on]
    print(f.shape)
    for i in range(0, f.shape[0]):
        f[i][3] = 255
        f[i][4] = 255
        f[i][5] = 0
    np.savetxt(save_path, f)
    print(car)
    print('------------- finish --------------')
