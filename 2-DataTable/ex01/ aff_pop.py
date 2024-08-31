from load_csv import load
import matplotlib.pyplot as plt
import numpy as np


def main():
    """
    Load life expectancy data for France from a CSV file and plot the
    projections.

    Raises:
    - Exception: Any exception that may occur during the process.
    """

    try:
        data = load("life_expectancy_years.csv")
        if data is not None:
            france_data = data[data['country'] == "France"]

            val = np.array(france_data.values[0][1:])
            years = np.array(france_data.columns[1:])

            plt.plot(years, val)
            plt.title('France Life expectancy Projections')
            plt.xlabel('Year')
            plt.ylabel('Life expectancy')
            plt.xticks(years[::40])
            plt.show()

    except Exception as e:
        print(f"from {__name__} \033[31m{type(e).__name__}\033[0m: {e} ")


if __name__ == "__main__":
    main()
