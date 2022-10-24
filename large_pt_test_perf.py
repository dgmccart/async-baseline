#script to access an example of large points data;
#determine data size (MB, GB, etc.), shape (e.g. 1024 x 1024 x 3), and element type (e.g. uint16);
#display the image in napari

import fsspec, zarr
import dask.array as da
import napari
import os
import numpy as np

##block to be modified to access different data
import pooch
import csv
import numpy as np

"""
Simulated Data
"""

np.random.seed(0)
n = 10_000_000
data = 1000 * np.random.rand(n, 3)

##end of block to be modified to access different data

#calculate and print element type (e.g. uint16), data size (MB, GB, etc.), shape (e.g. 1024 x 1024 x 3)
num = data.dtype
print(num)

size = data.nbytes
mb = size * (9.5367432 * 10**(-7))
gb = size * (9.3132 * 10**(-10))

print(size)
print(mb)
print(gb)

shape = data.shape
print(shape)

# Load image into the viewer [EDIT FOR NEW DATA]
viewer = napari.view_points(data)

napari.run()
