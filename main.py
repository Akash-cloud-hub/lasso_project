import cv2
import utility
import numpy as np

drawing = False
points = []
mask = None
img1 = cv2.imread('monkey-nft.png')

def main():
    clone = img1.copy()

    # (x1,y1,x2,y2) = cv2.selectROI("img1",img1,fromCenter= False,showCrosshair=True)
    #
    # selected_area = clone[y1:y1+y2,x1:x1+x2]
    # utility.show_img("selected_area",selected_area)

    cv2.namedWindow("free hand selection")
    cv2.setMouseCallback("free hand selection",draw_freehand)




def draw_freehand(event,x,y,flags,param):
    global drawing,points , mask

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        points = [(x,y)]
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        points.append((x,y))
        cv2.fillPoly(mask,[np.array(points)],(255,255,255))
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            points.append((x,y))
            mask = np.zeros_like(img1)
            while True:
                cv2.imshow("free hand selection", cv2.addWeighted(img1, 0.7, mask, 0.3, 0))
                # cv2.waitKey(0)
                key = cv2.waitKey(1) & 0xFF
                if key == ord('x'):
                    mask = np.zeros_like(img1)
                elif key == 27:
                    break

    selected_area = cv2.bitwise_and(img1,mask)
    utility.show_img("free hand selected area" , selected_area)



if __name__ == '__main__':
    main()
