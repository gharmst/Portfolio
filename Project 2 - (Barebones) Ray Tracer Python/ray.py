import numpy
import math
import vec3

class ray():

    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def origin(self):
        return self.origin

    def direction(self):
        return self.direction

    def at(self, t):
        return self.origin + self.t * self.direction #point3 for a given time t - at
