# save point cloud data
# Fandi Shan 2020 Nov

import numpy as np

# this array is 2d
load_pts = np.loadtxt('/Users/shanfandi/Desktop/points.txt')
part_seg = np.loadtxt('/Users/shanfandi/Desktop/pred_np.txt')

# convert the point cloud data array to 3d
pts3d = load_pts.reshape(load_pts.shape[0], load_pts.shape[1] // 3, 3)
print(pts3d.shape)
print(part_seg.shape)

# create single point cloud txt
for i in range(0, pts3d.shape[0]):
    txt_path = '/Users/shanfandi/Desktop/car_pts/' + \
        str(i) + '.txt'
    np.savetxt(txt_path, pts3d[i])
for i in range(0, part_seg.shape[0]):
    txt_path = '/Users/shanfandi/Desktop/car_seg/' + \
        str(i) + '_seg.txt'
    np.savetxt(txt_path, part_seg[i])
