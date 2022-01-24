import cv2
import numpy as np
import imutils
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def click_event(event, x, y, flags, params):
    global clicked_twice
    global clicked_once
    global x1
    global x2
    global y1
    global y2
    global multiplier

    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
 
        if(clicked_twice == 0):
            if(clicked_once == 0):
                print("Clicked once")
                x1 = x
                y1 = y
                print(x, ' ', y)
                

                clicked_once = 1
            else:
                x2 = x
                y2 = y
                print("Clicked twice")
                print(x, ' ', y)
                
                
                
                absoultue = int(input("Input the separation between the clicked points: "))
                print(((  (  (x2 - x1)**2  ) + ( (y2 - y1)**2)  ) **1/2))
                multiplier = (absoultue) /  (((x2-x1)**2+(y2-y2)**2)**(0.5))
                clicked_twice = 1
                print(x1, y1, x2, y2)
                print(multiplier)
                print("Press any key on the Main Screen to continue")

        
        



def nothing(x):
    pass

def hough():
    global multiplier
    img = cv2.imread(saved_path)
    #h, w, c = img.shape
    #img = imutils.resize(img, width=600)
    cv2.namedWindow('Output')
    cv2.namedWindow('Parameters')
    cv2.resizeWindow('Parameters', 600, 300)
    cv2.createTrackbar('Gaussian','Parameters',5,20,nothing)
    cv2.createTrackbar('Median','Parameters',7,20,nothing)
    cv2.createTrackbar('Min Rad','Parameters',22,300,nothing)
    cv2.createTrackbar('Max Rad','Parameters',25,300,nothing)
    cv2.createTrackbar('Min Dist','Parameters',22,400,nothing)
    clearConsole()
    print("Press s to save changes and escape to exit")

    while(1):    
        #creating a copy of the original image
        output = img.copy()
        gaussian = cv2.getTrackbarPos('Gaussian','Parameters')
        med = cv2.getTrackbarPos('Median','Parameters')
        minrad = cv2.getTrackbarPos('Min Rad','Parameters')
        maxrad = cv2.getTrackbarPos('Max Rad','Parameters')
        mindist = cv2.getTrackbarPos('Min Dist','Parameters')
        

        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        if gaussian%2 == 0:
            gaussian += 1
        if med%2 == 0:
            med += 1

        gray_image = cv2.GaussianBlur(gray_image, (gaussian, gaussian), 0)
        gray_image = cv2.medianBlur(gray_image, med)
        # gray_image= cv2.GaussianBlur(gray_image, (7, 7), 0)
        ret, th1 = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
        th2 = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 5)
        th3 = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 5)

        # https://www.pyimagesearch.com/2021/04/28/opencv-morphological-operations/#:~:text=Morphological%20operations%20are%20simple%20transformations,and%20structures%20inside%20of%20images.
        kernel = np.ones((5, 5), np.uint8)
        erosion = cv2.erode(th2, kernel, iterations=1)
        dilation = cv2.dilate(erosion, kernel, iterations=1)

        imgray = cv2.Canny(erosion, 30, 100)

        circles = cv2.HoughCircles(imgray, method=cv2.HOUGH_GRADIENT, dp=1, minDist=mindist, param1=50, param2=30,
                                minRadius=minrad, maxRadius=maxrad)

        if circles is not None:
            circles = np.uint16(np.around(circles))
            blue = (0, 0, 255)
            green = (0, 255, 0)
            for i in circles[0, :]:
                # draw the outer circle
                cv2.circle(output,(i[0],i[1]),i[2], green, 2)
                # draw the center of the circle
                cv2.circle(output, (i[0], i[1]), 2, blue, 3)
        cv2.imshow("Output",output)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
        elif k == ord('s'):
            cv2.imwrite(saved_path, output)
            if circles is not None:
                circles = np.uint16(np.around(circles))
                for i in circles[0, :]:
                    center = (i[0]*multiplier, i[1]*multiplier)
                    radius = i[2]*multiplier
                    
                    f.write("\n")
                    f.write("Centre: ")
                    f.write(str(center))
                    f.write("\n")
                    f.write("Radius: ")
                    f.write(str(radius))
                    f.write("\n")
                    
                    print("Centre: ",center)
                    print("Radius: ",radius)
            cv2.destroyAllWindows()
            hough()
            
            

    # close all open windows
    f.close()
    cv2.destroyAllWindows()
    exit()

def contour():
    cv2.namedWindow("Result")


    cv2.resizeWindow("Result",700,700)
    cv2.namedWindow("Parameters")
    cv2.resizeWindow("Parameters",640,120)
    cv2.createTrackbar("Threshold1","Parameters",150,255,lambda x:x)
    cv2.createTrackbar("Threshold2","Parameters",255,255,lambda x:x)
    cv2.createTrackbar("Area","Parameters",5000,30000,lambda x:x)
    clearConsole()
    print("Press s to save image and escape to exit")
    img = cv2.imread(path)
    h, w, c = img.shape
    img = imutils.resize(img, width=1000)

    while(1):
        #success, img = cap.read()
        #img = cv2.imread('resources/Pics_Redrawn/1.jpg')
        imgContour = img.copy()
        cv2.putText(imgContour, "Press s to save and escape to quit",(150,13),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1,cv2.LINE_AA, False)
        

        imgBlur = cv2.GaussianBlur(img, (7,7), 1)
        imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)

        threshold1 = cv2.getTrackbarPos("Threshold1","Parameters")
        threshold2 = cv2.getTrackbarPos("Threshold2","Parameters")
        imgCanny = cv2.Canny(imgGray, threshold1, threshold2)

        kernel = np.ones((5,5))
        imgDil = cv2.dilate(imgCanny,kernel,iterations=1)

        contours, hierarchy = cv2.findContours(imgDil, cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)

        for cnt in contours:
            area = cv2.contourArea(cnt)
            areaMin = cv2.getTrackbarPos("Area","Parameters")
            if area > areaMin :
                cv2.drawContours(imgContour, cnt, -1,(255,0,255), 7)
                perimeter = cv2.arcLength(cnt,True)
                approx = cv2.approxPolyDP(cnt, 0.02*perimeter,True)
                #print(len(approx))

                #x , y , w , h = cv2.boundingRect(approx)
                #cv2.rectangle(imgContour, (x , y),(x + w, y + h),(2,255,0),5)

                #cv2.putText(imgContour,"Points: " + str(len(approx)), (x + w + 20, y  + 20), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0) , 2)
                #cv2.putText(imgContour,"Area: " + str(int(area)), (x + w + 20, y + 45), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0) , 2)

        cv2.imshow("Result", imgContour)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            cv2.destroyAllWindows()
            break
        elif k == ord('s'):
            cv2.imwrite(saved_path, imgContour)
            cv2.destroyAllWindows()
            hough()
            break

def corner():
    global multiplier
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    f.write("Corner Coordinates:")
    f.write("\n")

    for i in contours:
        img = cv2.imread(path)
        cv2.putText(img, "Press s to save coordinates and any other key to move forward",(150,13),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1,cv2.LINE_AA, False)
        size = cv2.contourArea(i)
        rect = cv2.minAreaRect(i)
        if size <10000:
            gray = np.float32(gray)
            mask = np.zeros(gray.shape, dtype="uint8")
            cv2.fillPoly(mask, [i], (255,255,255))
            dst = cv2.cornerHarris(mask,5,3,0.04)
            ret, dst = cv2.threshold(dst,0.1*dst.max(),255,0)
            dst = np.uint8(dst)
            ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
            criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
            corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)
            if len(corners) >= 4:
                coord = []
                if rect[2] == 0 and len(corners) == 5:
                    x,y,w,h = cv2.boundingRect(i)
                    if w == h or w == h +3: #Just for the sake of example
                        shape = 'Square corners: '
                        print('Square corners: ')
                        for i in range(1, len(corners)):
                            #print(corners[i])
                            corners[i] = [x * multiplier for x in corners[i]]
                            coord.append(corners[i])
                        #f.write("\n")
                    else:
                        print('Rectangle corners: ')
                        shape = 'Rectangle corners: '
                        for i in range(1, len(corners)):
                            #print(corners[i])
                            corners[i] = [x * multiplier for x in corners[i]]
                            coord.append(corners[i])


                        #f.write("\n")
                elif len(corners) == 5 and rect[2] != 0:
                    print('Rombus corners: ')
                    shape = 'Rombus corners: '
                    for i in range(1, len(corners)):
                        #print(corners[i])
                        corners[i] = [x * multiplier for x in corners[i]]
                        coord.append(corners[i])
                    #f.write("\n")
                elif len(corners) == 4:
                    print('Triangle corners: ')
                    shape = 'Triangle corners: '
                    for i in range(1, len(corners)):
                        #print(corners[i])
                        corners[i] = [x * multiplier for x in corners[i]]
                        coord.append(corners[i])
                    #f.write("\n")
                elif len(corners) == 6:
                    print('Pentagon corners: ')
                    shape = 'Pentagon corners: '
                    for i in range(1, len(corners)):
                        #print(corners[i])
                        corners[i] = [x * multiplier for x in corners[i]]
                        coord.append(corners[i])
                    #f.write("\n")
            else: continue
            img[dst>0.1*dst.max()]=[0,0,255]
            for abc in coord:
                print(str(abc))
                
            cv2.imshow('image', img)
            k = cv2.waitKey(0)
            if k == ord('s'):
                f.write(shape)
                for pqr in coord:
                    f.write(str(pqr))
                    f.write("\n")
                f.write("\n")
                print("Saved")
            cv2.destroyAllWindows()
            ##########################################
    f.write("\n")
    f.write("Circle Coordinates:")
    f.write("\n")
    f.write("\n")
    contour()
    

if __name__=="__main__":

    
    
    print("Project made by Ashish and Hoshika")

    path = 'resources/Pics_Redrawn/4.jpg'
    inppath = input("Enter path of the image as a string (Default: resources/Pics_Redrawn/4.jpg): ")
    if inppath!="":
        path = inppath
    saved_path = 'saved/savedimg.jpg'
    
    img = cv2.imread(path)
    cv2.putText(img, "Project made by Ashish and Hoshika under Dr. Angel",(150,13),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1,cv2.LINE_AA, False)
    cv2.putText(img, "Select two points and input the distance, then press enter to move ahead",(150,30),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1,cv2.LINE_AA, False)
    cv2.imshow('image', img)
    clicked_once = 0
    clicked_twice = 0
    multiplier = 0
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    cv2.setMouseCallback('image', click_event)
     
    cv2.waitKey(0)
    
    f = open("Result_Coordinates.txt", "w")
    
    cv2.destroyAllWindows()
    corner()

    
    

f.close()