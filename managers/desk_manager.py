"""Import abstract class"""
from models.desk import Desk


class DeskManager:
    """
     A class for representing a desk manager.

         Methods:
             add_desk(desk: Desk): adds a desk to the list of desks.
             find_all_tables_higher_than(value: int): finds all desks with a height greater than the
             given value.
             find_all_with_length_greater_than(value: int): finds all desks with a length greater
             than the given value.
     """

    def __init__(self):
        """
           Initializes a new instance of the DeskManager class with an empty list of desks.
        """
        self.desk_list = []

    def add_desk(self, desk: Desk) -> None:
        """
           Adds a desk to the list of desks.
                Param desk: an instance of the Desk class to be added to the list.
        """
        self.desk_list.append(desk)

    def find_all_tables_higher_than(self, value: int):
        """
           Finds all desks with a height greater than the given value.
               Param value: the height value to compare against.
               Return: a list of desks with a height greater than the given value.
        """
        return list(filter(lambda desk: desk.height > value, self.desk_list))

    def find_all_with_length_greater_than(self, value: int):
        """
           Finds all desks with a length greater than the given value.
              Param value: the length value to compare against.
              Return: a list of desks with a length greater than the given value.
        """
        return list(filter(lambda desk: desk.length > value, self.desk_list))
