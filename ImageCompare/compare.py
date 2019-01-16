
# import the necessary packages
from skimage.measure import compare_ssim as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err
 
def compare_images(imageA, imageB, imageC, imageD, title):
	# compute the mean squared error and structural similarity index for the images
	
    
    # Original V. Original 
	m = mse(imageA, imageA)
	s = ssim(imageA, imageA)
 
	# Original V. Half
	m1 = mse(imageA, imageB)
	s1 = ssim(imageA, imageB)
    
	# Original V. Quarter
	m2 = mse(imageA, imageC)
	s2 = ssim(imageA, imageC)
    
	# Original V. SixPack
	m3 = mse(imageA, imageD)
	s3 = ssim(imageA, imageD)
    
    
    
	# setup the figure
	fig = plt.figure(title)
	plt.suptitle("Comparisons to Original Photo")

	# show first image
	ax = fig.add_subplot(2, 2, 1)
	ax.set_title("Original \n MSE: %.2f, SSIM: %.2f" % (m, s))
	plt.imshow(imageA, cmap = plt.cm.gray)
    
	plt.axis("off")
 
	# show the second image
	ax = fig.add_subplot(2, 2, 2)
	ax.set_title("Half Stitched \n MSE: %.2f, SSIM: %.2f" % (m1, s1))
	plt.imshow(imageB, cmap = plt.cm.gray)
	plt.axis("off")
    
    # show first image
	ax = fig.add_subplot(2, 2, 3)
	ax.set_title("Quarter Stitched \n MSE: %.2f, SSIM: %.2f" % (m2, s2))
	plt.imshow(imageC, cmap = plt.cm.gray)
	plt.axis("off")
 
	# show the second image
	ax = fig.add_subplot(2, 2, 4)
	ax.set_title("Sixpack Stitched \n MSE: %.2f, SSIM: %.2f" % (m3, s3))
	plt.imshow(imageD, cmap = plt.cm.gray)
	plt.axis("off")
 
	plt.tight_layout(pad=2.5, h_pad=1, w_pad=None, rect=None)
    
	# show the images
	plt.show()
    
    # load the images -- the original, the original + contrast,
# and the original + photoshop
original = cv2.imread("original.jpg")
half = cv2.imread("half.jpg")
quarter = cv2.imread("quarter.jpg")
sixpack = cv2.imread("sixpack.jpg")
 
# convert the images to grayscale
original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
half = cv2.cvtColor(half, cv2.COLOR_BGR2GRAY)
quarter = cv2.cvtColor(quarter, cv2.COLOR_BGR2GRAY)
sixpack = cv2.cvtColor(sixpack, cv2.COLOR_BGR2GRAY)


# initialize the figure
fig = plt.figure("Images")
images = ("Original", original), ("Half", half), ("Quarter", quarter), ("Six-pack", sixpack)
 
'''
# loop over the images
for (i, (name, image)) in enumerate(images):
	# show the image
	ax = fig.add_subplot(1, 3, i + 1)
	ax.set_title(name)
	plt.imshow(image, cmap = plt.cm.gray)
	plt.axis("off")
 
# show the figure
plt.show()
'''
# compare the images
compare_images(original, half, quarter, sixpack, "Original vs. Original")

