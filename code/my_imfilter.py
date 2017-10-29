import numpy as np

def my_imfilter(image, filter):
	
	[filter_height, filter_width] = np.shape(filter)
	[height_image, width_image, channel] = np.shape(image)
	output_image = np.zeros_like(image)
	height_padding = filter_height//2
	width_padding = filter_width//2
	image_padding = np.zeros([height_image + 2 * height_padding, width_image + 2 * width_padding, channel])
	
	for i in range(channel):
		image_padding[:,:,i] = np.lib.pad(image[:,:,i], ((height_padding, height_padding), (width_padding, width_padding)), 'constant', constant_values = 0)

	for i in range(output_image.shape[1]):
		for j in range(output_image.shape[0]):
			output_image[j, i, 0] = np.sum(filter * image_padding[j:j + filter_height, i:i + filter_width, 0])
			output_image[j, i, 1] = np.sum(filter * image_padding[j:j + filter_height, i:i + filter_width, 1])
			output_image[j, i, 2] = np.sum(filter * image_padding[j:j + filter_height, i:i + filter_width, 2])

	return output_image