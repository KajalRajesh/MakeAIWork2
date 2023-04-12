#! /usr/bin/env python

from rectangle0 import Rectangle
from rectangle0 import Box, Triangle

rectangle = Rectangle(4, 5)
# rectangle.height = 0
# rectangle.width = 0
rectangle.getColor()
print(f'Rectangle color: {rectangle.getColor()}')
rectangle.getArea()
print(f'Rectangle area: {rectangle.getArea()}')

# change the color for the object inside the definition
rectangle1 = Rectangle(4, 5 , "white")
print(f'Rectangle1 color: {rectangle1.getColor()}')



# for child class box create object
box = Box(4,4,2)
#box.getArea()
print(f'box area: {box.getArea()}')


triangle = Triangle(4,7)
#box.getArea()
print(f'triangle area: {triangle.getArea()}')
