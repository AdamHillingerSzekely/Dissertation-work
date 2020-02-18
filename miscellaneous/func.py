import os
import numpy as np
import pandas
import open3d as o3d
import copy


pcd_load = o3d.io.read_point_cloud("b_001.pcd")
o3d.visualization.draw_geometries([pcd_load])
pcd_load = o3d.io.read_point_cloud("aligned2.pcd")
o3d.visualization.draw_geometries([pcd_load])