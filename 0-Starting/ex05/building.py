import sys

"""
"__name__": variable that indicates the context in which a script is excecuted

- when sript is run directly "__name__" is set to "__main__".
- when script is imported as module, "__name__" is set to "<script name>"
"""


def check_string(input_str: str):
    """_summary_

    Args:
        input_str (str): user input as a str
    function prints the following information:
    - number of characters
    - number of upper letters
    - number of lower letters
    - number of punctuation marks
    - number of spaces
    - number of digits

    due to time complexity, if foret is prefered over
    sum(1 for char in input if char.isupper())
    """

    if input_str:
        char_count = 0
        upper_count = 0
        lower_count = 0
        punctuation_count = 0
        space_count = 0
        digit_count = 0

        for char in input_str:
            char_count += 1
            if char.isupper():
                upper_count += 1
            elif char.islower():
                print("lower char: " + char)
                lower_count += 1
            elif char.isspace():
                space_count += 1
            elif char.isdigit():
                digit_count += 1
            else:
                punctuation_count += 1

        print(f"The text contains {char_count} characters:")
        print(f"{upper_count} upper letters")
        print(f"{lower_count} lower letters")
        print(f"{punctuation_count} punctuation marks")
        print(f"{space_count} spaces")
        print(f"{digit_count} digits")


def main():
    """
    Verify userInput.

    if more than one argv passed: raise AssertionError
    if no imput: prompted to provide a string

    according to subject the carriage return counts as a space,
    however input seems to ignore that carriage
    thus it has to be added manually
    """

    argv_len = len(sys.argv)
    try:
        assert argv_len <= 2, "more than one argument is provided"
        if argv_len == 2:
            user_input = sys.argv[1]
        else:
            try:
                user_input = input("What is the text to count?\n")
                user_input += "\n"
            except EOFError:
                user_input = ""
        check_string(user_input)

    except Exception as e:
        error_type = type(e).__name__
        error_message = e.args[0] if e.args else None
        print(f"{error_type}: {error_message}")


if __name__ == "__main__":
    main()
