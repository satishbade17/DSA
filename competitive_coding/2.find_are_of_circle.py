import math

def area_of_circle(r):
    area = math.pi * r * r
    return round(area, 3)   # Round to 2 decimal places

r = float(input("Enter the radius: "))
print("Area of circle:", area_of_circle(r))