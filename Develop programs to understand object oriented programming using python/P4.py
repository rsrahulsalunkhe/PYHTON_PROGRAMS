# Object-Oriented Programming (OOP) Example

# Class definition
class Circle:
    # Class attribute
    pi = 3.14159

    # Constructor
    def __init__(self, radius):
        # Instance attributes
        self.radius = radius

    # Instance method
    def area(self):
        return self.pi * self.radius**2

    # Instance method
    def circumference(self):
        return 2 * self.pi * self.radius


# Creating instances of the Circle class
circle1 = Circle(5)
circle2 = Circle(7)

# Accessing instance attributes
print("Circle 1 - Radius:", circle1.radius)
print("Circle 2 - Radius:", circle2.radius)

# Calling instance methods
print("Circle 1 - Area:", circle1.area())
print("Circle 2 - Circumference:", circle2.circumference())

# Modifying instance attributes
circle1.radius = 10
print("Modified Circle 1 - Radius:", circle1.radius)
print("Modified Circle 1 - Area:", circle1.area())
