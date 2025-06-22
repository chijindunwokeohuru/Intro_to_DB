import math

class Shape:
    """
    Base class for all shapes.
    """
    
    def area(self):
        """
        Calculate the area of the shape.
        This is an abstract method that should be overridden by subclasses.
        
        Raises:
            NotImplementedError: If the method is not overridden in a subclass
        """
        raise NotImplementedError("Subclass must implement abstract method")


class Rectangle(Shape):
    """
    A class representing a rectangle, inheriting from Shape.
    
    Attributes:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
    """
    
    def __init__(self, length, width):
        """
        Initialize a new Rectangle instance.
        
        Args:
            length (float): The length of the rectangle
            width (float): The width of the rectangle
        """
        self.length = length
        self.width = width
    
    def area(self):
        """
        Calculate the area of the rectangle.
        
        Returns:
            float: The area of the rectangle (length × width)
        """
        return self.length * self.width


class Circle(Shape):
    """
    A class representing a circle, inheriting from Shape.
    
    Attributes:
        radius (float): The radius of the circle
    """
    
    def __init__(self, radius):
        """
        Initialize a new Circle instance.
        
        Args:
            radius (float): The radius of the circle
        """
        self.radius = radius
    
    def area(self):
        """
        Calculate the area of the circle.
        
        Returns:
            float: The area of the circle (π × radius²)
        """
        return math.pi * self.radius ** 2