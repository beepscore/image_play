"""
===============
Contour finding
===============

We use a marching squares method to find constant valued contours in an image.
In ``skimage.measure.find_contours``, array values are linearly interpolated
to provide better precision of the output contours. Contours which intersect
the image edge are open; all others are closed.

The `marching squares algorithm
<http://www.essi.fr/~lingrand/MarchingCubes/algo.html>`__ is a special case of
the marching cubes algorithm (Lorensen, William and Harvey E. Cline. Marching
Cubes: A High Resolution 3D Surface Construction Algorithm. Computer Graphics
(SIGGRAPH 87 Proceedings) 21(4) July 1987, p. 163-170).

"""

# http://scikit-image.org/docs/dev/auto_examples/edges/plot_contours.html#sphx-glr-auto-examples-edges-plot-contours-py

import matplotlib.pyplot as plt
import os

from skimage import color
from skimage import io
from skimage import measure


data_in_dir = './data/in'
filename = os.path.join(data_in_dir, 'rocket.jpg')
image = io.imread(filename)

# convert image to grayscale
# https://stackoverflow.com/questions/27026866/convert-an-image-to-2d-array-in-python#27028142
gray_image = color.rgb2gray(image)
print('gray_image')
print(gray_image)

# Find contours at a constant level
# http://scikit-image.org/docs/0.8.0/api/skimage.measure.find_contours.html
level = 0.25
fully_connected = 'low'
contours = measure.find_contours(gray_image, level, fully_connected)

# Display the image and plot all contours found
fig, ax = plt.subplots()
ax.imshow(gray_image, interpolation='nearest', cmap=plt.cm.gray)

for n, contour in enumerate(contours):
    ax.plot(contour[:, 1], contour[:, 0], linewidth=2)

ax.axis('image')
ax.set_xticks([])
ax.set_yticks([])
plt.show()
