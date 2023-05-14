class WritingDesk:
    """
    A class for representing a writing desk.

          Attributes:
              __number_of_drawers (int): number of desk drawers;
              __has_keyboard_tray (str): whether the desk has a retractable keyboard tray;
              __max_weight_capacity (int): the maximum weight that the table can support;
              __current_height (int): current desk height;
              __max_height: the maximum permissible table height.

          Methods:
              adjust_height(self, centimeters: int): method that increases the height of the desk (if it does not
              exceed the maximum allowed);
              move_down(self, centimeters: int): method that reduces the height of the desk (it cannot be less than 0);
              __str__(self): returns a string representation of the WritingDesk object.
    """
    instance = None

    def __init__(
            self,
            number_of_drawers: int = 0,
            has_keyboard_tray: str = "Unknown",
            max_weight_capacity: int = 0,
            current_height: int = 0,
            max_height: int = 150
    ):
        self.__number_of_drawers = number_of_drawers
        self.__has_keyboard_tray = has_keyboard_tray
        self.__max_weight_capacity = max_weight_capacity
        self.__current_height = current_height
        self.__max_height = max_height

    @staticmethod
    def get_instance():
        if WritingDesk.instance is None:
            WritingDesk.instance = WritingDesk()
        return WritingDesk.instance

    def adjust_height(self, centimeters: int):
        """
            Increases the height of the desk (if it does not exceed the maximum allowed).
            Arguments:
                centimeters (int): the height by which the current desk height is increased.
        """
        if self.__current_height + centimeters <= self.__max_height:
            self.__current_height += centimeters

    def move_down(self, centimeters: int):
        """
           Reduces the height of the desk (it cannot be less than 0).
           Arguments:
               centimeters (int): the height by which the current table height is reduced.
        """
        if self.__current_height - centimeters >= 0:
            self.__current_height -= centimeters

    def __str__(self):
        return f"WritingDesk(number_of_drawers={self.__number_of_drawers}, " \
               f"has_keyboard_tray={self.__has_keyboard_tray}, max_weight_capacity={self.__max_weight_capacity}, " \
               f"current_height={self.__current_height}, max_height={self.__max_height})"

        @property
        def number_of_drawers(self):
            return self.__number_of_drawers

        @number_of_drawers.setter
        def number_of_drawers(self, new_number_of_drawers):
            self.__number_of_drawers = new_number_of_drawers

        @property
        def has_keyboard_tray(self):
            return self.__has_keyboard_tray

        @has_keyboard_tray.setter
        def has_keyboard_tray(self, new_has_keyboard_tray):
            self.__has_keyboard_tray = new_has_keyboard_tray

        @property
        def max_weight_capacity(self):
            return self.__max_weight_capacity

        @max_weight_capacity.setter
        def max_weight_capacity(self, new_max_weight_capacity):
            self.__max_weight_capacity = new_max_weight_capacity

        @property
        def current_height(self):
            return self.__current_height

        @current_height.setter
        def current_height(self, new_current_height):
            self.__current_height = new_current_height

        @property
        def max_height(self):
            return self.__max_height

        @max_height.setter
        def max_height(self, new_max_height):
            self.__max_height = new_max_height
