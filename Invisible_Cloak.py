import cv2
import numpy as np
import time

"""We are replacing the red colored pixels with the background pixels to create the invisible effect in the video. For doing this, we have to store the background image for each frame."""
#Reading from the webcam
cap=cv2.VideoCapture(0)

#Allowing the system to sleep for 3 seconds prior to starting the webcam
time.sleep(3)
count=0
background=0

#Capturing the red color that background in the range of 60
for i in range(60):
    #cap.read() returns a tuple (boolean,object) 
    #boolean value defines whether the reading was successfull
    #and the second item is the image i.e read
    ret,background=cap.read()
#Flipping the retrieved iamge
background=np.flip(background,axis=1)

"""
In this step, we will put our focus on detecting the red part in the image. We will convert the RGB (red-blue-green) to HSV(hue-saturation-value) because RGB values are highly sensitive to illumination. After the conversion of RGB to HSV, it is time to specify the range of color to detect red color in the video.
"""
#Reading each and every frame fromw webcam untill its open
while (cap.isOpened()):
    ret,image=cap.read()
    if not ret:   #if the return value is false (image not read)
        break  #Breaking the loop so that it discontinues reading from webcam
    count+=1 #Else increase the frame count by 1
    image=np.flip(image,axis=1)   #flip the image 

    #Converting the color space from BGR to HSV
    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

    #Generating masks to detect red color
    lower_red = np.array([0, 125, 50])
    upper_red = np.array([10, 255,255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)
    mask1 = mask1 + mask2


    #Open and dilate the mask image
