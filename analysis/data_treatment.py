import pandas as pd

def read_excel_dataset(file_path, sheet_name='Sheet1'):
    """
    Read an Excel dataset using Pandas.

    Parameters:
    - file_path: str, path to the Excel file
    - sheet_name: str, name of the sheet to read (default is 'Sheet1')

    Returns:
    - DataFrame: Pandas DataFrame containing the dataset
    """
    try:
        # Read the Excel file into a DataFrame
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        print(type(df))
        return df
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None
    
def count_values_in_column(dataframe, column_name):
    """
    Count the occurrences of each unique value in a specified column of a Pandas DataFrame.

    Parameters:
    - dataframe: pd.DataFrame, the input Pandas DataFrame
    - column_name: str, the name of the column to count values

    Returns:
    - dict: a dictionary where keys are unique values in the specified column,
            and values are the counts of each value
    """
    if column_name not in dataframe.columns:
        raise ValueError(f"Column '{column_name}' not found in the DataFrame.")

    # Count occurrences using value_counts() and convert to dictionary
    value_counts_dict = dataframe[column_name].value_counts().to_dict()

    return value_counts_dict

def count_products_by_year(dataframe):
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
    dataframe["Year"] = dataframe["FECHAPEDIDO"].str[-2:]

    # Count occurrences for each unique "CODIGO" and last two digits combination
    result_df = dataframe.groupby(["CODIGO", "Year"]).size().reset_index(name="NumberOfProducts")

    return result_df

def count_products_by_unidades_consumo_contenidas(dataframe):
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
    dataframe["unidades consumo"] = dataframe["UNIDADESCONSUMOCONTENIDAS"]

    # Count occurrences for each unique "CODIGO" and last two digits combination
    result_df = dataframe.groupby(["CODIGO", "Year"]).size().reset_index(name="NumberOfProducts")

    return result_df

def print_unique_values(dataframe, column_name):
    """
    Print unique values for a specified column in a DataFrame.

    Parameters:
    - dataframe: pd.DataFrame, the input Pandas DataFrame
    - column_name: str, the name of the column for which to print unique values
    """
    if column_name not in dataframe.columns:
        print(f"Column '{column_name}' not found in the DataFrame.")
        return

    unique_values = dataframe[column_name].unique()
    
    print(f"Unique values in '{column_name}': {len(unique_values)}")
    # for value in unique_values:
    #     print(value)

def print_unique_pairs(dataframe, column1, column2):
    """
    Print unique pairs of values from two specified columns in a DataFrame.

    Parameters:
    - dataframe: pd.DataFrame, the input Pandas DataFrame
    - column1: str, the name of the first column
    - column2: str, the name of the second column
    """
    if column1 not in dataframe.columns or column2 not in dataframe.columns:
        print(f"One or both columns not found in the DataFrame.")
        return

    unique_pairs = dataframe[[column1, column2]].drop_duplicates()

    print(f"Unique pairs of '{column1}' and '{column2}':")
    print(unique_pairs)

def main():
    file_path = 'consumo_material_clean.xlsx'
    dataframe = read_excel_dataset(file_path, sheet_name='Sheet1')
    # print(dataframe)
    new_df = count_products_by_year(dataframe)
    # print_unique_values(dataframe, "CODIGO")

    print(new_df)


if __name__ == "__main__":
    main()