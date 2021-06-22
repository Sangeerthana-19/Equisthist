import cv2
import matplotlib.pyplot as plt
import numpy
image = cv2.imread(r'C:\Users\sange\Downloads\pic1.jpg')

# Histogram Equalization
r,g,b = cv2.split(image)
cv2.imshow("channels",b )
eq_channels = []
for ch, color in zip(channels, ['B', 'G', 'R']):
    eq_channels.append(cv2.equalizeHist(ch))
eq_image = cv2.merge(eq_channels)
cv2.namedWindow("Original", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Equalized Image", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Original", image)
cv2.imshow("Equalized Image", eq_image)

#cv2.imwrite("Equalized_color_img", eq_image)

cv2.waitKey()
cv2.destroyAllWindows()
############
# Plot histogram for equalized image
# show Histogram
channels = ('b', 'g', 'r')
# we now separate the colors and plot each in the Histogram
for i, color in enumerate(channels):
    histogram = cv2.calcHist([eq_image], [i], None, [256], [0, 256])
    plt.plot(histogram, color=color)
    plt.xlim([0, 256])
plt.show()