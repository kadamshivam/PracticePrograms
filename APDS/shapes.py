import math

def periemeter_of_square(s):
    periemeter=4*s                 # Periemeter of square is calculated 
    return periemeter

def periemeter_of_rectangle(l,b):
    periemeter=2*(l+b)              # Periemeter of rectangle is calculated 
    return periemeter

def periemeter_of_triangle(a,b,c):
    periemeter=a+b+c               # Periemeter of triangle is calculated 
    return periemeter

def circumference_of_circle(r):
    circumference=2*math.pi*r       # Periemeter of circle is calculated 
    return circumference

def area_of_square(s):
    area=s*s                        # Area of square is calculated 
    return area

def area_of_rectangle(b,h):
    area=b*h                       # Area of rectangle is calculated 
    return area

def area_of_triangle(b,h):
    area=1/2*b*h                   # Area of triangle is calculated 
    return area

def area_of_circle(r):
    area=math.pi*r*r               # Area of circle is calculated 
    return area

def close():
    print("Thank You")             # Program exits from the main loop