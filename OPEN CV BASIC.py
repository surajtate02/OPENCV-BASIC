#-------->>>>...OPENCV(COMPUTER VISION...<<<<<--------------

#Images ProcessingUsing Open Cv
# 1. Image Basic

# Q.what is image?
# there are three type image
#1. Black(0) & White(1) image
#2. gray scale(range 0 to 255)
#3. colour image(RGB We give range 0 to 255 three times bez RGB(0 to 255)

# Q.images Resolution?
# def. resolution saying how many pixal in sheet or image. how much resolution
# 1.Full HD -1920(y-axis)*1080(x-axis)
# 2. HD - 1320*720
# 3. ultra HD - 3800*2100
#------------>>>>>>>>>>>|||||<<<<<<<<<<<<<<<<<<<---------------------------------

# 2.Reading Images
# Q. How to create an image writing opencv

# import cv2
# import numpy as np
# reading images
# img = cv2.imread("image9.png")
# #image type
# print(type(img))

# #print img shape
# print(img.shape)
# Ans (463, 356, 3) 463*356 menas image resolution & 3 means 3 channal bexz RGB channel
# # disply image

# cv2.imshow("Suraj_Tate Showing Image", img)

# # we doing window delay 0 means infinite
# cv2.waitKey(0)

#--------------------->>>>>>>>>||||<<<<<<<<<<<<<-----------------

# # 3.Coverting It RGB To Grayscale
# # Q. How To Covert RGB To Grayscale image
# import cv2
# import numpy as np
#
# img = cv2.imread("image9.png")
#
# # cvtcolour is function to use converting image
# # we seeing every where RGB format but in a opencv codeing BGR channel is there
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# print(img_gray.shape)
# #(512, 512) means only one channel bcz This Is Gray Scale Image
# cv2.imshow("Coverted RGB To Grayscale image ", img_gray)
# cv2.waitKey(0)

#-------------->>>>>>>>>>>>>>>|||||<<<<<<<<<<<<----------------

# 4. Playing With RGB Colour Channels
# import cv2
# import numpy as np
#
# img = cv2.imread("image9.png")
#
# # BGR2GRAY we have green & red. we gived blue for 0
# # 3d image    (: : this means all channel)
# img[:,:,0]=0 # 0 means BLUE
# # img[:,:,1]=0  # 1 means Green
# # img[:,:,2]=0  # 2 means red
#
# cv2.imshow("window", img)
# cv2.waitKey(0)

# OR
# import cv2
# import numpy as np
#
# img = cv2.imread("image9.png")
#
# imgBlue = img[:, :, 0]
# imgGreen = img[:,:,1]
# imgRed = img[:,:,2]
#
# new_img = np.hstack((imgBlue, imgGreen,imgRed))
#
# cv2.imshow("window", new_img)
# cv2.waitKey(0)
#-------------->>>>>>>>>>|||||<<<<<<<<<<<------------------
# 5. Resize image
#
# import cv2
# import numpy as np
#
# img = cv2.imread("image9.png")
# # resize function is use resize image in tuple format
#
# img_resize = cv2.resize(img,(256,256))
# print(img_resize.shape)
#
# cv2.imshow("window", img_resize)
# cv2.waitKey(0)

#---------------->>>>>>>>>>>>|||||||<<<<<<<<<<<<<<<<---------------

# # 6.Flipping An Image (Rotating Image)
#
# import cv2
# import numpy as np
#
# img = cv2.imread("image9.png")
#
# # flip method we have 3 value(0, 1, -1) 0 means vertical flip, 1 means horizontal  axis flip, -1 means combine effect horizantal & vertical
# img_flip = cv2.flip(img,-1)
#
# cv2.imshow("window", img_flip)
# cv2.waitKey(0)

#-------->>>>>>>>||||<<<<<<<<<<<-------------------
# 7. Cropping An Image

# import cv2
# import numpy as np
#
# img = cv2.imread("image9.png")
#
# # 100:300 means hight axis range & 200:500 means width axis range
# img_crop = img[100:300,200:500]
#
# cv2.imshow("window", img_crop)
# cv2.waitKey(0)

#---------->>>>>>>||||||||||<<<<<<<<<<<<----------------
# 7. save An Image

# import cv2
# import numpy as np
#
# img = cv2.imread("image9.png")
#
# img_crop = img[100:300,200:500]
# # save an image to imwrite function in open cv
# cv2.imwrite("new image.jpg", img_crop)
#
# cv2.imshow("window", img_crop)
# cv2.waitKey(0)

#---------->>>>>>>>>>>>||||<<<<<<<<<--------------------
#  8. Drawing Shapes ANd Text On Images (IMP)
# How to draw Rectangle in image or shape in image

# creating Own image

# import cv2
# import numpy as np
#
# # zeros is function
# img = np.zeros((512, 512, 3))
#
# # creating Own image and giving shape rectangle, circle , line, text
# # thikness means border thickness=0 menas only rectangle& -1 thickness means filled rectangle
# # rectangle
#
# cv2.rectangle(img, pt1=(100,100),pt2=(300,300), color=(255, 0, 0), thickness=-1)
# # circle
# cv2.circle(img, center=(100,400),radius=50, color=(0, 0, 255), thickness=-1)
# #line
# cv2.line(img,pt1=(0,0),pt2=(512,512),thickness=2,color=(0,255,0))
# #text
# cv2.putText(img,org=(100,100),fontScale=4,color=(0,255,255),thickness=2,lineType=cv2.LINE_AA,text="Hello",fontFace=cv2.FONT_ITALIC)
#
#
#
# cv2.imshow("window", img)
# cv2.waitKey(0)
#------------------->>>>>>>>>||||||||||||<<<<<<<<<------------------------------

# 11. Live Direct Drawing

import cv2
import numpy as np


def draw(event,x,y,flags,params):

    if event == 1:
        cv2.circle(img,center=(x,y),radius=50,color=(0,0,255),thickness=-1)


cv2.namedWindow(winname="window")
cv2.setMouseCallback("window",draw)


img = cv2.imread("image9.png")

while True:
    cv2.imshow("window",img)

    if cv2.waitKey(1) & 0xFF == ord('X'):
        break
cv2.destroyAllWindows()
