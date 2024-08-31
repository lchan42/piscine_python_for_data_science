from ft_filter import ft_filter


def check_even(number):
    if number % 2 == 0:
        return True

    return False


def printResult(lst, my_ret, real_ret):

    print(f"original_list = {lst}\nmine = {my_ret}\nreal = {real_ret}")

    if my_ret == real_ret:
        print("\033[32m sucess\033[0m\n")
    else:
        print("\033[91merror\033[0m\n")


def test():

    # from school
    s = [
            ("Hello the World", ["Hello", "World"]),
            ("Hello the World", [])
        ]
    n = [4, 99]
    filtered_str = list(ft_filter(lambda x: (len(x) > n[0]), s[0][0].split()))
    printResult(s[0][0], filtered_str, s[0][1])
    filtered_str = list(ft_filter(lambda x: (len(x) > n[1]), s[1][0].split()))
    printResult(s[0][0], filtered_str, s[1][1])

    # from https://www.programiz.com/python-programming/methods/built-in/filter
    # number list
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    my_ret = list(ft_filter(lambda x: (x % 2 == 0), lst))
    real_ret = list(filter(lambda x: (x % 2 == 0), lst))
    printResult(lst, my_ret, real_ret)

    # random list and none
    lst = [1, 'a', 0, False, True, '0']
    my_ret = list(ft_filter(None, lst))
    real_ret = list(filter(None, lst))
    printResult(lst, my_ret, real_ret)

    # char list
    lst = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
    my_ret = list(ft_filter(lambda x: (x in "aeiou"), lst))
    real_ret = list(filter(lambda x: (x in "aeiou"), lst))
    printResult(lst, my_ret, real_ret)


if __name__ == "__main__":
    test()
