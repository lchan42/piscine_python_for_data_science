from typing import Any
from functools import wraps

def callLimit(limit: int):
    count = 0

    def callLimiter(function):
        def limit_function(*args, **kwds):
            try:
                assert limit >= count , f"{function}call to many times"
                function(*args, **kwds)
            except Exception as e:
                print(f"from {__name__} \033[31m{type(e).__name__}\033[0m: {e} ")
        return limit_function


def callLimit(limit: int):

    count = 0
    def callLimiter(function):
        def limit_function(*args, **kwds):
            try:
                nonlocal count
                count += 1
                if count <= limit:
                    return function(*args, **kwds)
                else:
                    raise AssertionError(f"{function} call too many times")
            except AssertionError as error:
                print("Error:", error)
        return limit_function

    return callLimiter
