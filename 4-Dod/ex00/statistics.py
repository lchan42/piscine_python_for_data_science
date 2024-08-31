from typing import Any


# no function are allowed in this module (++ .sort())
def bubble_sort(*args) -> list:
    arg_list = list(args)
    n = len(args)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if arg_list[j] < arg_list[i]:
                arg_list[i], arg_list[j] = arg_list[j],  arg_list[i]
    return arg_list


def mean(sorted_args):
    mean = 0.0
    for sorted_arg in sorted_args:
        mean += sorted_arg
    mean /= len(sorted_args)
    return mean


def median(sorted_args):
    n = len(sorted_args)
    m_index = n // 2

    if n % 2 == 0:
        median = (sorted_args[m_index - 1] + sorted_args[m_index]) / 2
    else:
        median = (sorted_args[m_index])
    return median


def quartile(sorted_args):

    n = len(sorted_args)
    q1 = sorted_args[n//4]
    q4 = sorted_args[n//4 * 3]
    # q1 = median(sorted_args[:n//2 + 1])
    # q4 = median(sorted_args[n//2:])

    return [float(q1), float(q4)]


def standard(sorted_args):
    return variance(sorted_args) ** 0.5


def variance(sorted_args):
    variance_total = 0.0
    m = mean(sorted_args)
    for arg in sorted_args:
        variance_total += (arg - m) ** 2
    return variance_total / len(sorted_args)


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    function_dict = {
        "mean": mean,
        "median": median,
        "quartile": quartile,
        "std": standard,
        "var": variance
    }

    try:
        # assert len(args) != 0
        assert all(isinstance(arg, int | float) for arg in args)
        assert all(kvalue in function_dict for kvalue in kwargs.values())

        sorted_args = bubble_sort(*args)
        for kvalue in kwargs.values():
            print(f"{kvalue} : {function_dict[kvalue](sorted_args)}")

    except Exception:
        print("ERROR")
