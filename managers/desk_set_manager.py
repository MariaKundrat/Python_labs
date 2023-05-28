"""Import abstract class and desk manager"""
from managers.desk_manager import DeskManager
from models.desk import Desk


class DeskSetManager:
    """
       A class for managing a set of desks.

           Attributes:
               desk_manager (DeskManager): a DeskManager instance to manage the desks.

           Methods:
               __iter__(self): returns an iterator for the desk sets.
               __getitem__(self, key: int): returns the desk set at the specified index.
               __next__(self): returns the next desk set in the iteration.
    """

    def __init__(self, desk_manager: DeskManager = None) -> None:
        self.desk_manager = desk_manager
        self.desk_index = 0
        self.desk_set_index = 0

    def __iter__(self):
        for desk in self.desk_manager:
            for item in desk.desk_set:
                yield item

    def __getitem__(self, key: int) -> Desk:
        """
           Returns the desk set at the specified index.
               Parameters:
                   key (int): the index of the desk set to return.
               Returns:
                   Desk: the desk set at the specified index.
        """
        desk_index = 0
        key -= len(self.desk_manager[desk_index].desk_set)
        while key > 0:
            key -= len(self.desk_manager[desk_index].desk_set)
            desk_index += 1
            if desk_index >= len(self.desk_manager):
                raise IndexError("desk manager out of range")
        return list(self.desk_manager[desk_index].desk_set)[key]

    def __next__(self):
        """
           Returns the next desk set in the iteration.
               Returns:
                   Desk: the next desk set in the iteration.
        """
        if self.desk_set_index < len(self.desk_manager[self.desk_index].desk_set):
            item = list(self.desk_manager[self.desk_index].desk_set)[
                self.desk_set_index
            ]
            self.desk_set_index += 1
            return item
        self.desk_index += 1
        if self.desk_index >= len(self.desk_manager):
            raise StopIteration
        self.desk_set_index = 0
        item = list(self.desk_manager[self.desk_index].desk_set)[
            self.desk_set_index
        ]
        self.desk_set_index += 1
        return item
