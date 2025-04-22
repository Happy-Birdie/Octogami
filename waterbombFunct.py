import svgwrite
#Functions for Ocogami algorithms

def get_full_length(w, tw, t):
    full_length = 0

    diff = (w - tw)/t
    current_tw_square = tw

    #full_length = (t * tw) + ((diff/2) * (t - 1))
    
    n = 1 #counter
    while n < t:
            full_length += (current_tw_square * 2) + diff/2
            current_tw_square += diff
            n+=1
    full_length += w

    return full_length

def write_crease(dwg, x1, y1, x2, y2):
    dwg.add(dwg.line((x1, y1), (x2, y2), stroke=svgwrite.rgb(255, 255, 255, '%')))

def write_in_large_diagnl(dwg, full_W, full_L, tw, added_W): #ADD BOOLEAN
    #high
    dwg.add(dwg.line((0, (full_W/2 + tw/2)), (full_L, (full_W - added_W)), stroke=svgwrite.rgb(255, 255, 255, '%')))
    #low
    dwg.add(dwg.line((0, (full_W/2 - tw/2)), (full_L, added_W), stroke=svgwrite.rgb(255, 255, 255, '%')))

    #if strip == true:
    #high
    dwg.add(dwg.line((0, (full_W/2 + tw/2) + added_W), (full_L, full_W), stroke=svgwrite.rgb(255, 255, 255, '%')))
    #low
    dwg.add(dwg.line((0, (full_W/2 - tw/2 - added_W)), (full_L, 0), stroke=svgwrite.rgb(255, 255, 255, '%')))


def write_square_length(dwg, x1, y1, x2, y2):
    dwg.add(dwg.line((x1, y1), (x2, y2), stroke=svgwrite.rgb(10, 10, 16, '%')))
    
def update_length(x1, y1, x2, y2, current_tw, diff):
    x1, x2 = x1 + current_tw, x2 + current_tw
    y1, y2 = y1 + diff/4, y2 - diff/4
    current_tw += diff/2
    return x1, y1, x2, y2, current_tw

def update_length_x2(x1, y1, x2, y2, current_tw, diff):
    x1, y1, x2, y2, current_tw = update_length(x1, y1, x2, y2, current_tw, diff)
    return update_length(x1, y1, x2, y2, current_tw, diff)

def add_strip(y1, y2, added_W,):
    return y1 + added_W, y2 - added_W

def write_square(dwg, current_tw, diff, full_W, full_L, t, added_W):
    #REMOVE ALL added_W & add_strip IF YOU DON'T WANT EXTRA STRIP
    x1, y1 = 0, (full_W/2 + current_tw/2 + added_W)
    x2, y2 = 0, (full_W/2 - current_tw/2 - added_W)
    n = 1
    while (n <= ((2 * t) - 1)):
        dwg.add(dwg.line((x1, y1), (x2, y2), stroke=svgwrite.rgb(255, 255, 255, '%')))
        x1, y1, x2, y2, current_tw = update_length(x1, y1, x2, y2, current_tw, diff)
        add_strip(y1, y2, added_W)
        if (n % 2 == 1):
            dwg.add(dwg.line((x1+current_tw/2, y1+diff/8), (x2+current_tw/2, y2-diff/8), stroke=svgwrite.rgb(255, 255, 255, '%'))) 
        n+=1
    dwg.add(dwg.line((full_L, 0), (full_L, full_W), stroke=svgwrite.rgb(255, 255, 255, '%'))) 
    #used to be y1 --> added_W, y2 --> full_W - added_W

def write_crease_pattern(dwg, current_tw, diff, full_W, full_L, t, added_W):
    x1, y1 = 0, (full_W/2 + current_tw/2)
    x2, y2 = 0, (full_W/2 - current_tw/2)
    x1_otherend, y1_otherend = x1, y1
    x2_otherend, y2_otherend = x2, y2
    current_tw2 = current_tw

    x1, y1, x2, y2, current_tw = update_length(x1, y1, x2, y2, current_tw, diff)
    x1_otherend, y1_otherend, x2_otherend, y2_otherend, current_tw2 = update_length_x2(x1_otherend, y1_otherend, x2_otherend, y2_otherend, current_tw2, diff)

    n = 1 #counter
    while n < t:
        write_crease(dwg, x1, y1, x2_otherend, y2_otherend)
        write_crease(dwg, x2, y2, x1_otherend, y1_otherend)

        x1, y1, x2, y2, current_tw = update_length_x2(x1, y1, x2, y2, current_tw, diff)
        x1_otherend, y1_otherend, x2_otherend, y2_otherend, current_tw2 = update_length_x2(x1_otherend, y1_otherend, x2_otherend, y2_otherend, current_tw2, diff)
        
        n+=1

def add_circles(dwg, current_tw, diff, full_W, full_L, t, added_W):
    r = 2 #circle radius
    x1, y1 = 0 + r, (full_W/2 + current_tw/2) + added_W/3
    x2, y2 = 0 + r, (full_W/2 - current_tw/2) - added_W/3
    x1, y1, x2, y2, current_tw = update_length(x1, y1, x2, y2, current_tw, diff)
    
    '''
    radius = 5 if elastic band
    or jsut keep = 1 for now
    '''
    n = 1 #counter
    while n < ((2 * t) - 1):
        circle = dwg.circle(center=(x1, y1), r=r, fill='none', stroke=svgwrite.rgb(255, 255, 255, '%'))
        dwg.add(circle) # Add the circle to the drawing
        circle = dwg.circle(center=(x2, y2), r=r, fill='none', stroke=svgwrite.rgb(255, 255, 255, '%'))
        dwg.add(circle) # Add the circle to the drawing

        x1, y1, x2, y2, current_tw = update_length(x1, y1, x2, y2, current_tw, diff)        
        n+=1

def add_lined_circles(dwg, current_tw, diff, full_W, full_L, t, added_W):
    r = 2 #circle radius
    x1, y1 = 0 + r, (full_W/2)
    x2, y2 = current_tw - r, (full_W/2)
    #useless, useless2, x2, useless3, current_tw = update_length(x1, y1, x2, y2, current_tw, diff)
    x1, useless2, x2, useless3, current_tw = update_length(x1, y1, x2, y2, current_tw, diff)

    #x1, x2 = x1 + current_tw, x2 + current_tw      

    '''
    radius = 5 if elastic band
    or jsut keep = 1 for now
    '''
    n = 1 #counter
    while n < ((2 * t) - 1):
        circle = dwg.circle(center=(x1, y1), r=r, fill='none', stroke=svgwrite.rgb(255, 255, 255, '%'))
        dwg.add(circle) # Add the circle to the drawing
        circle = dwg.circle(center=(x2, y2), r=r, fill='none', stroke=svgwrite.rgb(255, 255, 255, '%'))
        dwg.add(circle) # Add the circle to the drawing

        x1 -= r
        x2 += r
        x1, useless2, x2, useless3, current_tw = update_length_x2(x1, y1, x2, y2, current_tw, diff)
        x1 += r
        x2 -= r
        n+=1

def make_separate_cut(dwg, current_tw, diff, full_W, full_L, t, added_W):
    dwg = svgwrite.Drawing('octogami_tenctacle_cut.svg', size=(full_L, full_W))
    # Set viewBox to flip the y-axis and shift the origin to the bottom left
    dwg.viewbox(0, 0, full_L, full_W)
    #strip diagonals
    dwg.add(dwg.line((0, (full_W/2 + current_tw/2) + added_W), (full_L, full_W), stroke=svgwrite.rgb(255, 255, 255, '%')))
    dwg.add(dwg.line((0, (full_W/2 - current_tw/2 - added_W)), (full_L, 0), stroke=svgwrite.rgb(255, 255, 255, '%')))
    
    #end lines: tw, full_W
    x1, y1 = 0, (full_W/2 + current_tw/2 + added_W)
    x2, y2 = 0, (full_W/2 - current_tw/2 - added_W)
    dwg.add(dwg.line((x1, y1), (x2, y2), stroke=svgwrite.rgb(255, 255, 255, '%')))
    dwg.add(dwg.line((full_L, 0), (full_L, full_W), stroke=svgwrite.rgb(255, 255, 255, '%'))) 

    #circles
    add_circles(dwg, current_tw, diff, full_W, full_L, t, added_W)
    #add_lined_circles(dwg, current_tw, diff, full_W, full_L, t, added_W)
    dwg.save()
