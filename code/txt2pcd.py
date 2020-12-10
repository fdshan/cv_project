# convert txt file to pcd file, write a 11 lines header
# reference: https://www.pythonheidong.com/blog/article/169680/03724c3f50e37b3197ed/
import os

# save the xyz data, write header for pcd file


def txt2pcd(filename):
    xlist = []
    ylist = []
    zlist = []
    labelList = []
    with open(filename, 'r') as file_to_read:
        while True:
            lines = file_to_read.readline()
            if not lines:
                break
                pass
            x, y, z, label = [float(i) for i in lines.split(' ')]
            xlist.append(x)
            ylist.append(y)
            zlist.append(z)
            labelList.append(label)
    file_name = filename.split('/')
    name = file_name[-1][:-4]
    savefilename = name + ".pcd"
    savefilename = "/Users/shanfandi/Desktop/pcd_2048_labeled/" + savefilename
    if not os.path.exists(savefilename):
        f = open(savefilename, 'w')
        f.close()
    # write header
    with open(savefilename, 'w') as file_to_write:
        file_to_write.writelines(
            "# .PCD v0.7 - Point Cloud Data file format\n")
        file_to_write.writelines("VERSION 0.7\n")
        file_to_write.writelines("FIELDS x y z label\n")
        file_to_write.writelines("SIZE 4 4 4 4\n")
        file_to_write.writelines("TYPE F F F I\n")
        file_to_write.writelines("COUNT 1 1 1 1\n")
        file_to_write.writelines("WIDTH " + str(len(xlist)) + "\n")
        file_to_write.writelines("HEIGHT 1\n")
        file_to_write.writelines("VIEWPOINT 0 0 0 1 0 0 0\n")
        file_to_write.writelines("POINTS " + str(len(xlist)) + "\n")
        file_to_write.writelines("DATA ascii\n")
        for i in range(len(xlist)):
            file_to_write.writelines(
                str(xlist[i]) + " " + str(ylist[i]) + " " + str(zlist[i]) + " " + str(labelList[i]) + "\n")


#path = '/Users/shanfandi/Desktop/result_without_label'
path = '/Users/shanfandi/Desktop/scaled_data'
pcds = os.listdir(path)
for pcd in pcds:
    if 'txt' in pcd:
        filename = path + '/' + pcd
        txt2pcd(filename)
        print(filename)
