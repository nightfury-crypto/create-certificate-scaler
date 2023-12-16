import numpy as np
import cv2

def Detectfield(template):
    # Read the image
    image = cv2.imread(template)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply GaussianBlur to reduce noise and help with edge detection
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 200, 400)
    
    # Perform Hough Line Transform
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=200, maxLineGap=40)
    
    # Find the longest line
    longest_line = None
    max_length = 0
    height, width = image.shape[:2]
    for line in lines:
        x1, y1, x2, y2 = line[0]
        length = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        if length > max_length and y1-500 < height and width/2+100 >x2-x1:
            max_length = length
            longest_line = line
    
    # Draw the longest line on the original image
    longest = None
    if longest_line is not None:
        x1, y1, x2, y2 = longest_line[0]
        longest = { "x1": x1, "y1": y1, "x2": x2, "y2": y2}
        cv2.line(image, (x1, y1), (x2, y2), (0,255, 255), 2)
    # Display the result
    # cv2.imshow("Longest Line Detection", image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return longest

