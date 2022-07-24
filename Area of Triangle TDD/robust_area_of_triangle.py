# This is why we need Test Driven Development check noobs_area_of_triangle file
# Robust implementation of area of triangle

def area_of_triangle(base: float, height: float) -> float:
    """Calculates area of triangle for given non-negative numbers"""

    # Check if we have correct type of input parameters
    if type(base) not in [int, float]:
        raise TypeError("Base must be a number")
    if type(height) not in [int, float]:
        raise TypeError("Height must be a number")

    # Check if we have non negative input parameters
    if base < 0:
        raise ValueError("Base must be a positive number")
    if height < 0:
        raise ValueError("Height must be a positive number")

    return (base/2)*height


test_cases = [(2, 5),  # Integer
              (0.5, 0.5),  # Float
              (-2, 5),  # Negative Integer
              (0, 5),  # Integer but 0 base 
              (True, 2),  # Boolean
              ("base", 2)]  # String

for data in test_cases:
    print(f"The area of triangle of {data} "
          f"is: {area_of_triangle(*data)}")
