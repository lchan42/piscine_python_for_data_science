import sys
from ft_filter import ft_filter


def is_number(n) -> bool:
    try:
        int(n)
        return True
    except ValueError:
        return False


def main():
    """
    Argument:
        s (str): Text.
        n (int): Size limit.

    Returns:
        list of words that are longer than n

    Raises:
        AssertionError: only 2 arguments are requiered
        AssertionError: arguments are not str and int
    """

    try:
        if len(sys.argv) != 3:
            raise AssertionError("only a string(s), and an integer(n) needed")

        s, n = sys.argv[1], sys.argv[2]

        if not isinstance(s, str) or not is_number(n):
            raise AssertionError("the arguments are bad")

        n = int(n)

        filtered_string = \
            list(ft_filter(lambda word: len(word) > n, s.split()))

        print(filtered_string)

    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
