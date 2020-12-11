# Unreal Garage: Car Point Cloud Segmentation 

![mesh with pcd](https://github.com/fdshan/cv_project/blob/main/result/mesh_w_pcd.png)

## Intro 
* `code`: storaging all the codes for data processing
* `result`: visualized result after feeding our data into the point cloud segmentation networks
* `run_log`: training logs for all networks

## Part Segmentation networks
* [PointNet (2017)](https://github.com/charlesq34/pointnet) The first model that caught our attention is the PointNet, end-to-end learning for scattered and unordered point data. It has demonstrated a rich theoretical analysis and experimental results on point cloud segmentation and it is actually the first model that has been designed to be able to directly consume point clouds without transforming such data to regular 3-dimensional voxel grids or collections of images. Numerous models that have emerged later are pioneered by it. PointNet is a unified framework for various tasks including Object Classification, Object Part Segmentation and Semantic Scene Segmentation. After we trained the PointNet model by using our dataset combined with the ShapeNet car dataset, this is the training accuracy after we plotted in a line graph:
![PointNet](https://github.com/fdshan/cv_project/blob/main/result/Accuracy/pointnet.PNG)

* [PointNet++ (2017)](https://github.com/charlesq34/pointnet2) The same author has published another paper months after the PointNet. What they have realized is that sometimes the local features are not being appropriately captured from the original PointNet model. In other words, if we have a car model its orientation makes its wheels overlaid with each other, it will confuse the model to segment the correct wheel. PointNet++ resolves this issue by respecting spatial localities of all it’s input points. It learns hierarchical features with increasing scales of contexts. The author suggests running the model recursively on all the local features as much as possible. We can sample the points from the wheels and by repeating this process the model will eventually be able to precisely detect each wheel. Every set of information has been captured in the PointNet++. After we trained the PointNet++ model by using our dataset combined with the ShapeNet car dataset, this is the training accuracy after we plotted in a line graph:
![PointNet++](https://github.com/fdshan/cv_project/blob/main/result/Accuracy/pointnet%2B%2B.PNG)

* [PointCNN (2018)](https://github.com/yangyanli/PointCNN) The next model that caught our attention is PointCNN published in 2018. They have proposed to learn an X-transformation from the input points to simultaneously promote two causes:
1. The weighting of the input features associated with the points
2. The permutation of the points into a latent and potentially canonical order
After we trained the PointCNN model by using our dataset combined with the ShapeNet car dataset, this is the training accuracy after we plotted in a line graph:
![PointCNN](https://github.com/fdshan/cv_project/blob/main/result/Accuracy/pointcnn.PNG)

* [LDGCNN (2019)](https://github.com/KuangenZhang/ldgcnn) Both PointNet & PointNet++ have made tremendous impact on 3D-image processing. The LDGCNN(Linked Dynamic Graph CNN) published in 2019 classify and segment point cloud directly by removing the transformation network, link hierarchical features from dynamic graphs, freeze feature extractor, and retrain the classifier to increase the performance. It heavily borrowed the idea and code from PointNet and DGCNN. After we trained the LDGCNN model by using our dataset combined with the ShapeNet car dataset, this is the training accuracy after we plotted in a line graph:
![LDGCNN](https://github.com/fdshan/cv_project/blob/main/result/Accuracy/ldgcnn.PNG)

* [DGCNN (2019)](https://github.com/WangYueFt/dgcnn) The DGCNN (Dynamic Graph CNN) has the best accuracy on car part segmentation among all of the models that we have found. This paper published in 2019 was improved based on the PointNet. Instead of working on individual points like PointNet in which it neglects the geometric relationship among points, the DGCNN has proposed a simple operation called Edge Conv in which it captured local geometric structure and maintaining permutation invariance. After we trained the DGCNN model by using our dataset combined with the ShapeNet car dataset, this is the training accuracy after we plotted in a line graph:
![DGCNN](https://github.com/fdshan/cv_project/blob/main/result/Accuracy/dgcnn.PNG)

