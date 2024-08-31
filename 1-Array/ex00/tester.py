from give_bmi import give_bmi, apply_limit


def main():

    height = [2.71, 1.15]
    height_false = ['1', 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    bmi2 = give_bmi(height_false, weight)
    bmi3 = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(bmi2, type(bmi2))
    print(bmi3, type(bmi3))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
