#script to access an example of small labels data;
#determine data size (MB, GB, etc.), shape (e.g. 1024 x 1024 x 3), and element type (e.g. uint16);
#display the layer in napari

import fsspec, zarr
import dask.array as da
import napari
import os
import numpy as np

##block to be modified to access different data
import pooch
from tifffile import imread

"""
This data comes from the MitoNet Benchmarks. I downloaded and accessed the data locally.

Six benchmark volumes of instance segmentation of mitochondria from diverse volume EM datasets
Narayan K , Conrad RW
DOI: https://dx.doi.org/10.6019/EMPIAR-10982

Data is stored at EMPIAR and can be explored here: https://www.ebi.ac.uk/empiar/EMPIAR-10982/

With respect to the napari async slicing work, this dataset is small enough that it performs well in synchronous mode.
"""

salivary_gland_mito = imread('salivary_gland_mito.tif')

##end of block to be modified to access different data

#calculate and print element type (e.g. uint16), data size (MB, GB, etc.), shape (e.g. 1024 x 1024 x 3)
num = salivary_gland_mito.dtype
print(num)

size = salivary_gland_mito.nbytes
mb = size * (9.5367432 * 10**(-7))
gb = size * (9.3132 * 10**(-10))

print(size)
print(mb)
print(gb)

shape = salivary_gland_mito.shape
print(shape)

# Load layer into the viewer [EDIT FOR NEW DATA]
viewer = napari.view_labels(salivary_gland_mito)
napari.run()

#to run script with performance monitoring use the following command:
# NAPARI_PERFMON=INSERT_FILE_TREE_TO_JSON_FILE_WITH_FUNCTIONS python INSERT_NAME_OF_THIS_SCRIPT.py

