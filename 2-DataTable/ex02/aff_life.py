from load_csv import load
import matplotlib.pyplot as plt
import numpy as np


def pre_process_data(data: np.ndarray) -> np.ndarray:
    """
    Pre-process population data by converting 'M' and 'k'
    notations to numeric values.

    Parameters:
    - data (np.ndarray): The population data.

    Returns:
    - np.ndarray: The pre-processed population data.
    """

    converted_data = []
    for val in data:
        if 'M' in val:
            val = float(val.replace('M', '')) * 1e6
        elif 'k' in val:
            val = float(val[:-1]) * 1e3
        else:
            val = float(val)
        converted_data.append(val)

    return converted_data


def main():
    """
    Load population data for Belgium and France from a CSV file,
    pre-process the data, and plot population projections.

    Raises:
    - Exception: Any exception that may occur during the process.
    """

    try:
        data = load("population_total.csv")
        if data is not None:
            belgium_data = data[data['country'] == "Belgium"]
            france_data = data[data['country'] == "France"]

            # print(belgium_data
            years = np.array(belgium_data.columns[1:-50])
            belgium_val = np.array(belgium_data.values[0][1:-50])
            france_val = np.array(france_data.values[0][1:-50])

            belgium_val = pre_process_data(belgium_val)
            france_val = pre_process_data(france_val)

            plt.figure()
            plt.plot(years, france_val, label="France")
            plt.plot(years, belgium_val, label="Belgium")
            plt.legend()
            plt.title("Population Projections")
            plt.xticks(years[::40])
            plt.xlabel("Year")
            plt.ylabel("Population")
            max_pop = max(max(belgium_val), max(france_val))
            y_ticks = [i * 1e7 for i in range(int(max_pop / 1e7) + 1)]
            plt.yticks(y_ticks, ["{:,.0f}M".format(pop / 1e6) for pop
                                 in y_ticks])
            plt.show()

    except Exception as e:
        print(f"from {__name__} \033[31m{type(e).__name__}\033[0m: {e} ")


if __name__ == "__main__":
    main()
