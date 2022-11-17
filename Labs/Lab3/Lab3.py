from __future__ import annotations # importes so that I can use float|int as class attributes, recieved error without it
import math #imports math lib 

class Positions: # created class Position to hold x and y values --> Int and float as class attributes
    def __init__(self, x: float|int, y: float|int): 
        self._x = x
        self._y = y

    @property
    def x(self) -> float|int:
        return self._x
    
    @x.setter
    def x(self, value: float|int):
        #raises TypeError if value is a str
        if isinstance(value, str):
            raise TypeError("Value cannot be a string")
        self._x = value
    
    @property
    def y(self) -> float|int:
        return self._y
    
    @y.setter
    def y(self, value: float|int):
        if isinstance(value, str):
            raise TypeError("Value cannot be a string")
        self._y = value

#  likhet ==
    def __eq__(self, other): # dunder equal method to se if values are the same
        return (self.x, self.y == other.x, other.y)
# jämför < 
    def __lt__ (self, other): # special method "less than"
        return (self.x, self.y < other.x, other.y)
# mindre eller lika <=
    def __le__(self, other): # special method less than or equal to
        return (self.x, self.y <= other.x, other.y)








