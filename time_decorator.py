from time import perf_counter, sleep
from functools import wraps


def ft_timer(func):
    """times any function"""
    @wraps(func)
    def wrapper(*arg: any, **kwargs: any):
        """wrapper doc"""
        start_time = perf_counter()

        func(*arg, *kwargs)
        end_time = perf_counter()
        total_time = round(end_time - start_time, 2)
        print("Time", total_time, "seconds")

    return wrapper


@ft_timer
def do_something(param: str):
    """function that does something"""
    sleep(1)
    print(param)


if __name__ == '__main__':
    print("coucou")
    do_something("this is the main sentense\n")
    print(do_something.__doc__)
    print(do_something.__name__)
