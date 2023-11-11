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

def process_dataset(dataframe):
    """
    Process a pandas dataset by deleting columns "NUMERO" and "REFERENCIA" and adding a new column "TOTALUNIDADES".

    Parameters:
    - dataframe: pd.DataFrame, the input Pandas DataFrame

    Returns:
    - pd.DataFrame: a processed DataFrame with columns modified as described
    """
    # Check if "NUMERO" and "REFERENCIA" columns exist before dropping
    columns_to_drop = ["NUMERO", "REFERENCIA"]
    existing_columns = set(dataframe.columns)
    columns_to_drop = [col for col in columns_to_drop if col in existing_columns]

    # Drop specified columns
    dataframe.drop(columns=columns_to_drop, inplace=True, errors='ignore')

    # Add a new column "TOTALUNIDADES" by multiplying "CANTIDADCOMPRA" by "UNIDADESCONSUMOCONTENIDAS"
    dataframe["TOTALUNIDADES"] = dataframe["CANTIDADCOMPRA"] * dataframe["UNIDADESCONSUMOCONTENIDAS"]

    return dataframe

def save_to_excel(dataframe, file_path):
    """
    Save a pandas DataFrame to an Excel file.

    Parameters:
    - dataframe: pd.DataFrame, the input Pandas DataFrame
    - file_path: str, the file path where the Excel file should be saved

    Returns:
    - None
    """
    dataframe.to_excel(file_path, index=False)
    print(f"DataFrame saved to {file_path}")

original_dataset = read_excel_dataset("consumo_material_clean.xlsx")
new_dataset = process_dataset(original_dataset)

save_to_excel(new_dataset, "modified_dataset.xlsx")

# Example usage:
# processed_dataframe = process_dataset(your_input_dataframe)
