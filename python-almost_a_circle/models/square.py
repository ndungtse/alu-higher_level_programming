#!/usr/bin/python3
"""Defines the Square class, a Rectangle with equal width and height."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square, a special rectangle sharing one size value."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square using size for both width and height."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return [Square] (<id>) <x>/<y> - <size>."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Return the size (width) of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set width and height to the same size value."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes from positional args, else keyword args."""
        if args:
            attrs = ["id", "size", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the square."""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
