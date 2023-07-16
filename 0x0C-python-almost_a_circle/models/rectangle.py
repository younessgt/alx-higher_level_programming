#!/usr/bin/python3
""" module containing Ractangle class """

from models.base import Base


class Rectangle(Base):
    """class is created"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """retreiving the rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """seatting value to width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        """retreiving the rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting a value to height"""
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        """retreiving x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setting a value to x"""
        if type(value) != int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        """retreiving y"""
        return self.__y

    @y.setter
    def y(self, value):
        """ setting value to y"""
        if type(value) != int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        """ method the return the rectangle area"""
        return self.__width * self.__height

    def display(self):
        """ printing the rectangle with '#'"""
        print("\n" * self.__y, end='')
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """ giving the object a human readable string """
        return f"[Rectangle] ({self.id})\
 {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """ updation the attributes """
        if len(args) != 0:
            for idx, value in enumerate(args):
                if idx == 0:
                    self.id = value
                elif idx == 1:
                    self.width = value
                elif idx == 2:
                    self.height = value
                elif idx == 3:
                    self.x = value
                else:
                    self.y = value
        elif kwargs:
            for c in kwargs:
                if c == 'width':
                    self.width = kwargs[c]
                elif c == 'height':
                    self.height = kwargs[c]
                elif c == 'x':
                    self.x = kwargs[c]
                elif c == 'id':
                    self.id = kwargs[c]
                else:
                    self.y = kwargs[c]

    def to_dictionary(self):
        """ returning a dictionary representation of
        the Rectangle """

        return dict(x=self.x, y=self.y,
                    id=self.id, height=self.height,
                    width=self.width)
    # we can do it by another way we can use for loop:
    # first we create an empty dict n_dict = {}
    # for key, v in self.__dict__
    # then we check if key.startswith(_Rectangle__)
    # if true n_key = [len(_Rectangle__):]
    # then n_dict[n_key] = v
    # else n_dict[key] = v
