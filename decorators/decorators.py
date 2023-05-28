""""Import the necessary modules"""
import os
from collections import defaultdict
import atexit

call_counts = defaultdict(int)


def log_result_to_file(func):
    """
    A decorator that logs the result of a function to a file.

        The decorator logs the result of the function to a file with a name in the format
        "class_name_function_name.txt", where "class_name" is the name of the class of the first
        argument of the function and "function_name" is the name of the function.

            Parameters:
                func (callable): the function to decorate.

            Returns:
                callable: the decorated function.
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        class_name = args[0].__class__.__name__
        file_name = f"{class_name}_{func.__name__}.txt"
        with open(file_name, "a", encoding="utf-8") as file:
            file.write(str(result) + os.linesep)
        return result
    return wrapper


def log_call_count(file_path):
    """
    A decorator that logs the number of times a function is called to a file.

        The decorator logs the number of times the function is called to a file specified by
        `file_path`.
        The file contains one line for each function that has been called, in the format
        "function_name: count", where "function_name" is the name of the function and "count" is the
        number of times it has been called.

            Parameters:
                file_path (str): path to file where call counts will be stored.

            Returns:
                callable: a decorator that takes a function as an argument and returns a decorated function.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            call_counts[func.__name__] += 1
            return func(*args, **kwargs)
        return wrapper

    def read_call_counts_from_file():
        try:
            with open(file_path, 'r', encoding="utf-8") as file:
                for line in file:
                    function_name, count = line.strip().split('=')
                    call_counts[function_name] = int(count)
        except FileNotFoundError:
            pass

    def write_call_counts_to_file():
        with open(file_path, 'w', encoding="utf-8") as file:
            for function_name, count in call_counts.items():
                file.write(f"{function_name}={count}\n")
    read_call_counts_from_file()
    atexit.register(write_call_counts_to_file)
    return decorator
