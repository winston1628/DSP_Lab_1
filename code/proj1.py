# Before trying to construct hybrid images, it is suggested that you
# implement my_imfilter.m and then debug it using proj1_test_filtering.py

from my_imfilter import my_imfilter
from vis_hybrid_image import vis_hybrid_image
from normalize import normalize
from gauss2D import gauss2D
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import scipy

''' Setup '''
# read images and convert to floating point format
filename_1 = '../data/dog.bmp'
filename_2 = '../data/cat.bmp'
filename_3 = '../data/einstein.bmp'
filename_4 = '../data/marilyn.bmp'
I_1 = mpimg.imread(filename_1)
I_2 = mpimg.imread(filename_2)
I_3 = mpimg.imread(filename_3)
I_4 = mpimg.imread(filename_4)
I_1 = normalize(I_1)
I_2 = normalize(I_2)
I_3 = normalize(I_3)
I_4 = normalize(I_4)


fft_I_1 = abs(np.fft.fftshift(np.fft.fft2(np.sum(I_1, axis = 2))))
fft_I_2 = abs(np.fft.fftshift(np.fft.fft2(np.sum(I_2, axis = 2))))

# Several additional test cases are provided for you, but feel free to make
# your own (you'll need to align the images in a photo editor such as
# Photoshop). The hybrid images will differ depending on which image you
# assign as image1 (which will provide the low frequencies) and which image
# you asign as image2 (which will provide the high frequencies)

''' Filtering and Hybrid Image construction '''
cutoff_frequency = 7 # This is the standard deviation, in pixels, of the 
# Gaussian blur that will remove the high frequencies from one image and 
# remove the low frequencies from another image (by subtracting a blurred
# version from the original version). You will want to tune this for every
# image pair to get the best results.
gaussian_filter = gauss2D(shape=(cutoff_frequency*4+1,cutoff_frequency*4+1), sigma = cutoff_frequency)


#########################################################################
# TODO: Use my_imfilter create 'low_frequencies' and                    #
# 'high_frequencies' and then combine them to create 'hybrid_image'     #
#########################################################################
#########################################################################
# Remove the high frequencies from image1 by blurring it. The amount of #
# blur that works best will vary with different image pairs             #
#########################################################################
low_frequencies = my_imfilter(I_1, gaussian_filter)
low_frequencies_1 = my_imfilter(I_3, gaussian_filter)

############################################################################
# Remove the low frequencies from image2. The easiest way to do this is to #
# subtract a blurred version of image2 from the original version of image2.#
# This will give you an image centered at zero with negative values.       #
############################################################################
high_frequencies = I_2 - my_imfilter(I_2, gaussian_filter)
high_frequencies_1 = I_4 - my_imfilter(I_4, gaussian_filter)
high_frequencies = normalize(high_frequencies)
high_frequencies_1 = normalize(high_frequencies_1)
############################################################################
# Combine the high frequencies and low frequencies                         #
############################################################################
hybrid_image = normalize(low_frequencies + high_frequencies)
hybrid_image_1 = normalize(low_frequencies_1 + high_frequencies_1)

''' Visualize and save outputs '''
plt.figure(1)
plt.imshow(low_frequencies)
plt.figure(2)
plt.imshow(high_frequencies)
vis = vis_hybrid_image(hybrid_image)
plt.figure(3)
plt.imshow(vis)
plt.figure(4)
plt.imshow(low_frequencies_1)
plt.figure(5)
plt.imshow(high_frequencies_1)
vis_1 = vis_hybrid_image(hybrid_image_1)
plt.figure(6)
plt.imshow(vis_1)

#plt.figure(4)
#plt.hist(fft_I_1, bins = 'auto')
#plt.figure(5)
#plt.hist(fft_I_2, bins = 'auto')
plt.imsave('../results/image/low_frequencies.png', low_frequencies, 'quality', 95)
plt.imsave('../results/image/high_frequencies.png', high_frequencies, 'quality', 95)
plt.imsave('../results/image/hybrid_image.png', hybrid_image, 'quality', 95)
plt.imsave('../results/image/hybrid_image_scales.png', vis, 'quality', 95)
plt.imsave('../results/image/low_frequencies_ex.png', low_frequencies_1, 'quality', 95)
plt.imsave('../results/image/high_frequencies_ex.png', high_frequencies_1, 'quality', 95)
plt.imsave('../results/image/hybrid_image_ex.png', hybrid_image_1, 'quality', 95)
plt.imsave('../results/image/hybrid_image_scales_ex.png', vis_1, 'quality', 95)
plt.show()