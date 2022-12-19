import re


class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * pow(self.radius, 2)
    def length(self):
        return 2 * 3.14 * self.radius