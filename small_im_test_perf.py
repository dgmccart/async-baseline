#script to access an example of large image data;
#determine data size (MB, GB, etc.), shape (e.g. 1024 x 1024 x 3), and element type (e.g. uint16);
#display the image in napari

import fsspec, zarr
import dask.array as da
import napari
import os
import numpy as np

##block to be modified to access different data
import pooch
from tifffile import imread

"""
This data comes from the MitoNet Benchmarks.

Six benchmark volumes of instance segmentation of mitochondria from diverse volume EM datasets
Narayan K , Conrad RW
DOI: https://dx.doi.org/10.6019/EMPIAR-10982

Data is stored at EMPIAR and can be explored here: https://www.ebi.ac.uk/empiar/EMPIAR-10982/

With respect to the napari async slicing work, this dataset is small enough that it performs well in synchronous mode.
"""

salivary_gland_em_path = pooch.retrieve(
    url='https://ftp.ebi.ac.uk/empiar/world_availability/10982/data/mito_benchmarks/salivary_gland/salivary_gland_em.tif',
    known_hash='222f50dd8fd801a84f118ce71bc735f5c54f1a3ca4d98315b27721ae499bff94',
)

salivary_gland_em = imread(salivary_gland_em_path)

##end of block to be modified to access different data

#calculate and print element type (e.g. uint16), data size (MB, GB, etc.), shape (e.g. 1024 x 1024 x 3)
num = salivary_gland_em.dtype
print(num)

size = salivary_gland_em.nbytes
mb = size * (9.5367432 * 10**(-7))
gb = size * (9.3132 * 10**(-10))

print(size)
print(mb)
print(gb)

shape = salivary_gland_em.shape
print(shape)

# Load image into the viewer [EDIT FOR NEW DATA]
viewer = napari.view_image(salivary_gland_em)
napari.run()

#to run script with performance monitoring use the following command:
# NAPARI_PERFMON=INSERT_FILE_TREE_TO_JSON_FILE_WITH_FUNCTIONS python INSERT_NAME_OF_THIS_SCRIPT.py


