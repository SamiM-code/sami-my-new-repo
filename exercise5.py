def calculate_triangle():
    side1 = float(input("Please give the 1st side of a triangle: "))
    side2 = float(input("Please give the 2nd side of a triangle: "))
    side3 = float(input("Please give the 3rd side of a triangle: "))

    #Triangle types are: equilateral, isosceles or scalene

    #equilateral = All 3 sides of an equilateral triangle have the same length
    #isosceles = An isosceles triangle has two sides that are the same length, and a third side that is a different
    #scalene = If all of the sides have different lengths then the triangle is scalene

    #If equilateral
    if side1 == side2 == side3:
        print("The triangle is equilateral, all of its sides are equal length")
    elif side1 != side2 != side3:
        print("The triangle is scalene, all of its sides have different lengths")
    else:
        print("The triangle is isosceles, two of its sides have equal lenght")

calculate_triangle()

