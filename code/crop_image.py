

im = cv.imread('0.png', cv.CV_LOAD_IMAGE_GRAYSCALE)
'''
 Syntax: cv2.imread(path, flag)

Parameters:
path: A string representing the path of the image to be read.
flag: It specifies the way in which image should be read. It’s default value is cv2.IMREAD_COLOR

https://docs.opencv.org/3.4.10/d4/da8/group__imgcodecs.html
'''
(thresh, im_bw) = cv.threshold(im, 128, 255, cv.THRESH_OTSU)
'''
Python: cv2.threshold(src, thresh, maxval, type[, dst]) → retval, dst

C: double cvThreshold(const CvArr* src, CvArr* dst, double threshold, double max_value, int threshold_type)

Python: cv.Threshold(src, dst, threshold, maxValue, thresholdType) → None
    Parameters:	

        src – input array (single-channel, 8-bit or 32-bit floating point).
        dst – output array of the same size and type as src.
        thresh – threshold value.
        maxval – maximum value to use with the THRESH_BINARY and THRESH_BINARY_INV thresholding types.
        type – thresholding type (see the details below).

        https://docs.opencv.org/2.4/modules/imgproc/doc/miscellaneous_transformations.html?highlight=threshold#threshold
'''
im = cv.getRectSubPix(im_bw, (98, 33), (1, 1)) 
'''cv2.getRectSubPix(image, patchSize, center[, patch[, patchType]]) → patch
#cv.GetRectSubPix(src, dst, center) → None
Parameters:	

    src – Source image.
    patchSize – Size of the extracted patch.
    center – Floating point coordinates of the center of the extracted rectangle within the source image. The center must be inside the image.
    dst – Extracted patch that has the size patchSize and the same number of channels as src .
    patchType – Depth of the extracted pixels. By default, they have the same depth as src .

    #https://docs.opencv.org/2.4/modules/imgproc/doc/geometric_transformations.html'''


cv.imshow('Img', im)
''' Syntax: cv2.imshow(window_name, image)

Parameters:
window_name: A string representing the name of the window in which image to be displayed.
image: It is the image that is to be displayed.
https://www.geeksforgeeks.org/python-opencv-cv2-imshow-method/'''
cv.waitKey(0)
'''cv.CreateTrackbar(trackbarName, windowName, value, count, onChange) → None
    Parameters:	

        trackbarname – Name of the created trackbar.
        winname – Name of the window that will be used as a parent of the created trackbar.
        value – Optional pointer to an integer variable whose value reflects the position of the slider. Upon creation, the slider position is defined by this variable.
        count – Maximal position of the slider. The minimal position is always 0.
        onChange – Pointer to the function to be called every time the slider changes position. This function should be prototyped as void Foo(int,void*); , where the first parameter is the trackbar position and the second parameter is the user data (see the next parameter). If the callback is the NULL pointer, no callbacks are called, but only value is updated.
        userdata – User data that is passed as is to the callback. It can be used to handle trackbar events without using global variables.
'''

