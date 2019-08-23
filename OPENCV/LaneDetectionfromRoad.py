import cv2
import numpy as np
import matplotlib.pyplot as plt


def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #gblur = cv2.GaussianBlur(gray, (3, 3), 2)  # noise filtering by blurring iteration=2 kernel3x3
    gblur = cv2.GaussianBlur(gray, (5, 5), 0)  # noise filtering by blurring kernel5x5 iteration=0
    #gblur = cv2.GaussianBlur(gblur, (7, 7), 0)  # noise filtering by blurring iteration=2 kernel7x7
    edges = cv2.Canny(gblur, 50, 150)
    return edges


def region_of_interest(image):
    img_heigth = image.shape[0]  # shape[0] contains heigth of image
    '''
    region of interest is a triangular area for this application
    triangle definition= np.array of 3 points: [(Xa,Ya) (Xb,Yb) (Xc,Yc)] 
                                   (Xc,Yc) = (550, 250)
                                    /\
                                   /  \
                                  /____\n    
       (Xa,Ya)=(200, img_heigth)          (Xb,Yb) = (1100, img_heigth)
    '''
    roi_polygon_triangle = np.array([[(200, img_heigth), (1100, img_heigth), (550, 250)]])  #
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, roi_polygon_triangle, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

def display_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        '''alternative snippet
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 5)
        '''
        for x1, y1, x2, y2 in lines:
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 5)
    return line_image


def make_coordinates(image, line_params):
    slope, intercept = line_params
    y1 = image.shape[0]
    x1 = int((y1-intercept)/slope)
    y2 = int(y1*(3/5))
    x2 = int((y2 - intercept) / slope)
    return np.array([x1, y1, x2, y2])


def average_slope_intercept(image, lines):  # calculates avarage of slopes and intercepts of the lines seperately
    left_fit = []
    right_fit = []
    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        # polyfit returns slope(m) and const(c) of y=mx+c eqn consist of x1,x2,y1,y2 points
        # so, parameters[0] is slope m of the line and parameters[1] is constant of the line(y-intercept)
        parameters = np.polyfit((x1, x2), (y1, y2), 1)  # 1 means linear function fitting
        slope = parameters[0]
        intercept = parameters[1]  # interception point on the y axis (this is c in the eqn y=mx+c)
        if slope < 0:
            '''sum with left_fit if the line is on the left 
            we determine that if the line on the image has negative slope then the line is on the left side
            similarly
            '''
            left_fit.append((slope, intercept))
        else:
            '''sum with right_fit if the line is on the right 
            similarly if the line on the image has positive slope then the line is on the left side
            '''
            right_fit.append((slope, intercept))

    left_fit_average = np.average(left_fit, axis=0)
    right_fit_average = np.average(right_fit, axis=0)
    left_line = make_coordinates(image, left_fit_average)
    right_line = make_coordinates(image, right_fit_average)
    return np.array([left_line, right_line])



cap = cv2.VideoCapture("roadvideo.mp4")
while(cap.isOpened()):
    _, frame = cap.read()
    #img = cv2.imread('road2.jpg')
    #lane_image = np.copy(img)

    lane_image = np.copy(frame)   # taking copy
    cannyEdges = canny(lane_image)  # edge detection

    cropped_image = region_of_interest(cannyEdges)  # eliminating irrelevant regions on image (finding ROI)
    # detecting lines on ROI
    lines = cv2.HoughLinesP(cropped_image, 1, np.pi / 180, 100, np.array([]), minLineLength=40, maxLineGap=5)

    # average  lines on the both side seperately (right and left sides)
    averaged_lines = average_slope_intercept(lane_image, lines)

    # create a frame layer which only shows lines
    line_image = display_lines(lane_image, averaged_lines)

    # merge down lines layer and original image (adding weighted results in transparency for the lines)
    combo_image = cv2.addWeighted(line_image, 0.8, lane_image, 1, 1)

    #cv2.imshow("result line_image", line_image)
    cv2.imshow("result line_image on original image", combo_image)
    k = cv2.waitKey(1)
    if k == 27:
        break

    '''or  
    if cv2.waitKey(1) == ord('q'):
        break
    '''

cv2.destroyAllWindows()


