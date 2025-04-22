import svgwrite
import waterbombFunct
#Octogami
'''
state by length and width of it and put out the size thingie
VAR L W


l, w = 100, 1

L has to be >= 2w
w/3 is tw

'''

'''
L = full length of folded tesselation
W = full width of folded tesselation
t = number of squares in tesselation
tw = width of smallest square
'''
input_fullLength_cm, input_fullWidth_cm = 10, 3

L, W, t, tw = 1600, 200, 15, 30 #1000, 110, 10, 30 #500, 100, 5, 50
added_W = W/5 #tw/2
full_L = waterbombFunct.get_full_length(W, tw, t)
full_W = W + (added_W * 2)
diff = (W - tw)/t

width, height = full_L, full_W #L * 2, (W * 1.5) + (added_W * 2)


'''def square_trapezoid(dwg):
    dwg.add(dwg.line((0, 0), (10, 100), stroke=svgwrite.rgb(10, 10, 16, '%')))
    dwg.add(dwg.line((0, 0), (10, 100), stroke=svgwrite.rgb(10, 10, 16, '%')))
'''

dwg = svgwrite.Drawing('octogami_tenctacle_crease_p.svg', size=(width, height))
# Set viewBox to flip the y-axis and shift the origin to the bottom left
dwg.viewbox(0, 0, width, height)
waterbombFunct.write_in_large_diagnl(dwg, full_W, full_L, tw, added_W)
waterbombFunct.write_square(dwg, tw, diff, full_W, full_L, t, added_W)
waterbombFunct.write_crease_pattern(dwg, tw, diff, full_W, full_L, t, added_W)
#funct.add_circles(dwg, tw, diff, full_W, full_L, t, added_W) #REMOVE IF DOING SEPARATE FOR CUT

waterbombFunct.make_separate_cut(dwg, tw, diff, full_W, full_L, t, added_W)

dwg.save()