
"""
*******************************************************************************
Ali Bora Varinli
23.03.2024
*******************************************************************************
General Purpose: This script is designed to calculate the distance between the 
legs of a capacitor in an image. The legs are defined as a 1600x200 px ROI 
between 480 – 680 px on the y-axis. The distance is measured 20 pixels above 
the lowest point of the capacitor legs. The script also prints the total 
processing time of the algorithm.
*******************************************************************************
"""


import cv2
import numpy as np
import time

class DistanceCalculation:

    def __init__(self, image_path):

        # Reading the image
        self.image = cv2.imread(image_path)

        # Defining the ROI boundaries
        self.roiStartX = 0
        self.roiStartY = 480
        self.roiEndX = 1650
        self.roiEndY = 680

    def process_image(self):
        # Extract ROI
        roi = self.image[self.roiStartY:self.roiEndY, self.roiStartX:self.roiEndX]

        # Apply bilateral filter and Canny edge detection
        bilateralSmoothing = cv2.bilateralFilter(roi, 9, 75, 75)
        edges = cv2.Canny(bilateralSmoothing, 100, 200)

        # Find contours
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        # Find points on capacitor legs and calculate distance
        leftLegPoint, rightLegPoint = self.find_point(contours)
        if leftLegPoint and rightLegPoint:
            # Adjust points to be 20 pixels above the lowest point of the legs
            leftLegPoint = (leftLegPoint[0], leftLegPoint[1] - 20)
            rightLegPoint = (rightLegPoint[0], rightLegPoint[1] - 20)

            distance = self.find_distance(leftLegPoint, rightLegPoint)

            # Calculate midpoints of each leg
            midPointY = (self.roiStartY + self.roiEndY) // 2
            midPointLeftLeg = (leftLegPoint[0], midPointY)
            midPointRightLeg = (rightLegPoint[0], midPointY)

            # Draw a line between the midpoints
            cv2.line(self.image, midPointLeftLeg, midPointRightLeg, (0, 255, 0), 2)

            # Draw the distance on the image
            cv2.putText(self.image, f"Distance: {distance:.2f} pixels", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Display the processed image
            cv2.imshow('Processed Image', self.image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            # Save the processed image
            cv2.imwrite('processed_image.png', self.image)

            return distance
        else:
            print("Could not find capacitor leg points.")
            return None

    def find_point(self, contours):
        # Sort contours based on their area, assuming larger contours are more likely to be the legs
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:2]  # Keep only the largest two contours

        points = []
        for contour in contours:
            # Calculate the moment of contour
            M = cv2.moments(contour)
            if M["m00"] != 0:
                # Calculate x, y coordinates of the center
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                points.append((cX + self.roiStartX, cY + self.roiStartY))  # Adjust for ROI offset

        if len(points) == 2:
            return points[0], points[1]  # Return the two center points
        else:
            return None, None

    def find_distance(self, point1, point2):
        # Calculate the distance between two points using the Euclidean distance formula
        distance = np.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
        return distance

if __name__ == "__main__":
    start_time = time.time()
    distance_calculation = DistanceCalculation("images/IP1_Cap.png")  # Ensure the path is correct
    distance = distance_calculation.process_image()
    if distance is not None:
        total_time = time.time() - start_time
        print(f"Distance between capacitor legs (in pixels): {distance:.2f}")
        print(f"Time taken to measure (in seconds): {total_time:.2f}")