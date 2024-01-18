'''
Aim: Create a hollow pointcloud cube
'''

# User inputs
size = 30 # m
step = 0.5 # m # trying 0.05 m for target and 0.5 m for source

# Library imports
import numpy as np
import open3d as o3d

# Create sample cloud
sample_cloud = []
for i in np.arange(-size, size, 2*size-step):
	for j in np.arange(-size, size, step):
		for k in np.arange(-size, size, step):
			sample_cloud.append([i, j, k])

for i in np.arange(-size, size, step):
	for j in np.arange(-size, size, 2*size-step):
		for k in np.arange(-size, size, step):
			sample_cloud.append([i, j, k])

for i in np.arange(-size, size, step):
	for j in np.arange(-size, size, step):
		for k in np.arange(-size, size, 2*size-step):
			sample_cloud.append([i, j, k])
points = np.array(sample_cloud, dtype=np.float32)
# print(type(points))
# print(points.shape)

# Create an open3d PointCloud object
point_cloud = o3d.geometry.PointCloud()
point_cloud.points = o3d.utility.Vector3dVector(points)

# Save the PointCloud to a PCD file
o3d.io.write_point_cloud('sample_point_cloud.pcd', point_cloud)
print('PCD file saved successfully.')
