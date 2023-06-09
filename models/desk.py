"""Abstract Base Classes (ABC) module"""
from abc import ABC, abstractmethod


# pylint: disable = too-many-arguments
class Desk(ABC):
    """
    An abstract base class for representing a desk.

        Attributes:
        name (str): the name of the desk;
        height (int): the height of the desk;
        width (int): the width of the desk;
        length (int): the length of the desk;
        desk_set (set): a set of desk colors.

        Methods:
        adjust_height(self, centimeters: int): an abstract method for increasing the
        height of the desk;
        move_down(self, centimeters: int): an abstract method for reducing the height
        of the desk.
    """

    def __init__(self,
                 name,
                 height,
                 width,
                 length,
                 desk_set: set = ()
                 ):
        """
            Initializes a new instance of the Desk class.

                Arguments:
                name (str): the name of the desk;
                height (int): the height of the desk;
                width (int): the width of the desk;
                length (int): the length of the desk;
                desk_set (set): a set of desk colors.
        """
        self.name = name
        self.height = height
        self.width = width
        self.length = length
        self.desk_set = desk_set

    @abstractmethod
    def adjust_height(self, centimeters):
        """
           An abstract method for increasing the height of the desk.
                Arguments:
                    centimeters (int): the height by which to increase the current
                    desk height.
        """

    @abstractmethod
    def move_down(self, centimeters):
        """
           An abstract method for reducing the height of the desk.
                Arguments:
                    centimeters (int): the height by which to reduce the current
                    desk height.
        """

    def desk_dict(self, data_type):
        """
           Returns a dictionary containing the keys and values of object's attributes,
           filtered by a specific data type.
           Args:
               data_type: the data type used to filter the attributes.
               Only attributes with values of this data type will be included in the dictionary.
           Returns:
               dict: a dictionary with the filtered attribute keys and values.
        """
        return {key: value for key, value in self.__dict__.items() if isinstance(value, data_type)}

    def __iter__(self):
        return iter(self.desk_set)
