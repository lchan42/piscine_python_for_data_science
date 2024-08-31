from sos import convert_into_morse


def printResult(lst, my_ret, real_ret):

    print(f"original_list = {lst}\nmine = {my_ret}\nreal = {real_ret}")

    if my_ret == real_ret:
        print("\033[32m sucess\033[0m\n")
    else:
        print("\033[91merror\033[0m\n")


if __name__ == "__main__":
    # https://morsecode.world/international/translator.html
    tests_tuple = (
        ("Hello World", ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."),
        ("je suis un test", ".--- . / ... ..- .. ... / ..- -. / - . ... -"),
        ("abcdefghijkl", ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.."),
        ("1 2 3 4", ".---- / ..--- / ...-- / ....-"),
        ("1234", ".---- ..--- ...-- ....-")
    )
    for test in tests_tuple:
        my_ret = convert_into_morse(test[0].split())
        real_ret = test[1]
        printResult(test[0], my_ret, real_ret)
