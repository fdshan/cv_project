# scale the data to match the ShapeNet format
# reference: https://blog.csdn.net/SGL_LGS/article/details/105962966

import os
import numpy as np


def change_scale(data):
    # centre
    xyz_min = np.min(data[:, 0:3], axis=0)
    xyz_max = np.max(data[:, 0:3], axis=0)
    xyz_move = xyz_min + (xyz_max - xyz_min) / 2
    data[:, 0:3] = data[:, 0:3] - xyz_move
    # scale
    scale = np.max(data[:, 0:3])
    scale = np.max(data[:, 0:3])
    data[:, 0:3] = data[:, 0:3] / scale
    return data[:, 0:3]


# scale the data
path_str = '/Users/shanfandi/Desktop/labeled_txt'  # your directory path
save_path = '/Users/shanfandi/Desktop/scaled_data'
txts = os.listdir(path_str)
for txt in txts:
    if 'txt' in txt:
        data_path = path_str + '/' + txt
        data = np.loadtxt(data_path)
        scaled = change_scale(data)
        name = save_path + '/' + txt
        np.savetxt(name, scaled)
        print(name)
