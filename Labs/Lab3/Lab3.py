import math #imports math lib 
from __future__ import annotations # importerar future annotations. Kunde inte tilldela "attributes Int|float till klasserna annars" 

# I denna klass finns properties och metoder som är relevanta för både Circle och Rectangle klassen
class Positions:
    def __init__(self, x: float|int, y: float|int): 
        self._x = x
        self._y = y
 

    @property
    def x(self) -> float|int:
        return self._x
    
    @x.setter #setter tillåter oss att tilldela värde åt x samt återge felmeddelande om ett icke numeriskt värde matas in
    def x(self, value: float|int):
        #raises TypeError if value is a str
        if isinstance(value, str):
            raise TypeError("Värdet kan inte vara en sträng")
        self._x = value
    
    @property
    def y(self) -> float|int:
        return self._y
    
    @y.setter #setter tillåter oss att tilldela värde åt y samt återge felmeddelande om ett icke numeriskt värde matas in
    def y(self, value: float|int):
        if isinstance(value, str):
            raise TypeError("Värdet kan inte vara en sträng")
        self._y = value

#  likhet ==
    def __eq__(self, other): #dunder metod för att jämföra
        return (self.x, self.y) == (other.x, other.y)
# jämför < 
    def __lt__ (self, other): # special metod "less than"
        return (self.x, self.y ) < (other.x, other.y)
# mindre eller lika <=
    def __le__(self, other): # special metod "less than or equal to"
        return (self.x, self.y ) <= (other.x, other.y)

# translationsmetod. Metoden skulle "flytta" på x och y genom att ge nya värden till x och y, fick dock inte denna att fungera.
    def move(self, new_x, new_y):
        return (self.x, self.y) = (self.new_x, self.new_y)


# I denna klass finns properties och metoder specifika för circle klassen
class Circle(Positions):

    def __init__ (self, x, y, radius):
        super().__init__(x, y) # super() ser till att "barn-klassen" ärver allt från föräldra klassen (Positions)
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

    #euclidean distance för att beräkna om punkter är innanför cirkeln
    # fick inte denna att fungera....
    def inside_circle(self, x_distance, y_distance) -> bool:
        eucledian_distance = math.sqrt((self.x - self.x_distance)**2 + (self.y - self.y_distance)**2)
        if eucledian_distance < self.radius:
            return True
        return False

    #Metod för enhetscirkeln. Returnerar sann om inmatade cirkeln har nedanstående värden
    def unit_circle(self):
        if self.x == 0 and self.y == 0 and self._radius == 1:
            return True
        return False
  

# I denna klass finns properties och metoder specifika för rectangle klassen
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
        

    # __repr__ - skapar en repr som skriver ut stringen nedan
    def __repr__(self) -> str:
        return f'Rectangel(x point: {self.x}, y point: {self.y}, width: {self._width} and length: {self._length})'

    # __str__() # dunder str som även  denna skriver ut texten nedan
    def __str__(self) -> str:
        return f'Rectangle has x point: {self.x}, y point: {self.y}, width: {self._width} and length: {self._length}'

    def square(self)-> bool:  #metod för att undersöka om inmatade värden är en kvadrat
        return self.width  == self.length

    # inside of the square - metod för att se om punkter befinner sig inom rektangeln
    def inside_square(self): 
        if self.x < self._width and self.y < self._length:
            return True




   









