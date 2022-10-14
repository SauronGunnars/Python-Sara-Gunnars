import math #imports math lib 

class Circle:
    def __init__ (self, x, y, radius):
        self._x = x
        self._y = y
        self._radius = radius
    @property
    def area(self):
        return (self._radius**2) * math.pi
    
    @property
    def circumfence(self):
        return (self._radius + self._radius) * math.pi

class Rectangle:
    def __init__(self, x, y, width, length):
        self._x = x
        self._y = y
        self._width = width 
        self._length = length 

    @property
    def area(self):
        return self._width*self._length
    
    @property
    def circumfence(self):
        return (self._width*2) + (self._length*2)






