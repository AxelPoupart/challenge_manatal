
import math

# Made of a radius and compute


class Circle(object):

    radius = 0

    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        return (self.radius ** 2)*math.pi

    def compute_perimeter(self):
        return (self.radius) * 2 * math.pi
