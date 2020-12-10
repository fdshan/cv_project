# convert pcd to txt, delete the header
# here my pcd file header have 10 lines
# reference: https://blog.csdn.net/SGL_LGS/article/details/105962966

import os
from os import listdir, path
import numpy as np
import open3d as o3d

# pcd to txt, delete the header
path_str = '/Users/shanfandi/Desktop/labeled_pcd'  # your directory path
save_path = '/Users/shanfandi/Desktop/labeled_txt'
txts = os.listdir(path_str)
for txt in txts:
    print(txt)
    if 'pcd' in txt:
        with open(os.path.join(path_str, txt), 'r') as f:
            lines = f.readlines()

        with open(os.path.join(save_path, os.path.splitext(txt)[0] + ".txt"), 'w') as f:
                # ignore the header
            f.write(''.join(lines[10:]))
