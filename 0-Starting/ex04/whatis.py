import sys


def check_odd_even(number: int) -> str:
    if number % 2 == 0:
        return "I'm Even."
    else:
        return "I'm Odd."


if len(sys.argv) < 2:
    exit()
try:
    assert len(sys.argv) == 2, "more than one argument is provided"
    try:
        userInput = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")
    print(f"{check_odd_even(int(userInput))}")

except AssertionError as e:
    print(f"AssertionError: {e.args[0]}")
