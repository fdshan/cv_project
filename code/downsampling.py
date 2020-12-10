import os
from os import listdir, path
import numpy as np
import open3d as o3d

path = '/Users/shanfandi/Desktop/CV_project/ptcloud'
save_path = '/Users/shanfandi/Desktop/result'
cars = os.listdir(path)
for car in cars:
    if 'pcd' in car:
        each_car = path + '/' + car
        pcd = o3d.io.read_point_cloud(each_car)
        print(pcd)
        downpcd = pcd.voxel_down_sample(voxel_size=3)

        down_path = save_path + '/' + car
        o3d.io.write_point_cloud(down_path, downpcd)
        pcd2 = o3d.io.read_point_cloud(down_path)
        print(pcd2)
