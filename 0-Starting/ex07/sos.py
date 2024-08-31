import sys


def convert_into_morse(string_lst: list[str]) -> str:
    """_summary_
    this function aims to convert any list into s string in morse

    Args:
        string_lst (list[str]): list of words that needs to be converted

    Returns:
        str: a string in morse code
    """
    # Dictionary representing the morse code chart
    NESTED_MORSE = {
        'A': '.-', 'B': '-...',
        'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-',
        'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--',
        'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.',
        '0': '-----', ', ': '--..--', '.': '.-.-.-',
        '?': '..--..', '/': '-..-.', '-': '-....-',
        '(': '-.--.', ')': '-.--.-'
    }

    ret = []
    for string in string_lst:
        morse_word = ' '.join(NESTED_MORSE[char] for char in string.upper())
        ret.append(morse_word)
    return ' / '.join(ret)


def main():

    """
    _summary_:
    this script a takes an argument and convert print it into morse code
    it supports only spaces and alphanum characters

    Raises:
        AssertionError: too much args provided
        AssertionError: non supported character provided
    """

    try:
        if len(sys.argv) != 2:
            raise AssertionError("only one argument is requiered")

        user_input_lst = sys.argv[1].split(" ")

        # new_lst = [expression for element in sequence if condition]
        # string.isalnum() for string in user_input_lst = lst of bool
        if all(string.isalnum() for string in user_input_lst):
            print(convert_into_morse(user_input_lst))
        else:
            raise AssertionError("bad argument")

    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
