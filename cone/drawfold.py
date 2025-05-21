import svgwrite

def y():
    return 64

def write_crease(dwg, x1, y1, x2, y2):
    dwg.add(dwg.line((x1, y1), (x2, y2), stroke='black'))

def rotate(dwg, g, x, y, theta_1):
    rotation = f'rotate({theta_1}, {y}, {x})'
    g = dwg.g(transform=rotation) #'rotate(45, 50, 50)'

