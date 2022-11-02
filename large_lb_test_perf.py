#script to access an example of large labels data;
#determine data size (MB, GB, etc.), shape (e.g. 1024 x 1024 x 3), and element type (e.g. uint16);
#display the layer in napari

import fsspec, zarr
import dask.array as da
import napari
import numpy as np

##block to be modified to access different data

group = zarr.open(zarr.N5FSStore('s3://janelia-cosem-datasets/jrc_hela-2/jrc_hela-2.n5/labels', anon=True)) # access the root of the n5 container

# s0 (highest resolution) through s5 (lowest resolution) are available,
# so s3 is a suitable choice in the middle
zarr_array = group['endo_seg/s0']
data = da.from_zarr(zarr_array, chunks=zarr_array.chunks)

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

# Load layer into the viewer [EDIT FOR NEW DATA]
viewer = napari.view_labels(data)
napari.run()

#to run script with performance monitoring use the following command:
# NAPARI_PERFMON=INSERT_FILE_TREE_TO_JSON_FILE_WITH_FUNCTIONS python INSERT_NAME_OF_THIS_SCRIPT.py

