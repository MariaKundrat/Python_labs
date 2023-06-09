"""
    This module provides custom exception classes.
    Exceptions:
        HeightError: an exception raised when the height of a desk exceeds its maximum
        allowed value.
        CentimetersError: an exception raised when an invalid value is passed as the number
        of centimeters to increase or decrease the height of a desk.
"""


class HeightError(Exception):
    """
        An exception raised when the height of a desk exceeds its maximum allowed value.

        Attributes:
            message (str): a message describing the error.

        Methods:
            __init__(self, message: str): initializes a new instance of the HeightError class.
    """
    def __init__(self, message):
        super().__init__(message)


class CentimetersError(Exception):
    """
        An exception raised when an invalid value is passed as the number of centimeters to increase
        or decrease the height of a desk.

        Attributes:
            message (str): a message describing the error.

        Methods:
            __init__(self, message: str): initializes a new instance of the InvalidCentimetersError
            class.
    """
    def __init__(self, message):
        super().__init__(message)
