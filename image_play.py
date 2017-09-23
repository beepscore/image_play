# http://scikit-image.org/docs/dev/auto_examples/color_exposure/plot_adapt_rgb.html#sphx-glr-auto-examples-color-exposure-plot-adapt-rgb-py

import os
import matplotlib.pyplot as plt

# scikit-image package contains skimage
from skimage import color
from skimage import data
from skimage import filters
from skimage import io

data_in_dir = './data/in'
filename = os.path.join(data_in_dir, 'sun.jpg')
image = io.imread(filename)

# show unprocessed image
fig0 = plt.figure(figsize=(14, 7))
ax_each = fig0.add_subplot(121, adjustable='box-forced')
ax_each.imshow(image)
plt.show()

# http://scikit-image.org/docs/dev/user_guide/getting_started.html
# coins = data.coins()
# threshold_value = filters.threshold_otsu(coins)
# 107

# convert image to grayscale
gray_image = color.rgb2gray(image)

# show grayscale image
fig1 = plt.figure(figsize=(14, 7))
ax_each = fig1.add_subplot(121, adjustable='box-forced')
# https://stackoverflow.com/questions/39805697/skimage-why-does-rgb2gray-from-skimage-color-result-in-a-colored-image#45057729
ax_each.imshow(gray_image, cmap="gray")
plt.show()
