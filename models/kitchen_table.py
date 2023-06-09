"""Import abstract class"""
from models.desk import Desk


# pylint: disable = too-many-arguments
class KitchenTable(Desk):
    """
    A class for representing a kitchen table.

        Attributes:
        name (str): the name of the desk;
        height (int): the height of the desk;
        width (int): the width of the desk;
        length (int): the length of the desk.
        material (str): the material of the table;
        max_height (int): the maximum permissible table height;
        desk_set (set): a set of desk colors.

        Methods:
        adjust_height(self, centimeters: int): method that increases the height
        of the desk (if it does not exceed the maximum allowed);
        move_down(self, centimeters: int): method that reduces the height of the
        desk (it cannot be less than 0);
        __str__(self): returns a string representation of the KitchenTable object.
    """

    def __init__(self,
                 name: str = "Kitchen Table unknown",
                 height: int = 0,
                 width: int = 0,
                 length: int = 0,
                 material: str = "Unknown",
                 max_height: int = 0,
                 desk_set: set = ("black", "white")
                 ):
        """
            Initializes a new instance of the KitchenTable class.

                Arguments:
                name (str): the name of the table;
                height (int): the height of the table;
                width (int): the width of the table;
                length (int): the length of the table;
                material (str): the material of the table;
                max_height (int): the maximum permissible table height;
                desk_set (set): a set of desk colors.
        """
        super().__init__(name, height, width, length, desk_set)
        self.material = material
        self.max_height = max_height

    def adjust_height(self, centimeters: int):
        """
            Increases the height of the desk (if it does not exceed the maximum allowed).
                Arguments:
                    centimeters (int): the height by which the current desk height
                    is increased.
        """
        if self.height + centimeters <= self.max_height:
            self.height += centimeters
        return self.height

    def move_down(self, centimeters: int):
        """
            Reduces the height of the desk (it cannot be less than 0).
                Arguments:
                    centimeters (int): the height by which the current table height is
                    reduced.
        """
        if self.height - centimeters >= 0:
            self.height -= centimeters
        return self.height

    def __str__(self):
        return f"KitchenTable(name={self.name}, height={self.height}, width={self.width}," \
               f" length={self.length}, material={self.material}, max_height={self.max_height}, " \
               f"desk_set={self.desk_set})"
