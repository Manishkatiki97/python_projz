import cv2
img = cv2.imread("galaxy.jpg",0)
print(type(img))
print(img)
print(img.shape)
print(img.ndim)

# resize the image to fit in the screen
resized_image = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))

# to show the image 
cv2.imshow("Galaxy", resized_image)

# Write the resized image
# cv2.imwrite("galaxy_resized.jpg", resized_image)

# time to close the window in milli seconds
cv2.waitKey(2000)
cv2.destroyAllWindows()