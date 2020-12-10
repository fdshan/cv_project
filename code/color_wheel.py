import numpy as np
import os
import re


def isRow(path):
    sub = 'car(.*)_wheel.txt'
    a = re.findall(sub, path)
    result = int(a[0])
    return result


cars_path = '/Users/shanfandi/Desktop/wheel'
cars = os.listdir(cars_path)
print(len(cars))
for car in cars:
    num = isRow(car)
    #seg_path = '/Users/shanfandi/Desktop/seg' + '/car' + str(num) + '_seg.txt'
    car_path = cars_path + '/' + car
    save_path = '/Users/shanfandi/Desktop/wheel' + \
        '/car' + str(num) + '_wheel_rgb.txt'
    f = np.loadtxt(car_path)
    # add 3 column in wheel.txt
    add_on = np.zeros_like(f)
    f = np.c_[f, add_on]
    print(f.shape)
    for i in range(0, f.shape[0]):
        f[i][3] = 0
        f[i][4] = 255
        f[i][5] = 255
    np.savetxt(save_path, f)
    print(car)
    print('------------- finish --------------')
