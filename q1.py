# Foothill College
# CS 03B - Object Oriented Programming Methodologies in Python
# Question 1
# Prepared by Viet Trinh
# Email: trinhviet@fhda.edu

import math


class Circle:
    def __init__(self, x=0, y=0, radius=1):
        """Set the intial x and y-coordinates and the radius.

        :param x: (int) X-coordinate of center of a circle
        :param y: (int) Y-coordinate of center of a circle
        :param radius: (int) radius of a circle
        """
        self._x = x
        self._y = y
        self._radius = radius

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    def get_area(self):
        """Calculate the area of a circle."""
        return math.pi * (self._radius ** 2)

    def get_perimeter(self):
        """Calculate the perimeter of a circle."""
        return 2 * math.pi * self._radius

    def contain_point(self, x, y):
        """Use distance formula to see if a point is in a circle."""
        distance = math.sqrt((x - self._x) ** 2 + (y - self._y) ** 2)
        return distance < self._radius

    def contain_circle(self, circle):
        """Use distance formula to see if a circle is in a circle."""
        distance = math.sqrt((circle.x - self._x) ** 2 +
                             (circle.y - self._y) ** 2)
        return distance + circle.radius < self._radius

    def overlaps(self, circle):
        """Check if a circle overlaps with another circle."""
        distance = math.sqrt((circle.x - self._x) ** 2 +
                             (circle.y - self._y) ** 2)
        return distance < (self._radius + circle.radius)


def run():
    print("===== Question 1 =====")
    circle1 = Circle(0, 0, 6)
    circle2 = Circle(3, 4, 2)
    circle3 = Circle(-1, -1, 1)
    circle4 = Circle(6, 6, 3)
    circles = [circle1, circle2, circle3, circle4]
    for i in range(len(circles)):
        circle = circles[i]
        print(f"Circle {i + 1}: Area = {circle.get_area():.2f}, "
              f"Perimeter = {circle.get_perimeter():.2f}")
        if circle.contain_point(2, 2):
            print(f"Point (2, 2) is inside Circle {i + 1}.")
        for j in range(len(circles)):
            if i != j:
                cir = circles[j]
                if circle.contain_circle(cir):
                    print(f"Circle {j + 1} is inside Circle {i + 1}.")
                if circle.overlaps(cir):
                    print(f"Circle {j + 1} overlaps Circle {i + 1}.")