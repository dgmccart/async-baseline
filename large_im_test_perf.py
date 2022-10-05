#script to access an example of large image data;
#determine data size (MB, GB, etc.), shape (e.g. 1024 x 1024 x 3), and element type (e.g. uint16);
#display the image in napari

import fsspec, zarr
import dask.array as da
import napari
import numpy as np

# access the root of the n5 container
group = zarr.open(zarr.N5FSStore('s3://sci-imaging-data-public/jrc_hela-2/jrc_hela-2.n5/', anon=True)) 

# s0 (highest resolution) through s5 (lowest resolution) are available,
zarr_array = group['em/fibsem-uint16/s2']
data = da.from_zarr(zarr_array, chunks=zarr_array.chunks)

#calculate and print element type (e.g. uint16), data size (MB, GB, etc.), shape (e.g. 1024 x 1024 x 3)
num = data.dtype
print(num)

size = zarr_array.nbytes
mb = size * (9.5367432 * 10**(-7))
gb = size * (9.3132 * 10**(-10))

print(size)
print(mb)
print(gb)

shape = data.shape
print(shape)

# Load image into the viewer
viewer = napari.view_image(data, contrast_limits=(18000, 40000))
napari.run()

#to run script with performance monitoring use the following command:
# NAPARI_PERFMON=INSERT_FILE_TREE_TO_JSON_FILE_WITH_FUNCTIONS python INSERT_NAME_OF_THIS_SCRIPT.py



