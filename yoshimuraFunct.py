import math
import svgwrite

def y(y, full): #convert y to x-yplane
    return full - y

def getLength(theta, lRect):
    # Calculate the length of the rectangle based on the angle and width
    alpha = (180-theta)/2
    return lRect * math.tan(math.radians(alpha))

def addCrossRect(dwg, x, y, lRect, wRect):
    dwg.add(dwg.line(start=(x, y), end=(x+lRect, y+wRect), stroke='black')) #, stroke_width=1
    dwg.add(dwg.line(start=(x, y+wRect), end=(x+lRect, y), stroke='black'))
    dwg.add(dwg.line(start=(x+lRect, y), end=(x+lRect, y+wRect), stroke='black'))

def addLines(dwg, x, y, wRect, L, tRows):
    dwg.add(dwg.line(start=(0, y), end=(0, y+wRect*tRows), stroke='black')) 

    for y in range(tRows*2+1):
        y = y * wRect/2
        dwg.add(dwg.line(start=(0, y), end=(L, y), stroke='black'))
