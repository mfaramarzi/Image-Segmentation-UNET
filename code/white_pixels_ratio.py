#Count total number of white pixels in an image

img=cv2.imread(filename,1)
TP= width * height
white= TP - cv2.countNonZero(img[1])
print "Dimensions:", img.size, "Total pixels:", TP, "White", white

#####################

import cv2
image = cv2.imread("pathtoimg", 0)
count = cv2.countNonZero(image)
print(count)

################################################################




import cv2
import numpy as np

img = cv2.imread('img.png', cv2.IMREAD_GRAYSCALE)
n_white_pix = np.sum(img == 255)
print('Number of white pixels:', n_white_pix)


#or


map<Vec3b, int> palette;
for (int y = 0; y<im.rows; y++) {

for (int x = 0; x<im.cols; x++)
    {
        Vec3b color = im.at<Vec3b>(Point(x, y));
        if (palette.count(color) == 0)
        {
            palette[color] = 1;
        }
        else
        {
            palette[color] = palette[color] + 1;
        }
    }
}

#https://stackoverflow.com/questions/47494350/count-total-number-of-white-pixels-in-an-image-is-throwing-an-error