# Name: Junbum Ko
# SBUID: 115935594
##################### SCORE ######################
####### Score:  8/10
#################################################
# Remove the ellipses (...) when writing your solutions.

# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 

def fahrenheit2celsius(fahrenheit): 
   fahrenheit = float(input("Type the temperature in degree farenheit: "))
   celsius = (fahrenheit - 32) * 5 / 9
   return celsius

def what_to_wear(celsius):
    if celsius < -10:
        print("Puffy jacket")
        return "Puffy_jacket"
    elif celsius >= -10 and celsius < 0:
        print("Scarf")
        return "Scarf"
    elif celsius >= 0 and celsius < 10:
        print("Sweater")
        return "Sweater"
    elif celsius >= 10 and celsius < 20:
        print("Light jacket")
        return "Light jacket"
    else:
        print("T-shirt")
        return "T-shirt"

       
# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):
    return abs(((x1*y2 + x2*y3 + x3*y1)-(x1*y3 + x2*y1 + x3*y2))/ 2)

def euclidean_distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 1/2  # refrain from returning the entire equation as is

def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    return (((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 1/2) + (((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 1/2) + (((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 1/2)  # you have aldready defined euclidean_distance() that could be used to calculate parameter--> instead you put everything in the return statement -> its not a good programming practice and most of the time you will end up with the wrong output


# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 

import math

def deg2rad(deg):
    return int(deg) * math.pi / 180
    
def apothem(number_sides, length_side):
    return int(length_side) / 2 * math.tan(180/int(number_sides))   # Mistake here-> Instead of having entire equation as a return statement, you could break down the problem into variables and functions-> you could use deg2rad function to get apothem

def polygon_area(number_sides, length_side):
    return int(number_sides) * int(length_side) * int(apothem(number_sides, length_side)) / 2


# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.

# Exercise 1 test
fahrenheit = 40
what_to_wear(fahrenheit2celsius(fahrenheit))

# Exercise 2 test
x1, x2, x3, y1, y2, y3 = -4, -5, 3, -4, 5, -3 # declaration of the vertices of the triangle
area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )

# Exercise 3 test
number_sides = 5
length_side = 4
print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))

