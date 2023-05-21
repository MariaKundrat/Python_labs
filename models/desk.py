from abc import ABC, abstractmethod


class Desk(ABC):
    """
    An abstract base class for representing a desk.

        Attributes:
        name (str): the name of the desk;
        height (int): the height of the desk;
        width (int): the width of the desk;
        length (int): the length of the desk.

        Methods:
        adjust_height(self, centimeters: int): an abstract method for increasing the height of the desk;
        move_down(self, centimeters: int): an abstract method for reducing the height of the desk.
    """

    def __init__(self,
                 name,
                 height,
                 width,
                 length
                 ):
        """
            Initializes a new instance of the Desk class.

                Arguments:
                name (str): the name of the desk;
                height (int): the height of the desk;
                width (int): the width of the desk;
                length (int): the length of the desk.
        """
        self.name = name
        self.height = height
        self.width = width
        self.length = length

    @abstractmethod
    def adjust_height(self, centimeters):
        """
           An abstract method for increasing the height of the desk.
                Arguments:
                    centimeters (int): the height by which to increase the current desk height.
        """

    @abstractmethod
    def move_down(self, centimeters):
        """
           An abstract method for reducing the height of the desk.
                Arguments:
                    centimeters (int): the height by which to reduce the current desk height.
        """
