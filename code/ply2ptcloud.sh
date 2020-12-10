#!/bin/bash
# get the file name
files=$(ls meshply)
postfix='ptcloud.pcd'
meshdir='./meshply'
ptcdir='./ptcloud'
for file in ${files}
do
	echo ${ptcdir}/${file%_*}_${postfix}
	# pcl_mesh2pcd <.ply file> <.pcd file>
	pcl_mesh2pcd ${meshdir}/${file} ${ptcdir}/${file%_*}_${postfix} -no_vis_result

done