import pandas as pd

def count_last_digits(dataframe):
    """
    Count the occurrences of the last two digits of "FECHAPEDIDO" for each unique "CODIGO" value.

    Parameters:
    - dataframe: pd.DataFrame, the input Pandas DataFrame with "CODIGO" and "FECHAPEDIDO" columns

    Returns:
    - pd.DataFrame: a DataFrame with "CODIGO" and "LastDigitsCount" columns
    """
    if "CODIGO" not in dataframe.columns or "FECHAPEDIDO" not in dataframe.columns:
        raise ValueError("Both 'CODIGO' and 'FECHAPEDIDO' columns are required in the DataFrame.")

    # Extract last two digits from "FECHAPEDIDO"
    dataframe["LastDigits"] = dataframe["FECHAPEDIDO"].str[-2:]

    # Count occurrences for each unique "CODIGO" and last two digits combination
    result_df = dataframe.groupby(["CODIGO", "LastDigits"]).size().reset_index(name="LastDigitsCount")

    return result_df

# Example usage:
data = {'CODIGO': ['A', 'B', 'A', 'B', 'A'],
        'FECHAPEDIDO': ['01/01/22', '01/02/23', '01/03/23', '01/01/23', '01/02/23']}
df = pd.DataFrame(data)

result_df = count_last_digits(df)

print("Count of last two digits of 'FECHAPEDIDO' for each 'CODIGO' value:")
print(result_df)
