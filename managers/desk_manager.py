"""Import abstract class and decorators"""
from models.desk import Desk
from decorators.decorators import log_result_to_file, log_call_count


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

    @log_result_to_file
    @log_call_count("call_counts.txt")
    def find_all_tables_higher_than(self, value: int):
        """
           Finds all desks with a height greater than the given value.
               Param value: the height value to compare against.
               Return: a list of desks with a height greater than the given value.
        """
        return list(filter(lambda desk: desk.height > value, self.desk_list))

    @log_result_to_file
    @log_call_count("call_counts.txt")
    def find_all_with_length_greater_than(self, value: int):
        """
           Finds all desks with a length greater than the given value.
              Param value: the length value to compare against.
              Return: a list of desks with a length greater than the given value.
        """
        return list(filter(lambda desk: desk.length > value, self.desk_list))

    def __len__(self) -> int:
        return len(self.desk_list)

    def __getitem__(self, desk_index: int) -> Desk:
        return self.desk_list[desk_index]

    def __iter__(self):
        return iter(self.desk_list)

    def get_height_of_desks(self) -> list[int]:
        """
           Returns a list of heights of all desks after moving them down by 10 centimeters.
               Returns:
                   list: a list of heights of all desks after moving them down by 10 centimeters.
        """
        return [desk.move_down(10) for desk in self.desk_list]

    def enumerate_desks(self):
        """
            Returns a list of tuples containing the index and desk for all desks in the desk list.
                Returns:
                    list: a list of tuples containing the index and desk for all desks in the
                    desk list.
        """
        return list(enumerate(self.desk_list))

    def zip_desk(self):
        """
           Returns a zipped list of tuples containing the height after moving down by 10 centimeters
           and desk for all desks in the desk list.
               Returns:
                   list: a list of tuples containing the height after moving down by 10
                   centimeters and desk for all desks in the desk list.
        """
        return list(zip(self.get_height_of_desks(), self.desk_list))

    def desks_higher_than(self, value):
        """
           Checks if all or any desks have a length greater than the given value.
               Parameters:
                   value (int): the length value to compare against.
               Returns:
                   dict: a dictionary with keys "All" and "Any" and values indicating if all or
                   any desks have a length greater than the given value.
        """
        all_desks = all(desk.length > value for desk in self.desk_list)
        any_desks = any(desk.length > value for desk in self.desk_list)
        return {"All": all_desks, "Any": any_desks}
