import svgwrite
import SVG.waterbombFunct as waterbombFunct

width, height = 200, 200
dwg = svgwrite.Drawing('test.svg', size=(width, height))
# Set viewBox to flip the y-axis and shift the origin to the bottom left
dwg.viewbox(0, 0, width, height)

#funct.add_circles(dwg, tw, diff, full_W, full_L, t, added_W) #REMOVE IF DOING SEPARATE FOR CUT

waterbombFunct.make_separate_cut(dwg, tw, diff, full_W, full_L, t, added_W)

dwg.save()