import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Load a CSV file into a Pandas DataFrame.

    Parameters:
    - path (str): The path to the CSV file.

    Returns:
    - pd.DataFrame: The loaded DataFrame.

    Raises:
    - ValueError: If the file extension is not '.csv'.
    - Exception: Any other exception that may occur during the loading process.
    """

    try:
        if ".csv" not in path:
            raise ValueError("file must be .csv")
        data = pd.read_csv(path)
        print(f"Loading dataset of dimensions {data.shape}")
        return data

    except Exception as e:
        print(f"from {__name__} \033[31m{type(e).__name__}\033[0m: {e} ")
        return None
