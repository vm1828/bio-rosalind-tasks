import time

from typing import Callable, Any
from tempfile import NamedTemporaryFile


def test_solution(func: Callable, given: str, expected: Any, *args) -> None:
    """
    Generates tmp file with test input, 
    then the file is used as an argument for the tested function.

    Args:
        func (Callable): function to test
        given (str): test input
        expected (Any): test output

    Raises:
        Exception: expected output, actual output
    """
    with NamedTemporaryFile() as f:
        f.write(given)
        actual = func(f.name, *args)
        if actual == expected:
            print("Test passed!")
        else:
            raise Exception(
                f"\nExpected output: \n{repr(expected)}\nActual output: \n{repr(actual)}")


def timeit(n=1):
    """Decorator is used for testing function performance over n executions

    Args:
        n (int, optional): Number of executions. Defaults to 1.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            total = 0
            for _ in range(n):
                start = time.perf_counter()
                func(*args, **kwargs)
                end = time.perf_counter()
                total += (end - start)
            avg_time = round(total/n, 6)
            print(
                f"Average execution time of *{args[0].__name__}* over {n} calls: {avg_time} seconds") if avg_time else None
            return func(*args, **kwargs)
        return wrapper
    return decorator


@timeit(n=100)
def test_performance(func: Callable, test_file: str) -> None:
    """_summary_

    Args:
        func (Callable): function to test
        test_file (str): file with test input
    """
    func(test_file)
