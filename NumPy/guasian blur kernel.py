import cv2
import numpy as np

# Step 1: Load an image
image = cv2.imread('mokshe.png')

# Step 2: Define a Gaussian kernel
kernel_size = 5
sigma = 2
kernel = cv2.getGaussianKernel(kernel_size, sigma)
gaussian_kernel = np.outer(kernel, kernel.transpose())

# Step 3: Perform convolution
blurred_image = cv2.filter2D(image, -1, gaussian_kernel)

# Step 4: Display or save the blurred image
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()