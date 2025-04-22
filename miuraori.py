import svgwrite
import math
import miuraoriFunct

t, tRows = 8, 8
lRect = 200
wRect = lRect

'''
var theta = 45; //in thriangle from top
________
|    C/| --> angle labeled with
|    / |
|   /  |
|  /   |
| /    |
|/_____|
miuraoriFunct.getLength(theta, lRect) 
'''

L, W = lRect*t, wRect*tRows #full length and width of crease pattern
# Create an SVG drawing with dimensions 800x600
dwg = svgwrite.Drawing('miura-ori.svg', profile='tiny', size=(f"{L}px", f"{W}px"))
dwg.viewbox(0, 0, L, W)


# Add the group to the SVG
dwg.add(dwg.line(start=(0, 0), end=(0, wRect*tRows), stroke='black')) 
for x in range(t):
    x = x*lRect
    for q in range(tRows):
        y = q * wRect
        miuraoriFunct.addCrossRect(dwg, x, y, lRect, wRect, q)
        dwg.add(dwg.line(start=(0, y), end=(L, y), stroke='black'))


# Save the file
dwg.save()