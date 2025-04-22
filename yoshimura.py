import svgwrite
import math
import yoshimuraFunct

t, tRows = 3, 4
theta = ((2*t - 2)*180)/(t * 2)
lRect = 200
wRect = yoshimuraFunct.getLength(theta, lRect) 

L, W = lRect*t, wRect*tRows #full length and width of crease pattern
# Create an SVG drawing with dimensions 800x600
dwg = svgwrite.Drawing('yoshimura.svg', profile='tiny', size=(f"{L}px", f"{W}px"))
dwg.viewbox(0, 0, L, W)


# Add the group to the SVG
for i in range(t):
    x = i*lRect
    for y in range(tRows):
        y = y * wRect
        yoshimuraFunct.addCrossRect(dwg, x, y, lRect, wRect)
        yoshimuraFunct.addLines(dwg, x, y, wRect, L, tRows)

# Save the file
dwg.save()