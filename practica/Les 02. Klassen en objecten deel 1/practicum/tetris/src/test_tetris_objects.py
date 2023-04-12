#!/usr/bin/env python

from tetris_objects import Figure
from random import choice, randrange
import logging
import numpy as np

logging.basicConfig(level=logging.DEBUG)

# Random Red Green Blue Color
color = lambda: (randrange(30, 256), randrange(30, 256), randrange(30, 256))

# Block
shape = np.array([(0, -1), (-1, -1), (-1, 0), (0, 0)])

# Create block object from class Figure
blockShape = np.array([])
block = Figure(shape, color)

logging.debug(f"block color : {block.getColor()}")
logging.debug(f"block shape :  {block.getShape()}")

# iShape

# Shape of i-shape
shape = np.array([(-1, 0), (-2, 0), (0, 0), (1, 0)])

# Random Red Green Blue Color
color = lambda: (randrange(30, 256), randrange(30, 256), randrange(30, 256))

iShape = Figure(shape, color)

logging.debug(f"iShape color : {iShape.getColor()}")
logging.debug(f"iShape shape :  {iShape.getShape()}")

logging.debug("Rotate counterclockwise")
iShape.rotate()

logging.debug(f"iShape color : {iShape.getColor()}")
logging.debug(f"iShape shape :  {iShape.getShape()}")

# zShape

# Shape of z-shape
shape = np.array(
    [(-1, 0), (-1, 1), (0, 0), (0, -1)],
)

# Random Red Green Blue Color
color = lambda: (randrange(30, 256), randrange(30, 256), randrange(30, 256))
zShape = Figure(shape, color)

logging.debug(f"zShape color : {zShape.getColor()}")
logging.debug(f"zShape shape :  {zShape.getShape()}")
zShape.rotate()

logging.debug(f"zShape color : {zShape.getColor()}")
logging.debug(f"zShape shape :  {zShape.getShape()}")