import cv2 as cv
import numpy as np

print('''

//*** USER MANUAL ***//

*** FOR SWITCHING BETWEEN PHASES DOUBLE CLICK MOUSE WHEEL ***

PHASE 1 {

FOR DRAWING CIRCLE JUST SINGLE LEFT CLICK
FOR DRAWING RECTANGLE JUST SINGLE RIGHT CLICK

}

PHASE 2 {
    FOR WRITING TEXT SINGLE RIGHT CLICK THEN WRITE THE TEXT YOU WANT TO WRITE ON SCREEN AND THEN ENTER THE THICKNESS OF TEXT
    FOR DRAWING ECLIPSE JUST DOUBLE LEFT CLICK
    FOR DRAWING SINGLE LEFT CLICK ON POINTS BETWEEN YOU WANT TO CREATE LINE
}

FOR CHANGING COLOR JUST USE TRACKBAR ABOVE

R -> RED
G -> GREEN
B -> BLUE

''')

mode = True
draw = False
mode2 = True
ix,iy = -1,-1

def color_r(c):
    r = c
    return r
    
def color_g(c):
    g = c
    return g
    
def color_b(c):
    b = c
    return b
    
def Paints(event,x,y,flags,param):
    global mode,ix,iy,mode2,draw,color
 
    if event == cv.EVENT_MBUTTONDBLCLK:
        if mode == True:
            mode = False
            draw = True
            mode2 = False
        else:
            mode = True
            draw = False
            mode2 = True
        
    elif event == cv.EVENT_LBUTTONDOWN:
        if mode2 == True:
            if draw == False:
                cv.circle(img,(x,y),15,(r,g,b),-1)
            

    elif event == cv.EVENT_LBUTTONDBLCLK:
        if mode2 == False:
                cv.ellipse(img,(ix,iy),(x,y),0,0,180,(r,g,b),-1)


    elif event == cv.EVENT_RBUTTONDOWN:
        if mode == True:
            if draw == False:
                    cv.rectangle(img,(ix,iy),(x,y),(r,g,b),-1)
                    ix,iy = -1,-1
            else:
                if ix == -1 and iy == -1:
                    ix = x
                    iy = y 
                    
    elif event == cv.EVENT_LBUTTONUP:
        if mode == False:
            if ix == -1 and iy == -1:
                ix = x
                iy = y
            else:
                cv.line(img,(ix,iy),(x,y),(r,g,b),1)
                ix,iy = -1,-1
    
    elif event == cv.EVENT_RBUTTONUP:
        if mode == False: 
            font = cv.FONT_HERSHEY_SIMPLEX
            text = input('Enter text you want to enter : ')
            text_thickness = int(input('Enter thickness you want to enter : '))
            cv.putText(img,text,(x,y), font, text_thickness,(r,g,b),2,cv.LINE_AA)

            
img = np.zeros((600,600,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',Paints)

cv.createTrackbar('R','image',0,255,color_r)
cv.createTrackbar('G','image',0,255,color_g)
cv.createTrackbar('B','image',0,255,color_b)

# switch = '0 : OFF \n1 : ON'
# cv.createTrackbar(switch, 'image',0,1,nothing)

while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

    r = cv.getTrackbarPos('R','image')
    g = cv.getTrackbarPos('G','image')
    b = cv.getTrackbarPos('B','image')
    # s = cv.getTrackbarPos(switch,'image')
    # if s == 0:
    #     img[:] = 0
    # else:
    #     img[:] = [b,g,r]
cv.destroyAllWindows()