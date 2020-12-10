import numpy as np
import os
import re


def isRow(path):
    sub = 'car(.*).txt'
    a = re.findall(sub, path)
    result = int(a[0])
    return result


cars_path = '/Users/shanfandi/Desktop/data'
cars = os.listdir(cars_path)
print(len(cars))
for car in cars:
    num = isRow(car)
    seg_path = '/Users/shanfandi/Desktop/seg' + '/car' + str(num) + '_seg.txt'
    car_path = cars_path + '/' + car
    save_path_roof = '/Users/shanfandi/Desktop/roof' + \
        '/car' + str(num) + '_roof.txt'
    save_path_hood = '/Users/shanfandi/Desktop/hood' + \
        '/car' + str(num) + '_hood.txt'
    save_path_wheel = '/Users/shanfandi/Desktop/wheel' + \
        '/car' + str(num) + '_wheel.txt'
    save_path_body = '/Users/shanfandi/Desktop/body' + \
        '/car' + str(num) + '_body.txt'
    f = np.loadtxt(car_path)
    roof = []
    hood = []
    wheel = []
    body = []
    seg = np.loadtxt(seg_path)
    #add_on = np.zeros_like(f)
    #f = np.c_[f, add_on]
    print(f.shape)
    for i in range(0, seg.shape[0]):
        # roof
        if seg[i] == 0:
            roof.append(f[i])
            # hood
        if seg[i] == 1:
            hood.append(f[i])
            # wheels
        if seg[i] == 2:
            wheel.append(f[i])
            # body
        if seg[i] == 3:
            body.append(f[i])

    np.savetxt(save_path_roof, roof)
    np.savetxt(save_path_hood, hood)
    np.savetxt(save_path_wheel, wheel)
    np.savetxt(save_path_body, body)
    print(car)
    print('------------- finish --------------')
