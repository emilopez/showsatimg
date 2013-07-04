# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 11:34:20 2013

@author: emiliano
"""

import rasterIO
import numpy as np
#from mayavi import mlab
import matplotlib.pyplot as plt
import matplotlib.cm as cm
# ruta de la imagen
filename_img = '2000073-et.img'

file_pointer = rasterIO.opengdalraster(filename_img)
driver, XSize, YSize, proj_wkt, geo_t_params = rasterIO.readrastermeta(file_pointer)

# en data tengo la matriz que representa la imagen
data = rasterIO.readrasterband(file_pointer, 1)


data = data.astype(np.float32)
# Podria recortarla
#data = data[0:500, 1500:2000]
#Algunos Otros mapas de color: Greys_r,Blues, hsv
plt.imshow(data, cmap = cm.hot)
del data
plt.show()

#mlab.figure(size=(400, 320), bgcolor=(0.16, 0.28, 0.46))
#mlab.surf(data, colormap='hot')#,warp_scale=0.5) #vmin=1200, vmax=1610)
 

##mlab.view(-5.9, 83, 570, [5.3, 20, 238])
#mlab.show()