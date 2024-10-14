# Foothill College
# CS 03B - Object Oriented Programming Methodologies in Python
# Question 2
# Prepared by Viet Trinh
# Email: trinhviet@fhda.edu

# implement your code here
import math


class Triangle:
    def __init__(self, side1=1.0, side2=1.0, side3=1.0):
        """Create a default triangle.

        :param side1: (float) Side 1 of the triangle.
        :param side2: (float) Side 2 of the triangle.
        :param side3: (float) Side 3 of the triangle.
        """
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3

    @property
    def side1(self):
        return self._side1

    @property
    def side2(self):
        return self._side2

    @property
    def side3(self):
        return self._side3

    def get_perimeter(self):
        """Calculate the perimeter of the triangle."""
        return self.side1 + self.side2 + self.side3

    def get_area(self):
        """Calculate the area of the triangle with Heron's formula."""
        s = self.get_perimeter() / 2
        area = math.sqrt(s * (s - self.side1) * (s - self.side2) *
                         (s - self.side3))
        return area

    def __str__(self):
        return (f"Triangle with sides: {self.side1}, "
                f"{self.side2}, {self.side3}\n"
                f"Perimeter: {self.get_perimeter()}\n"
                f"Area: {self.get_area()}")


def run():
    print("===== Question 2 =====")
    triangle1 = Triangle(4.8, 7.0, 11.0)
    triangle2 = Triangle(2.0, 12.0, 13.1)
    print(triangle1)
    print(triangle2)
