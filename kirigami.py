'''#USING SVGUTILS
import svgutils
svg = svgutils.transform.fromfile('camera.svg')
originalSVG = svgutils.compose.SVG('camera.svg')
originalSVG.rotate(90)
originalSVG.move(svg.height, 10)
figure = svgutils.compose.Figure(svg.height, svg.width, originalSVG)
figure.save('svgNew.svg')'''


import svgwrite
import math
import kiriFunct

Lsq, Ltz, htri = 100, 200, 100

fullSide = Lsq + ((Lsq)+(Lsq*0.75))*2
L, W = fullSide, fullSide
# Create an SVG drawing with dimensions 800x600
dwg = svgwrite.Drawing('kirigami.svg', profile='tiny', size=(f"{L}px", f"{W}px"))
#can also do str(L) + "px", str(W) + "px"
dwg.viewbox(0, 0, L, W)

midx, midy = L/2, W/2
'''BOTH ARE EQUAL TO 450 DISTANCE IN ANY SIZE L, W
print(midy+Lsq*1.5+Lsq*0.75)
print(fullSide)
'''

theta = 270  # rotation angle in degrees
theta_rad = math.radians(theta) # degrees to radians

# Create a group for applying transformations
group = dwg.g(transform=f"rotate({theta}, {midx}, {midy})")

'''#line
group.add(dwg.line(start=(100, 100), end=(300, 100), stroke='black', stroke_width=3))'''

#circle
group.add(dwg.circle(center=(midx, midy), r=Lsq/20, fill = 'none', stroke='black', stroke_width=2)) #if want fill, add fill='red'
#square (rect)
group.add(dwg.rect(insert=((midx-(Lsq/2)), (midy-(Lsq/2))), size=(Lsq, Lsq), fill='none', stroke='black', stroke_width=2))

# Add the group to the SVG
dwg.add(group)
while theta >= 0:
    kiriFunct.trapezoid(dwg, group, midx, midy, Lsq, Ltz)
    kiriFunct.triangle(dwg, group, midx, midy, Lsq, Ltz)
    dwg.add(group)
    theta -= 90
    group = dwg.g(transform=f"rotate({theta}, {midx}, {midy})")
    print(theta)

# Save the file
dwg.save()