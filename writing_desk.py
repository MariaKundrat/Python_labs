class WritingDesk:
    """
    A class for representing a writing desk.

          Attributes:
              number_of_drawers (int): number of desk drawers;
              has_keyboard_tray (str): whether the desk has a retractable keyboard tray;
              max_weight_capacity (int): the maximum weight that the table can support;
              current_height (int): current desk height;
              max_height: the maximum permissible table height.

          Methods:
              adjust_height(self, centimeters: int): method that increases the height of the desk (if it does not
              exceed the maximum allowed);
              move_down(self, centimeters: int): method that reduces the height of the desk (it cannot be less than 0);
              __str__(self): returns a string representation of the WritingDesk object.
    """
    __instance = None

    def __init__(
            self,
            number_of_drawers: int = 0,
            has_keyboard_tray: str = "Unknown",
            max_weight_capacity: int = 0,
            current_height: int = 0,
            max_height: int = 150
    ):
        self.number_of_drawers = number_of_drawers
        self.has_keyboard_tray = has_keyboard_tray
        self.max_weight_capacity = max_weight_capacity
        self.current_height = current_height
        self.max_height = max_height

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def adjust_height(self, centimeters: int):
        """
            Increases the height of the desk (if it does not exceed the maximum allowed).
            Arguments:
                centimeters (int): the height by which the current desk height is increased.
        """
        if self.current_height + centimeters <= self.max_height:
            self.current_height += centimeters

    def move_down(self, centimeters: int):
        """
           Reduces the height of the desk (it cannot be less than 0).
           Arguments:
               centimeters (int): the height by which the current table height is reduced.
        """
        if self.current_height - centimeters >= 0:
            self.current_height -= centimeters

    def __str__(self):
        return f"WritingDesk(number_of_drawers={self.number_of_drawers}, " \
               f"has_keyboard_tray={self.has_keyboard_tray}, max_weight_capacity={self.max_weight_capacity}, " \
               f"current_height={self.current_height}, max_height={self.max_height})"
