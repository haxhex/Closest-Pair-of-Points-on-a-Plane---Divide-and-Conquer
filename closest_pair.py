"""
Author : Helia Ghorbani
Student ID : 9824353
Date: 2022-05-18
----------------------------------------------------------
The algorithm finds distance between closest pair of points
in the given n points by using Divide and Conquer approach.
----------------------------------------------------------
Summary of how it works:
The points are sorted based on X and then based on Y separately.
By applying divide and conquer approach, 
minimum distance will be found recursively.
Closest points may be on different sides of partition.
This case handled by forming a border of points
which X distance is less than closest pair distance
(by using closest_pair_dis) from mid point of X. 
Points sorted based on Y are used to reduce sorting time.
Closest pair distance is found in the border of points. 
(by using closest_in_border)
----------------------------------------------------------
Final result:
At the end the minimum of closest_pair_dis and closest_in_border
(finding by using min(closest_pair_dis, closest_in_border)) 
would be the final answer.
----------------------------------------------------------
Time complexity: O(n*log n)
"""
# ----------------------------------------------------------

import math
import copy
"""
distance_calculator(point1, point2)
----------------------------------------------------------
This function calculate square distance between 2 given points.
----------------------------------------------------------
Input: 2 points
Output: sqrt((x2 - x1)^2 + (y2 - y1)^2)
"""
def distance_calculator(point1, point2):
	dst = math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)
	return dst

# ----------------------------------------------------------

"""
minimum_distance_finder(points,  points_nums,  minimum_distance = float("inf"))
----------------------------------------------------------
Brute Force approach to find distance between closest pair points
This function find the minimum distance between given points
by using two nested loops. 
In this function calculate distance between each of 2 points
by using function 'distance_calculator'.
If current distance less than minimum distance calculated in last
step minimum distance will be equal to current distance.
After dividing our problem to subproblems is used it to solve 
subproblems.
----------------------------------------------------------
Input: array of points, number of points
Output: minimum distance between given points
"""
def minimum_distance_finder(points, points_nums, minimum_distance = float("inf")):
	for i in range(points_nums):
		for j in range(i + 1, points_nums):
			if distance_calculator(points[i], points[j]) < minimum_distance:
				minimum_distance = distance_calculator(points[i], points[j])
	return minimum_distance

# ----------------------------------------------------------

"""
closest pair of points in border
This function find minimum distance of points that 
in the border less than minimum distance.
All points are sorted according to y value.
Find the points that difference between their 'y' is less than minimum distance.
This loop runs at most 6 times.
----------------------------------------------------------
Input: array of points, number of points, minimum distance
Output: minimum_distance
"""
def minimum_distance_in_border(border, size, minimum_distance = float("inf")):	
	for i in range(size):
		j = i + 1
		while j < size and (border[j][1] - border[i][1]) < minimum_distance:
			minimum_distance = distance_calculator(border[i], border[j])
			j += 1
	return minimum_distance
# ----------------------------------------------------------
"""
closest_pair_of_points(points_sorted_on_x, points_sorted_on_y, points_nums)
----------------------------------------------------------
Divide and Conquer Approach:
Divide problem to subproblems and solve subproblems
by using a recursive function to find the minimum distance.
----------------------------------------------------------
Input: array of points sorting according to x, array of points sorting on y,
	   number of points
Output: 
"""
def closest_pair_of_points(points_sorted_on_x, points_sorted_on_y, points_nums):
	# Using brute force "minimum_distance_finder" function if there are 2 or 3 points.
	if  points_nums <= 3:
		return minimum_distance_finder(points_sorted_on_x, points_nums)
# ----------------------------------------------------------
	# Find the middle point
	mid =  points_nums // 2
	midPoint = points_sorted_on_x[mid]
# ----------------------------------------------------------
	# a copy of left points according to mid point
	left_points = points_sorted_on_x[:mid]
	# a copy of right points according to mid point
	right_points = points_sorted_on_x[mid:]
# ----------------------------------------------------------
	# According to mid point consider vertical line and find min of each side,
	left_min_distance = closest_pair_of_points(left_points, points_sorted_on_y, mid)
	right_min_distance = closest_pair_of_points(right_points, points_sorted_on_y, points_nums - mid)
# ----------------------------------------------------------
	# Find the smaller between left minimum and right minimum
	min_left_right = min(left_min_distance, right_min_distance)
# ----------------------------------------------------------
	# Make array border[] that contains points closer than
 	# min_left_right to the line passing through the mid point
	border_points_sorted_on_x = []
	border_points_sorted_on_y = []
	# append left points and right points
	left_right_points = left_points + right_points
	for i in range(points_nums):
		# if difference between points to mid point less than minimum
		# between left side and right side append it to border
		# that sorted according to x
		if abs(left_right_points[i][0] - midPoint[0]) < min_left_right:
			border_points_sorted_on_x.append(left_right_points[i])
   # ----------------------------------------------------------
   		# if difference between points sorted based on y and mid point
		# less than minimum between left side and right side according
		# append it border that sorted according to y
		if abs(points_sorted_on_y[i][0] - midPoint[0]) < min_left_right:
			border_points_sorted_on_y.append(points_sorted_on_y[i])
   # ----------------------------------------------------------
   	#sort border that sorted based on x according to y
	border_points_sorted_on_x.sort(key = lambda point: point[1])
 	# find the minimum between minumum of left and right side
	# and border that sorted according to x
	min_x = min(min_left_right, minimum_distance_in_border(border_points_sorted_on_x, len(border_points_sorted_on_x), min_left_right))
  	# find the minimum between minumum of left and right side
	# and border that sorted according to y
	min_y = min(min_left_right, minimum_distance_in_border(border_points_sorted_on_y, len(border_points_sorted_on_y), min_left_right))
   # ----------------------------------------------------------
	# find minimum distance of points in border
	min_xy = min(min_x, min_y) 
	return min_xy
# ----------------------------------------------------------
"""
closest(points, points_nums)
----------------------------------------------------------
This function find the closest points 
first make a copy of points and sort them according to x
and call function 'closest_pair_of_points' to divide problem
to smaller subproblems
and then solve smaller problems recursively
----------------------------------------------------------
Input: array of points, number of points
Output: smallest distance between closest points
"""
def closest_point(points, points_nums):
	points.sort(key = lambda point: point[0])
	# make copy of points and sort them based on x
	points_sort_x = copy.deepcopy(points)
	points_sort_x.sort(key = lambda point: point[0])
# ----------------------------------------------------------
	# find smallest distance by using 'closest_pair_of_points'
	# recursively
	return closest_pair_of_points(points, points_sort_x, points_nums)
# ----------------------------------------------------------
# sample points - Input points
#points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
# points = [(-1, 3), (3, 3), (1, 1), (4, 2), (2, 0.5), (-1, -1), (2, -1), (4, -0.5)]
# number of points
points = [(2, 4),
(12, 12),
(10, 12),
(5, 20),
(13, 14),
(5, 5),
(30, 1)]
points_nums = len(points)
# prints result
result = "{0:.5f}".format(closest_point(points, points_nums))

print(f"the minimum distance is: {result} unit")

