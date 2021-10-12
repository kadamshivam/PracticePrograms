import shapes

def main():
    print("Menu: \n 1.Periemeter of Square \n 2.Periemeter of Rectangle \n 3.Periemeter of Triangle \n 4.Periemeter of Circle \n 5.Area of Square \n 6.Area of Rectangle \n 7.Area of Triangle \n 8.Area of Circle \n 9.Exit")
    option=int(input("Please choose a option from above Menu "))
    
    if option==1:
        print("Formula for Periemeter of square is 4*side")
        side=int(input("Please enter measurement of side "))
        answer=shapes.periemeter_of_square(side)   # Measurement of one side of Square is passed to periemeter of square method and calculated periemeter is returned and stored in answer variable.
        print("Periemeter of Square is ",answer,"\n")
        main()

    if option==2:
        print("Formula for Periemeter of rectangle is 2(length+breath)")
        length=int(input("Please enter measurement of length "))
        breadth=int(input("Please enter measurement of breadth "))
        answer=shapes.periemeter_of_rectangle(length,breadth)   # Measurement of length and breadth is passed to periemeter of rectangle method and calculated periemeter is returned and stored in answer variable.
        print("Periemeter of Rectangle is ",answer,"\n")  
        main()

    if option==3:
        print("Formula for periemeter of triangle is side(a)+side(b)+side(c)")
        a=int(input("Please enter measurement of side a "))
        b=int(input("Please enter measurement of side b "))
        c=int(input("Please enter measurement of side c "))
        answer=shapes.periemeter_of_triangle(a,b,c)    # Measurement of one side, second side and third side of Triangle is passed to periemeter of triangle method and calculated periemeter is returned and stored in answer variable.
        print("Periemeter of Triangle is ",answer,"\n")
        main()

    if option==4:
        print("Formula for Circumference of circle is 2*pi*radius")
        r=int(input("Please enter measurement of radius "))
        answer=shapes.circumference_of_circle(r)    # Measurement of radius of Circle is passed to circumference of circle method and calculated circumference is returned and stored in answer variable.
        print("Circumference of Circle is ",answer,"\n")
        main()

    if option==5:
        print("Formula for Area of Square is side*side")
        side=int(input("Please enter measurement of side "))
        answer=shapes.area_of_square(side)     # Measurement of one side of Square is passed to area of square method and calculated area is returned and stored in answer variable.
        print("Area of Square is ",answer,"\n")
        main()

    if option==6:
        print("Formula for Area of Rectangle is length*breath")
        length=int(input("Please enter measurement of length "))
        breadth=int(input("Please enter measurement of breadth "))
        answer=shapes.area_of_rectangle(length,breadth)    # Measurement of length and breadth is passed to area of rectangle method and calculated area is returned and stored in answer variable.
        print("Area of Rectangle is ",answer,"\n")
        main()

    if option==7:
        print("Formula for Area of triangle is 1/2*base*height")
        base=int(input("Please enter measurement of side base "))
        height=int(input("Please enter measurement of side height "))
        answer=shapes.area_of_triangle(base,height)     # Measurement of base and height is passed to area of triangle method and calculated area is returned and stored in answer variable.
        print("Area of Triangle is ",answer,"\n")
        main()

    if option==8:
        print("Formula for Area of Circle is pi*radius*radius")
        r=int(input("Please enter measurement of radius "))
        answer=shapes.area_of_circle(r)     # Measurement of radius of Circle is passed to area of circle method and calculated area is returned and stored in answer variable.
        print("Area of Circle is ",answer,"\n")
        main()

    if option==9:
        shapes.close()   # Close method is evoked 

main()