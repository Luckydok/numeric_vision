import cv2                              
import numpy as np                           #importing libraries
cap = cv2.VideoCapture(0)                #creating camera object
while( cap.isOpened() ) :
	ret,img = cap.read()	#reading the frames
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(gray,(5,5),0)
	ret,thresHoldedImg = cv2.threshold(blur,50,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
	image, contours, hierarchy = cv2.findContours(thresHoldedImg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #Find the contours of the img

	thresh = 100
	canny_output = cv2.Canny(gray, thresh, thresh*2, 3);
	image, contours, hierarchy = cv2.findContours(canny_output, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE);
	#drawing = np.zeros(img.shape,np.uint8)
	#cv2.drawContours(image, contours, -1, (0,120,0), 3)
	for contour in contours:
		try:
			cv2.drawContours(img, [contour], 3, (0,255,0), 3)
			break
		except cv2.error as e:
			print e
	#cv2.drawContours(img, contours, 3, (0,255,0), 3)
	#for contour in contours:
	#	cv2.drawContours(drawing,[contour],0,(0,255,0),2)
	#cv2.imshow('input', drawing)



	#max_area = 0
	#cnt=0
	#for i in range(len(contours)):
    #        cnt=contours[i]
    #        area = cv2.contourArea(cnt)
    #        if(area>max_area):
    #            max_area=area
    #            ci=i
  	#	cnt=contours[ci]

  	#hull = cv2.convexHull(cnt)
  	#drawing = np.zeros(img.shape,np.uint8)
	#cv2.drawContours(drawing,[cnt],0,(0,255,0),2)
	#cv2.drawContours(drawing,[hull],0,(0,0,255),2)
	cv2.imshow('input',image)     #displaying the frames
	k = cv2.waitKey(10)
	if k == 27:
		break