import svgwrite
import math

def y(y, full): #convert y to x-yplane
    return full - y

L, W = 800, 600
# Create an SVG drawing with dimensions 800x600
dwg = svgwrite.Drawing('rotated.svg', profile='tiny', size=("800px", "600px"))
dwg.viewbox(0, 0, L, W)

midx, midy = 400, 300
Lsq, Ltz, htri = 100, 200, 100

theta = 0  # rotation angle in degrees
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

def trapezoid(dwg, group, midx, midy, Lsq, Ltz):
    group.add(dwg.polygon(points=[(midx-Ltz/2, midy-Lsq*1.5), (midx+Ltz/2, midy-Lsq*1.5), (midx+Lsq/2, midy-Lsq/2), (midx-Lsq/2, midy-Lsq/2)], fill='none', stroke='black', stroke_width=2))

trapezoid(dwg, group, midx, midy, Lsq, Ltz)

def triangle(dwg, group, midx, midy, Lsq, Ltz):
    yOftz = midy-Lsq*1.5
    group.add(dwg.polygon(points=[(midx-Ltz/2, yOftz), (midx+Ltz/2, yOftz), (midx, yOftz-Lsq*0.75)], fill='none', stroke='black', stroke_width=2))

triangle(dwg, group, midx, midy, Lsq, Ltz)

dwg.add(group)


# Save the file
dwg.save()

'''#USINg ELEMENT TREE
import svgwrite
import xml.etree.ElementTree as ET

# Load the SVG file (replace 'existing.svg' with your file)
try:
    tree = ET.parse('existing.svg')
    root = tree.getroot()
except FileNotFoundError:
    print("Error: 'existing.svg' not found.  Creating a new SVG file.")
    root = ET.Element("svg", {"xmlns": "http://www.w3.org/2000/svg", "version": "1.1"})
    tree = ET.ElementTree(root)

# Create a new SVG drawing using the existing SVG root
d = svgwrite.Drawing(None, root)

# Define circle attributes
center_x = 100
center_y = 100
radius = 50
fill_color = 'red'
stroke_color = 'black'
stroke_width = 2

# Create the circle element
circle = d.circle(center=(center_x, center_y), r=radius, fill=fill_color, stroke=stroke_color, stroke_width=stroke_width)

# Add the circle to the SVG
d.add(circle)

# Save the modified SVG
tree.write("modified_existing.svg", encoding="utf-8")'''

'''from svgutils.transform import SVGFigure, LineElement, CircleElement, RectElement, PolygonElement

# Create SVG figure with given dimensions
fig = SVGFigure("800px", "600px")

# Create a line
line = LineElement({
    "x1": "100", "y1": "100",
    "x2": "300", "y2": "100",
    "stroke": "black", "stroke-width": "3"
})
fig.append([line])

# Create a circle
circle = CircleElement({
    "cx": "200", "cy": "200",
    "r": "50",
    "fill": "red", "stroke": "black", "stroke-width": "2"
})
fig.append([circle])

# Create a square (rectangle)
square = RectElement({
    "x": "300", "y": "200",
    "width": "100", "height": "100",
    "fill": "blue", "stroke": "black", "stroke-width": "2"
})
fig.append([square])

# Create a trapezoid with a helper function
def draw_trapezoid(x1, y1, x2, y2, x3, y3, x4, y4):
    return PolygonElement({
        "points": f"{x1},{y1} {x2},{y2} {x3},{y3} {x4},{y4}",
        "fill": "green", "stroke": "black", "stroke-width": "2"
    })

# Add trapezoid
trapezoid = draw_trapezoid(150, 300, 250, 300, 220, 350, 180, 350)
fig.append([trapezoid])

# Save to file
fig.save("shapes_example.svg")'''

'''======================================================='''