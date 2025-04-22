import math
import svgwrite

def getLength(theta, lRect):
    # Calculate the length of the rectangle based on the angle and width
    alpha = (180-theta)/2
    return lRect * math.tan(math.radians(alpha))

def addCrossRect(dwg, x, y, lRect, wRect, iterEven):
    if iterEven % 2 == 0:
        dwg.add(dwg.line(start=(x, y), end=(x+lRect, y+wRect), stroke='black')) #, stroke_width=1
    else: 
        dwg.add(dwg.line(start=(x, y+wRect), end=(x+lRect, y), stroke='black'))