import os
import numpy as np
import pandas
import open3d as o3d
from sklearn.decomposition import PCA
import pcl


def save_nppcd(np_pcd, save_dir, save_normals=False, save_xyz=False):
		f=open(save_dir,'w+')
		if not save_xyz:
			f.write("# .PCD v0.7 - Point Cloud Data file format\n")
			f.write("VERSION 0.7\n")
			if save_normals:
				f.write("FIELDS x y z normal_x normal_y normal_z\n")
				f.write("SIZE 4 4 4 4 4 4\n")
				f.write("TYPE F F F F F F\n")
				f.write("COUNT 1 1 1 1 1 1\n")
			else:
				f.write("FIELDS x y z\n")
				f.write("SIZE 4 4 4\n")
				f.write("TYPE F F F\n")
				f.write("COUNT 1 1 1\n")
			f.write("WIDTH "+str(np_pcd.shape[0])+"\n")
			f.write("HEIGHT 1\n")
			f.write("VIEWPOINT 0 0 0 1 0 0 0\n")
			f.write("POINTS "+str(np_pcd.shape[0])+"\n")
			f.write("DATA ascii\n")
			f.close()
			save_points(np_pcd, save_dir)
		else:
			save_points(np_pcd, save_dir)
		f.close()
		
def save_points(np_pcd, save_dir):
  f_ = open(save_dir, 'a')
  for point in np_pcd:
     f_.write( str(np.float32(point[0])) + ' ' + str(np.float32(point[1])) + ' ' + str(np.float32(point[2])) + '\n')
  f_.close()





j=0
os.chdir('/Users/adamszekely/primitive_shapes_generator/clean/boxes')
for f in os.listdir():
      if f.endswith(".pcd"):
       j=j+1
       pcd_before = pcl.load(f)
       pca = PCA(n_components=3)
       pca.fit(pcd_before)
       pcd_after=pca.fit_transform(pcd_before)
       save_points(pcd_after, "/Users/adamszekely/primitive_shapes_generator/Aligned_shapes/boxes/aligned"+str(j)+".pcd")
       save_nppcd(pcd_after, "/Users/adamszekely/primitive_shapes_generator/Aligned_shapes/boxes/aligned"+str(j)+".pcd", save_normals=False, save_xyz=False)
       

k=0
os.chdir('/Users/adamszekely/primitive_shapes_generator/clean/spheres')
for f in os.listdir():
      if f.endswith(".pcd"):
       k=k+1
       pcd_before = pcl.load(f)
       pca = PCA(n_components=3)
       pca.fit(pcd_before)
       pcd_after=pca.fit_transform(pcd_before)
       save_points(pcd_after, "/Users/adamszekely/primitive_shapes_generator/Aligned_shapes/spheres/aligned"+str(k)+".pcd")
       save_nppcd(pcd_after, "/Users/adamszekely/primitive_shapes_generator/Aligned_shapes/spheres/aligned"+str(k)+".pcd", save_normals=False, save_xyz=False)



i=0
os.chdir('/Users/adamszekely/primitive_shapes_generator/clean/cylinders')
for f in os.listdir():
      if f.endswith(".pcd"):
       i=i+1
       pcd_before = pcl.load(f)
       pca = PCA(n_components=3)
       pca.fit(pcd_before)
       pcd_after=pca.fit_transform(pcd_before)
       save_points(pcd_after, "/Users/adamszekely/primitive_shapes_generator/Aligned_shapes/cylinders/aligned"+str(i)+".pcd")
       save_nppcd(pcd_after, "/Users/adamszekely/primitive_shapes_generator/Aligned_shapes/cylinders/aligned"+str(i)+".pcd", save_normals=False, save_xyz=False)





    
