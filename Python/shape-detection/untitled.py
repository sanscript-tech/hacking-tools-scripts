import cv2
import numpy as np
import os
shapes = {}
#calculates the area of the shape

def area(cnt):
    area = cv2.contourArea(cnt)
    return area     
                      
#calculates the centroids of the shape
                                                             
def centroids(cnt):
    M = cv2.moments(cnt)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    #print(cx,cy)
    return cx,cy         


if __name__ == '__main__':
    global shapes
    img = cv2.imread("img.png",0)
    image = cv2.imread("img.png")
    h_img,w_img=img.shape
    shapes = {} #creates an empty dictionary
        
    ret,thresh = cv2.threshold(img , 240, 255, cv2.THRESH_BINARY)#calculates threshold of the gray image
    contours,hierarchy= cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    
                                
    for cnt in contours:#loops through each shape
        approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)#it approximates a contour shape 
        cv2.drawContours(image , [approx], 0, (0), 5)
        x = approx.ravel()[0]
        y = approx.ravel()[1]

        if len(approx) == 3:
            shapes["Triangle"]=[]#initialising the key "Triangle" with an empty list
            
            ar=area(cnt)#calling area function
            cx,cy=centroids(cnt)#calling centroids function
            color = image[cy,cx]#gives pixels of point(cx,cy) 
            blue,green,red=color#unpacking of tuple

            m=max(blue,green,red)
            if color[0]==m:
                col="blue"
            elif color[1]==m:
                col= "green"
            else:
                col="red"
            shapes["Triangle"].append(col)#appending the list with property color 
            shapes["Triangle"].append(ar)#appending the list with property area 

            shapes["Triangle"].append(cx)#appending the list with property cx 

            shapes["Triangle"].append(cy)#appending the list with property cy

            
        elif len(approx) == 4 : 
            (x, y, w, h) = cv2.boundingRect(approx)# to highlight the region of interest 
            arr = w / float(h)#calculates aspect ratio
            areaa=area(cnt)
            if arr >= 0.95 and arr <= 1.05 and w<(w_img-10) :#if aspect ratio is approximately equal to one then it is a square
#w<1000 because the w of the whole image is 1024 
        
                shapes["Square"]=[]
                ar=area(cnt)
                cx,cy=centroids(cnt)
                color = image[cy,cx]
                blue,green,red=color

                m=max(blue,green,red)
                if color[0]==m:
                    col="blue"
                elif color[1]==m:
                    col= "green"
                else:
                    col="red"
                shapes["Square"].append(col)    
                shapes["Square"].append(ar)
                shapes["Square"].append(cx)
                shapes["Square"].append(cy)        
            elif(w<(w_img-10) and areaa>=0.99*w*h):
                shapes["Rectangle"]=[]
                ar=area(cnt)
                cx,cy=centroids(cnt)
                color = image[cy,cx]
                blue,green,red=color

                m=max(blue,green,red)
                if color[0]==m:
                    col="blue"
                elif color[1]==m:
                    col= "green"
                else:
                    col="red"
                shapes["Rectangle"].append(col)    
                shapes["Rectangle"].append(ar)
                shapes["Rectangle"].append(cx)
                shapes["Rectangle"].append(cy)

            elif(w<(w_img-10)):
                shapes["Rhombus"]=[]
                ar=area(cnt)
                cx,cy=centroids(cnt)
                color = image[cy,cx]
                blue,green,red=color

                m=max(blue,green,red)
                if color[0]==m:
                    col="blue"
                elif color[1]==m:
                    col= "green"
                else:
                    col="red"
                shapes["Rhombus"].append(col)    
                shapes["Rhombus"].append(ar)
                shapes["Rhombus"].append(cx)
                shapes["Rhombus"].append(cy)
           
            
        elif len(approx) == 5:
            shapes["Pentagon"]=[]
            ar=area(cnt)
            cx,cy=centroids(cnt)
            color = image[cy,cx]
            blue,green,red=color

            m=max(blue,green,red)
            if color[0]==m:
                col="blue"
            elif color[1]==m:
                col= "green"
            else:
                col="red"
            shapes["Pentagon"].append(col)
            shapes["Pentagon"].append(ar)
            shapes["Pentagon"].append(cx)
            shapes["Pentagon"].append(cy)
        elif len(approx) == 6:
            shapes["Hexagon"]=[]
            ar=area(cnt)
            cx,cy=centroids(cnt)
            color = image[cy,cx]
            blue,green,red=color

            m=max(blue,green,red)
            if color[0]==m:
                col="blue"
            elif color[1]==m:
                col= "green"
            else:
                col="red"
            shapes["Hexagon"].append(col)
            shapes["Hexagon"].append(ar)
            shapes["Hexagon"].append(cx)
            shapes["Hexagon"].append(cy)    
        elif 6 < len(approx) < 15:
            shapes["Ellipse"]=[]
            ar=area(cnt)
            cx,cy=centroids(cnt)
            color = image[cy,cx]
            blue,green,red=color

            m=max(blue,green,red)
            if color[0]==m:
                col="blue"
            elif color[1]==m:
                col= "green"
            else:
                col="red"
            shapes["Ellpise"].append(col)
            shapes["Ellpise"].append(ar)
            shapes["Ellpise"].append(cx)
            shapes["Ellpise"].append(cy)
        else:
#if contour has no vertex then it is a circle
            shapes["Circle"]=[]
            ar=area(cnt)
            cx,cy=centroids(cnt)
            color = image[cy,cx]
            blue,green,red=color

            m=max(blue,green,red)
            if color[0]==m:
                col="blue"
            elif color[1]==m:
                col= "green"
            else:
                col="red"
            shapes["Circle"].append(col)
            shapes["Circle"].append(ar)
            shapes["Circle"].append(cx)
            shapes["Circle"].append(cy)


  
    
    print(shapes)
