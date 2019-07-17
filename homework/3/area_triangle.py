def get_triangle_area(x1,y1,x2,y2,x3,y3):
    area = (abs(x2*y3-x3*y2-x1*y3+x3*y1+x1*y2-x2*y1))/2
    return area
