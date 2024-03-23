# image-processing-application-measuring-capacitor-leg-distance


This script is designed to calculate the distance between capacitor legs in an image. The legs are defined as a 1600x200 px Region of Interest (ROI) between 480 – 680 px on the y-axis. The distance is measured 20 pixels above the lowest point of the capacitor legs. The script also prints the total processing time of the algorithm.

The script starts by importing the necessary libraries: OpenCV (cv2) for image processing, numpy for numerical operations, and time to measure processing time.

A class called `DistanceCalculation` is defined and this class has methods to process the image, find the points on the capacitor legs and calculate the distance between these points.

In the `__init__` method, the image is read and ROI boundaries are defined.

The `process_image` method extracts the ROI, applies a double-sided filter to the ROI and does Canny edge detection, then finds contours in the result image. It finds the points on the capacitor legs and calculates the distance between them. If points are found, the points are set 20 pixels above the lowest point of the capacitor legs. It then calculates the midpoint of each leg, draws a line between the midpoints, and plots the distance on the image. Displays the processed image, saves it, and returns the distance. If the points are not found, a message is printed and None is returned.

The `find_point` method sorts contours by their area, assuming larger contours are more likely legs. It only keeps the two largest contours. For each contour, it calculates the moment of the contour and calculates the x,y coordinates of the center. Points are adjusted and rotated for ROI offset.

The `find_distance` method calculates the distance between two points using the Euclidean distance formula.

In the main part of the script, an instance of the `DistanceCalculation` class is created that contains the path to the image. The `process_image` method is called and if the distance is not None , it is printed. The total processing time of the algorithm is also printed.

![processed_image](https://github.com/alabora33/image-processing-application-measuring-capacitor-leg-distance/assets/41023507/18457be6-9fbf-4433-ae2a-4c2ea87ce501)
