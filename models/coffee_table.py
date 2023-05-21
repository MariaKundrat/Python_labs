from models.desk import Desk


class CoffeeTable(Desk):
    """
    A class for representing a coffee table.

        Attributes:
        name (str): the name of the table;
        height (int): the height of the table;
        width (int): the width of the table;
        length (int): the length of the table.
        number_of_shelves (int): the number of table shelves;
        number_of_seats (int): the number of seats that can be placed around the table.

        Methods:
        adjust_height(self, centimeters: int): method that does not allow to change the height of the table;
        move_down(self, centimeters: int): method that does not allow to change the height of the table;
        __str__(self): returns a string representation of the CoffeeTable object.
    """

    def __init__(self,
                 name: str = "Coffee Table unknown",
                 height: int = 0,
                 width: int = 0,
                 length: int = 0,
                 number_of_shelves: int = 0,
                 number_of_seats: int = 0
                 ):
        """
           Initializes a new instance of the CoffeeTable class.

              Arguments:
                name (str): the name of the table;
                height (int): the height of the table;
                width (int): the width of the table;
                length (int): the length of the table;
                number_of_shelves (int): the number of table shelves;
                number_of_seats (int): the number of seats that can be placed around the table.
        """
        super().__init__(name, height, width, length)
        self.number_of_shelves = number_of_shelves
        self.number_of_seats = number_of_seats

    def adjust_height(self, centimeters):
        """
           Does not allow to change the height of the table.
                Arguments:
                    centimeters (int): ignored.
        """
        print("You cannot increase the height of CoffeeTable")

    def move_down(self, centimeters):
        """
           Does not allow to change the height of the table.
                Arguments:
                    centimeters (int): ignored.
        """
        print("You cannot increase the height of CoffeeTable")

    def __str__(self):
        return f"CoffeeTable(name={self.name}, height={self.height}, width={self.width}, length={self.length}, " \
               f"number_of_shelves={self.number_of_shelves}, number_of_seats={self.number_of_seats})"
