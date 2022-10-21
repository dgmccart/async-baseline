#script to access an example of small points data;
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
This data comes from the Neurocyto Lab's description of the ThunderSTORM format.
This file format is used to represent single molecule localizations.

With respect to the napari async slicing work, this dataset is small enough that it performs well in synchronous mode.

If someone is interested, then you can use the uncertainty_xy attribute from the STORM data to change the point size.

More information is available here: http://www.neurocytolab.org/tscolumns/
"""

storm_path = pooch.retrieve(
    url='http://www.neurocytolab.org/wp-content/uploads/2018/06/ThunderSTORM_TS3D.csv',
    known_hash='665a28b2fad69dbfd902e4945df04667f876d33a91167614c280065212041a29',
)

with open(storm_path) as csvfile:
    data = list(csv.reader(csvfile))

data = np.array(data[1:]).astype(float)
data = data[:, 1:4]

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
