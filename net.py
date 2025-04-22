import svgwrite
import math

def draw_cross(filename="cross_angle.svg", width=500, height=500, length=100, angle=30):
    dwg = svgwrite.Drawing(filename, size=(width, height))
    
    # Define center point
    center_x, center_y = width // 2, height // 2
    
    # Draw the first vertical line
    dwg.add(dwg.line((center_x, center_y - length), (center_x, center_y + length), stroke="black", stroke_width=2))
    
    # Draw the first horizontal line
    dwg.add(dwg.line((center_x - length, center_y), (center_x + length, center_y), stroke="black", stroke_width=2))
    
    # Calculate rotated diagonal line endpoints using the given angle
    rad_angle = math.radians(angle)  # Convert degrees to radians
    
    end_x1 = center_x + length * math.cos(rad_angle)
    end_y1 = center_y - length * math.sin(rad_angle)
    
    end_x2 = center_x - length * math.cos(rad_angle)
    end_y2 = center_y + length * math.sin(rad_angle)
    
    # Draw diagonal lines with the specified angle
    dwg.add(dwg.line((center_x, center_y), (end_x1, end_y1), stroke="red", stroke_width=2))
    dwg.add(dwg.line((center_x, center_y), (end_x2, end_y2), stroke="red", stroke_width=2))
    
    dwg.save()
    print(f"SVG file saved as '{filename}' with diagonal lines at {angle} degrees.")

draw_cross()
