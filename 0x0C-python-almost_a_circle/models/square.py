#!/usr/bin/python3
""" Module containinge square class """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class is created """

    def __init__(self, size, x=0, y=0, id=None):
        """ constructor """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ converting the object info to human readable string"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ retreiving the square size"""
        return self.width

    @size.setter
    def size(self, value):
        """ setting a value to the size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ updation the attributes """

        if len(args) != 0:
            for idx, value in enumerate(args):
                if idx == 0:
                    self.id = value
                elif idx == 1:
                    self.size = value
                elif idx == 2:
                    self.x = value
                else:
                    self.y = value
        elif kwargs:
            for c in kwargs:
                if c == 'size':
                    self.size = kwargs[c]
                elif c == 'x':
                    self.x = kwargs[c]
                elif c == 'id':
                    self.id = kwargs[c]
                else:
                    self.y = kwargs[c]

    def to_dictionary(self):
        """ returning a dictionary representation of Square"""

        return dict(id=self.id, x=self.x, size=self.size, y=self.y)
