# This is example of Test Driven Development - Why need of Test Cases ?
# Area of Triangle is (1/2*base)*height

def area_of_triangle(base, height):
    return (base/2)*height


test_cases = [(2, 5),  # Integer
              (0.5, 0.5),  # Float
              (-2, 5),  # Negative Integer
              (0, 5),  # Integer but 0 base 
              (True, 2),  # Boolean
              ("base", 2)]  # String

for data in test_cases:
    print(f"The area of triangle of {data} "
          f"is:{area_of_triangle(*data)}")

# Output :
# The area of triangle of (2, 5) is:5.0
# The area of triangle of (0.5, 0.5) is:0.125
# The area of triangle of (-2, 5) is:-5.0
# The area of triangle of (True, 2) is:1.0
# Traceback (most recent call last):
#   File "d:\Python Program\Python_Programs\Area of Triangle TDD\area_of_triangle.py", line 16, in
# <module>
#     f"is:{area_of_triangle(*data)}")
#   File "d:\Python Program\Python_Programs\Area of Triangle TDD\area_of_triangle.py", line 5, in area_of_triangle
#     return (base/2)*height
# TypeError: unsupported operand type(s) for /: 'str' and 'int'
