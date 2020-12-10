import os
import numpy as np
import open3d as o3d
import h5py

# convert our txt data file into h5 file, make sure the format is same as shapenet h5 file
# 'data' --> n*2048*3
# 'label' --> n*1
# 'pid' --> n*2048
# car, label --> 3
# for each part, the pid is
# roof --> 8
# hood --> 9
# wheel --> 10
# body --> 3


# txt file path, store all the car data and segmentation label
path = '/Users/shanfandi/Desktop/correct_labeled_car'
cars = os.listdir(path)
data = []
alldata = []
label = np.zeros([160, 1])
pid = np.zeros([160, 2048])
#count = 0
for car in cars:
    if 'txt' in car:
        print(car)
        car_path = path + '/' + car
        # load the data
        car_data = np.loadtxt(car_path)
        # x, y, z, pid
        data = car_data.T[0:4]
        data = data.T
        alldata.append(data)

output = np.vstack(alldata)
print(output.shape)
output = output.reshape(-1, 2048, 4)
print(output.shape)
for i in range(160):
    label[i] = 3

print(np.unique(label))
f = h5py.File('/Users/shanfandi/Desktop/my_dataset_test.h5', 'w')
f['data'] = output[:, :, 0:3]
f['label'] = label
f['pid'] = output[:, :, 3]


'''
imgData = np.zeros((30, 3, 128, 256))
f = h5py.File('/Users/shanfandi/Desktop/test.h5', 'w')  # 创建一个h5文件，文件指针是f
f['data'] = imgData  # 将数据写入文件的主键data下面
f['labels'] = range(100)  # 将数据写入文件的主键labels下面
f.close()
'''
