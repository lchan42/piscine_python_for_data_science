from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def main():
    """
    Load life expectancy and income data for the year 1900 from CSV files,
    merge the data, and plot a scatter plot.

    Raises:
    - Exception: Any exception that may occur during the process.
    """

    try:
        # load files
        life_expect_data = load("life_expectancy_years.csv")
        income_data = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
            )

        if life_expect_data is not None and income_data is not None:
            life_expect_1900 = life_expect_data[['country', '1900']]
            income_1900 = income_data[['country', '1900']]

            # re-naming columns for more clarity
            life_expect_1900 = \
                life_expect_1900.rename(columns={'1900': 'life expectancy'})
            income_1900 = income_1900.rename(columns={'1900': 'gdp'})

            # merge tabs into a single one (also remove non-commun counties)
            df = pd.merge(life_expect_1900, income_1900, on='country')

            # remove nan from data_frame
            df = df.dropna(axis=0)

            # convert to numeric
            df["life expectancy"] = pd.to_numeric(df["life expectancy"])
            df['gdp'] = pd.to_numeric(df["gdp"])

            # show graph
            ax = df.plot.scatter(x='gdp', y='life expectancy', title='1900')
            ax.set_xscale("log")
            ax.set_xticks([300, 1000, 10000])
            ax.set_xticklabels(['300', '1k', '10k'])
            plt.show()

    except Exception as e:
        print(f"from {__name__} \033[31m{type(e).__name__}\033[0m: {e} ")


if __name__ == "__main__":
    main()
