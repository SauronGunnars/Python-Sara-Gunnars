import math #imports math lib 
from __future__ import annotations # importes so that I can use float|int as class attributes, recieved error without it

class Positions:
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
    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)
# jämför < 
    def __lt__ (self, other): # special method "less than"
        return (self.x, self.y )< (other.x, other.y)
# mindre eller lika <=
    def __le__(self, other): # special method less than or equal to
        return (self.x, self.y ) <= (other.x, other.y)

# translationsmetod för att flytta x och y
   # def move(self, x_move, y_move):
        return (self.x, self.y) += (self.x_move, self.y_move) 



class Circle(Positions):

    def __init__ (self, x, y, radius, x_distance, y_distance):
        super().__init__(x, y, x_distance, y_distance) # super() function has the class inherent all the properties and methods from Positions
        self._radius = radius


    @property
    def area(self):
        return (self._radius**2) * math.pi
    
    @property
    def circumfence(self):
        return (self._radius + self._radius) * math.pi

    # __repr__
    def __repr__(self) -> str:
        return f'Circle(x point: {self.x}, y point: {self.y} and radius: {self._radius})'
    # __str__()
    def __str__(self) -> str:
        return f'Circle has x point: {self.x}, y point: {self.y} and radius: {self._radius}'

    #euclidean distance to check if points are inside of circle

    def inside_circle(self, x_distance, y_distance) -> bool:
        eucledian_distance = math.sqrt((self.x - self.x_distance)**2 + (self.y - self.y_distance)**2)
        if eucledian_distance < self.radius:
            return True
        return False

    #unit circle
    def unit_circle(self):
        if self.x == 0 and self.y == 0 and self._radius == 1:
            return True
        return False
  


class Rectangle(Positions):
    def __init__(self, x, y, width, length):
        super().__init__(x, y)
        self._width = width 
        self._length = length 

    @property
    def area(self):
        return self._width*self._length
    
    @property
    def circumfence(self):
        return (self._width*2) + (self._length*2)
        
    # __repr__
    def __repr__(self) -> str:
        return f'Rectangel(x point: {self.x}, y point: {self.y}, width: {self._width} and length: {self._length})'

    # __str__()
    def __str__(self) -> str:
        return f'Rectangle has x point: {self.x}, y point: {self.y}, width: {self._width} and length: {self._length}'

    def square(self)-> bool: 
        return self.width  == self.length

    # inside of the square
    def inside_square(self):
        if self.x < self._width and self.y < self._length:
            return True




   









