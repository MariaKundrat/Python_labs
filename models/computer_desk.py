"""Import abstract class"""
from decorators.decorators import logged
from exceptions.exceptions import HeightError, CentimetersError
from models.desk import Desk


class ComputerDesk(Desk):
    """
    A class for representing a computer desk.

        Attributes:
        name (str): the name of the desk;
        height (int): the height of the desk;
        width (int): the width of the desk;
        length (int): the length of the desk.
        number_of_drawers (int): number of desk drawers;
        has_keyboard_tray (str): whether the desk has a retractable keyboard tray;
        max_height (int): the maximum permissible table height;
        desk_set (set): a set of desk colors.

        Methods:
        adjust_height(self, centimeters: int): method that increases the height
        of the desk (if it does not exceed the maximum allowed);
        move_down(self, centimeters: int): method that reduces the height of the
        desk (it cannot be less than 0);
        __str__(self): returns a string representation of the ComputerDesk object.
    """

    def __init__(self,
                 name: str = "Computer Desk unknown",
                 height: int = 0,
                 width: int = 0,
                 length: int = 0,
                 number_of_drawers: int = 0,
                 has_keyboard_tray: str = "Unknown",
                 max_height: int = 0,
                 desk_set: set = ("brown", "gray")
                 ):
        """
          Initializes a new instance of the ComputerDesk class.

               Arguments:
               name (str): the name of the table;
               height (int): the height of the table;
               width (int): the width of the table;
               length (int): the length of the table;
               number_of_drawers (int): number of desk drawers;
               has_keyboard_tray (str): whether the desk has a retractable
               keyboard tray;
               max_height (int): the maximum permissible table height;
               desk_set (set): a set of desk colors.
        """
        super().__init__(name, height, width, length, desk_set)
        self.number_of_drawers = number_of_drawers
        self.has_keyboard_tray = has_keyboard_tray
        self.max_height = max_height

    @logged(CentimetersError, "console")
    @logged(HeightError, "console")
    def adjust_height(self, centimeters):
        """
           Increases the height of the desk (if it does not exceed the maximum allowed).
                Arguments:
                    centimeters (int): the height by which the current desk height
                    is increased.
                Raises:
                    CentimetersError: If `centimeters` is not an integer or is less than 0.
                    HeightError: If increasing the height by `centimeters` would cause it to exceed
                    `max_height`.
        """
        if not isinstance(centimeters, int):
            raise CentimetersError("Centimeters must be an integer")
        if centimeters < 0:
            raise CentimetersError("Centimeters must be a positive integer")
        if self.height + centimeters <= self.max_height:
            self.height += centimeters
        else:
            raise HeightError(f"Cannot increase height above {self.max_height}")
        print(f"New height: {self.height}")
        return self.height

    @logged(CentimetersError, "console")
    @logged(HeightError, "console")
    def move_down(self, centimeters):
        """
           Reduces the height of the desk (it cannot be less than 0).
                Arguments:
                    centimeters (int): the height by which the current table height
                    is reduced.
                Raises:
                    CentimetersError: If `centimeters` is not an integer or is less than 0.
                    HeightError: If decreasing the height by `centimeters` would cause it to
                    go below 0.
        """
        if not isinstance(centimeters, int):
            raise CentimetersError("Centimeters must be an integer")
        if centimeters < 0:
            raise CentimetersError("Centimeters must be a positive integer")
        if self.height - centimeters >= 0:
            self.height -= centimeters
        else:
            raise HeightError(f"Cannot reduce height above {self.max_height}")
        print(f"New height: {self.height}")
        return self.height

    def __str__(self):
        return f"ComputerDesk(name={self.name}, height={self.height}, width={self.width}," \
               f"length={self.length}, number_of_drawers={self.number_of_drawers}, " \
               f"has_keyboard_tray={self.has_keyboard_tray}, max_height={self.max_height}, " \
               f"desk_set={self.desk_set})"
