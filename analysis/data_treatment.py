import pandas as pd
import numpy as np

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

def count_purchases_by_year(dataframe):
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

def calculate_total_by_codigo(dataframe):
    """
    For each unique "CODIGO" value with the same "FECHAPEDIDO" last two digits, 
    multiply them by their respective "TOTALUNIDADES" and add them.

    Parameters:
    - dataframe: pd.DataFrame, the input Pandas DataFrame with "CODIGO", "FECHAPEDIDO", and "TOTALUNIDADES" columns

    Returns:
    - pd.DataFrame: a DataFrame with "CODIGO", "Year", and "TotalByCodigo" columns
    """
    if "CODIGO" not in dataframe.columns or "FECHAPEDIDO" not in dataframe.columns or "CANTIDADCOMPRA" not in dataframe.columns:
        raise ValueError("Required columns 'CODIGO', 'FECHAPEDIDO', and 'CANTIDADCOMPRA' are missing.")

    # Extract last two digits from "FECHAPEDIDO"
    dataframe["Year"] = dataframe["FECHAPEDIDO"].str[-2:]

    # Multiply "TOTALUNIDADES" by their respective "CODIGO"
    dataframe["TotalByCodigo"] = dataframe["CANTIDADCOMPRA"] * dataframe.groupby(["CODIGO", "Year"])["CANTIDADCOMPRA"].transform('sum')

    # Drop the intermediate "Year" column if needed
    # dataframe.drop(columns=["Year"], inplace=True)

    # Sum the calculated total for each unique "CODIGO" and last two digits combination
    result_df = dataframe.groupby(["CODIGO", "Year"])["TotalByCodigo"].sum().reset_index()

    return result_df

def group_by_origen_and_date(dataframe):
    """
    Group a pandas DataFrame by modified "ORIGEN" column and the last two digits of "FECHAPEDIDO".

    Parameters:
    - dataframe: pd.DataFrame, the input Pandas DataFrame with "FECHAPEDIDO" and "ORIGEN" columns

    Returns:
    - pd.DataFrame: a grouped DataFrame with counts
    """
    if "FECHAPEDIDO" not in dataframe.columns or "ORIGEN" not in dataframe.columns:
        raise ValueError("Both 'FECHAPEDIDO' and 'ORIGEN' columns are required in the DataFrame.")

    # Extract last two digits from "FECHAPEDIDO"
    dataframe["Year"] = dataframe["FECHAPEDIDO"].str[-2:]

    # Remove the last number from "ORIGEN" (assuming it's in the format "1-2-60")
    dataframe["Hospital"] = dataframe["ORIGEN"].apply(lambda x: '-'.join(x.split('-')[:-1]))

    # Group by the modified "ORIGEN" and last two digits of "FECHAPEDIDO"
    grouped_df = dataframe.groupby(["Hospital", "Year"]).size().reset_index(name="Purchases")

    return grouped_df

def group_by_codigo_and_tgl(dataframe):
    """
    Group a pandas DataFrame by "CODIGO" and "TGL" columns.

    Parameters:
    - dataframe: pd.DataFrame, the input Pandas DataFrame with "CODIGO" and "TGL" columns

    Returns:
    - pd.DataFrame: a grouped DataFrame with counts
    """
    if "CODIGO" not in dataframe.columns or "TGL" not in dataframe.columns:
        raise ValueError("Both 'CODIGO' and 'TGL' columns are required in the DataFrame.")

    # Group by "CODIGO" and "TGL"
    grouped_df = dataframe.groupby(["CODIGO", "TGL"]).size().reset_index(name="Counts")

    return grouped_df

def sum_counts_by_tgl(dataframe):
    """
    Sum the "Counts" for each unique "TGL" value in a pandas DataFrame.

    Parameters:
    - dataframe: pd.DataFrame, the input Pandas DataFrame with "CODIGO", "TGL", and "Counts" columns

    Returns:
    - pd.DataFrame: a DataFrame with the sum of "Counts" for each unique "TGL" value
    """
    if "CODIGO" not in dataframe.columns or "TGL" not in dataframe.columns or "Counts" not in dataframe.columns:
        raise ValueError("Required columns 'CODIGO', 'TGL', and 'Counts' are missing.")

    # Sum the "Counts" for each unique "TGL" value
    summed_counts_by_tgl = dataframe.groupby("TGL")["Counts"].sum().reset_index(name="TotalCounts")

    return summed_counts_by_tgl

def sum_importe_by_fecha(dataframe):
    """
    Sum the "IMPORTELINEA" for each unique "FECHAPEDIDO" last two digits in a pandas DataFrame.

    Parameters:
    - dataframe: pd.DataFrame, the input Pandas DataFrame with "FECHAPEDIDO" and "IMPORTELINEA" columns

    Returns:
    - pd.DataFrame: a DataFrame with the sum of "IMPORTELINEA" for each unique "FECHAPEDIDO" last two digits
    """
    if "FECHAPEDIDO" not in dataframe.columns or "IMPORTELINEA" not in dataframe.columns:
        raise ValueError("Required columns 'FECHAPEDIDO' and 'IMPORTELINEA' are missing.")

    # Extract last two digits from "FECHAPEDIDO"
    dataframe["Year"] = dataframe["FECHAPEDIDO"].str[-2:]

    # Sum the "IMPORTELINEA" for each unique "FECHAPEDIDO" last two digits
    summed_importe_by_fecha = dataframe.groupby("Year")["IMPORTELINEA"].sum().reset_index(name="TotalImporte")

    return summed_importe_by_fecha

def sum_importe_by_month(dataframe):
    """
    Sum the "IMPORTELINEA" for each unique "FECHAPEDIDO" last two digits in a pandas DataFrame.

    Parameters:
    - dataframe: pd.DataFrame, the input Pandas DataFrame with "FECHAPEDIDO" and "IMPORTELINEA" columns

    Returns:
    - pd.DataFrame: a DataFrame with the sum of "IMPORTELINEA" for each unique "FECHAPEDIDO" last two digits
    """
    if "FECHAPEDIDO" not in dataframe.columns or "IMPORTELINEA" not in dataframe.columns:
        raise ValueError("Required columns 'FECHAPEDIDO' and 'IMPORTELINEA' are missing.")

    # Extract last two digits from "FECHAPEDIDO"
    dataframe["Month"] = dataframe["FECHAPEDIDO"].str[-5:]

    # Sum the "IMPORTELINEA" for each unique "FECHAPEDIDO" last two digits
    summed_importe_by_fecha = dataframe.groupby("Month")["IMPORTELINEA"].sum().reset_index(name="TotalImporte")

    return summed_importe_by_fecha

def sum_cantidad_by_fecha(dataframe):
    """
    Sum the "CANTIDADCOMPRA" for each unique "FECHAPEDIDO" last two digits in a pandas DataFrame.

    Parameters:
    - dataframe: pd.DataFrame, the input Pandas DataFrame with "FECHAPEDIDO" and "CANTIDADCOMPRA" columns

    Returns:
    - pd.DataFrame: a DataFrame with the sum of "CANTIDADCOMPRA" for each unique "FECHAPEDIDO" last two digits
    """
    if "FECHAPEDIDO" not in dataframe.columns or "CANTIDADCOMPRA" not in dataframe.columns:
        raise ValueError("Required columns 'FECHAPEDIDO' and 'CANTIDADCOMPRA' are missing.")

    # Extract last two digits from "FECHAPEDIDO"
    dataframe["Year"] = dataframe["FECHAPEDIDO"].str[-2:]

    # Sum the "CANTIDADCOMPRA" for each unique "FECHAPEDIDO" last two digits
    summed_cantidad_by_fecha = dataframe.groupby("Year")["CANTIDADCOMPRA"].sum().reset_index(name="TotalCantidad")

    return summed_cantidad_by_fecha

def count_occurrences_by_year(dataframe):
    """
    Count the occurrences of each unique value of "FECHAPEDIDO" last two digits in a pandas DataFrame.

    Parameters:
    - dataframe: pd.DataFrame, the input Pandas DataFrame with "FECHAPEDIDO" column

    Returns:
    - pd.DataFrame: a DataFrame with "Year" and "Occurrences" columns
    """
    if "FECHAPEDIDO" not in dataframe.columns:
        raise ValueError("The 'FECHAPEDIDO' column is required in the DataFrame.")

    # Extract last two digits from "FECHAPEDIDO"
    dataframe["Year"] = dataframe["FECHAPEDIDO"].str[-2:]

    # Count occurrences for each unique "Year" value
    occurrences_by_year = dataframe["Year"].value_counts().reset_index()
    occurrences_by_year.columns = ["Year", "Occurrences"]

    return occurrences_by_year

def group_by_codigo_and_origen(dataframe):
    """
    Group a pandas DataFrame by "CODIGO" and "ORIGEN" columns.

    Parameters:
    - dataframe: pd.DataFrame, the input Pandas DataFrame with "CODIGO" and "ORIGEN" columns

    Returns:
    - pd.DataFrame: a grouped DataFrame with counts
    """
    if "CODIGO" not in dataframe.columns or "ORIGEN" not in dataframe.columns:
        raise ValueError("Both 'CODIGO' and 'ORIGEN' columns are required in the DataFrame.")

    # Group by "CODIGO" and "ORIGEN"
    grouped_df = dataframe.groupby(["CODIGO", "ORIGEN"]).size().reset_index(name="Counts")

    return grouped_df

def count_occurrences_by_tipo_and_year(dataframe):
    """
    Count occurrences of different values of "TIPOCOMPRA" for each unique "FECHAPEDIDO" last two digits.

    Parameters:
    - dataframe: pd.DataFrame, the input Pandas DataFrame with "FECHAPEDIDO" and "TIPOCOMPRA" columns

    Returns:
    - pd.DataFrame: a DataFrame with counts
    """
    if "FECHAPEDIDO" not in dataframe.columns or "TIPOCOMPRA" not in dataframe.columns:
        raise ValueError("Both 'FECHAPEDIDO' and 'TIPOCOMPRA' columns are required in the DataFrame.")

    # Extract last two digits from "FECHAPEDIDO"
    dataframe["Year"] = dataframe["FECHAPEDIDO"].str[-2:]

    # Group by "Year" and "TIPOCOMPRA" and count occurrences
    grouped_df = dataframe.groupby(["Year", "TIPOCOMPRA"]).size().reset_index(name="Occurrences")

    return grouped_df

def calculate_average_quantity_by_tipo_and_year(dataframe):
    """
    Calculate the average of "CANTIDADCOMPRA" for each unique "FECHAPEDIDO" last two digits and "TIPOCOMPRA" value.

    Parameters:
    - dataframe: pd.DataFrame, the input Pandas DataFrame with "FECHAPEDIDO", "TIPOCOMPRA", and "CANTIDADCOMPRA" columns

    Returns:
    - pd.DataFrame: a DataFrame with the calculated averages
    """
    if "FECHAPEDIDO" not in dataframe.columns or "TIPOCOMPRA" not in dataframe.columns or "CANTIDADCOMPRA" not in dataframe.columns:
        raise ValueError("Columns 'FECHAPEDIDO', 'TIPOCOMPRA', and 'CANTIDADCOMPRA' are required in the DataFrame.")

    # Extract last two digits from "FECHAPEDIDO"
    dataframe["Year"] = dataframe["FECHAPEDIDO"].str[-2:]

    # Group by "Year", "TIPOCOMPRA", and calculate the average of "CANTIDADCOMPRA"
    grouped_df = dataframe.groupby(["Year", "TIPOCOMPRA"])["CANTIDADCOMPRA"].mean().reset_index(name="AverageQuantity")

    return grouped_df


# def count_products_by_unidades_consumo_contenidas(dataframe):
#     """
#     Count the occurrences of the last two digits of "FECHAPEDIDO" for each unique "CODIGO" value.

#     Parameters:
#     - dataframe: pd.DataFrame, the input Pandas DataFrame with "CODIGO" and "FECHAPEDIDO" columns

#     Returns:
#     - pd.DataFrame: a DataFrame with "CODIGO" and "LastDigitsCount" columns
#     """
#     if "CODIGO" not in dataframe.columns or "FECHAPEDIDO" not in dataframe.columns:
#         raise ValueError("Both 'CODIGO' and 'FECHAPEDIDO' columns are required in the DataFrame.")

#     # Extract last two digits from "FECHAPEDIDO"
#     dataframe["unidades consumo"] = dataframe["UNIDADESCONSUMOCONTENIDAS"]

#     # Count occurrences for each unique "CODIGO" and last two digits combination
#     result_df = dataframe.groupby(["CODIGO", "Year"]).size().reset_index(name="NumberOfProducts")

#     return result_df

def calculate_spending_range(data, confidence_level=0.95, num_bootstraps=1000):
    """
    Calculate the 95% confidence interval for the spending in the next year using bootstrapping.

    Parameters:
    - data: np.array or list, the historical spending data
    - confidence_level: float, the desired confidence level (default is 0.95)
    - num_bootstraps: int, the number of bootstrap samples (default is 1000)

    Returns:
    - tuple: a tuple containing the lower and upper bounds of the confidence interval
    """
    if not isinstance(data, (np.ndarray, list)):
        raise ValueError("Input data should be a NumPy array or a Python list.")

    # Calculate the mean of the historical spending data
    mean_spending = np.mean(data)

    # Generate bootstrap samples
    bootstrap_samples = np.random.choice(data, size=(num_bootstraps, len(data)), replace=True)

    # Calculate the mean of each bootstrap sample
    bootstrap_means = np.mean(bootstrap_samples, axis=1)

    # Calculate the confidence interval
    lower_bound = np.percentile(bootstrap_means, (1 - confidence_level) / 2 * 100)
    upper_bound = np.percentile(bootstrap_means, (1 + confidence_level) / 2 * 100)

    return lower_bound, upper_bound


def filter_rows_by_column_value(dataframe, column_name, target_value):
    """
    Filter rows in a Pandas DataFrame where a specified column has a value equal to or containing the target string.

    Parameters:
    - dataframe: pd.DataFrame, the input Pandas DataFrame
    - column_name: str, the name of the column to filter on
    - target_value: str, the string to search for in the specified column

    Returns:
    - pd.DataFrame: a DataFrame with rows filtered based on the specified column and string
    """
    if column_name not in dataframe.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")

    # Filter rows where the specified column contains or is equal to the target string
    filtered_dataframe = dataframe[dataframe[column_name].str.contains(target_value, case=False, na=False)]

    return filtered_dataframe

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

# def print_unique_pairs(dataframe, column1, column2):
#     """
#     Print unique pairs of values from two specified columns in a DataFrame.

#     Parameters:
#     - dataframe: pd.DataFrame, the input Pandas DataFrame
#     - column1: str, the name of the first column
#     - column2: str, the name of the second column
#     """
#     if column1 not in dataframe.columns or column2 not in dataframe.columns:
#         print(f"One or both columns not found in the DataFrame.")
#         return

#     unique_pairs = dataframe[[column1, column2]].drop_duplicates()

#     print(f"Unique pairs of '{column1}' and '{column2}':")
#     print(unique_pairs)

def main():
    file_path = 'consumo_material_clean.xlsx' #modified_dataset.xlsx
    # file_path = 'modified_dataset.xlsx' #consumo_material_clean.xlsx
    original_dataframe = read_excel_dataset(file_path, sheet_name='Sheet1')
    # print(dataframe)
    hospital_year_purchases_df = group_by_origen_and_date(original_dataframe)
    year_money_df = sum_importe_by_fecha(original_dataframe)
    month_money_df = sum_importe_by_month(original_dataframe)
    # month_money_df = filter_rows_by_column_value(month_money_df, "Month", "/20")
    # Convert the 'Date' column to datetime format
    month_money_df['Date'] = pd.to_datetime(month_money_df['Month'], format='%m/%d')
    month_money_df = month_money_df.sort_values(by='Date').reset_index(drop=True)
    spent_money = year_money_df['TotalImporte'].values
    spent_money = np.array(spent_money)
    lower_cost, upper_cost = calculate_spending_range(spent_money)
    year_purchases_df = count_occurrences_by_year(original_dataframe)
    codigo_origen_df = group_by_codigo_and_origen(original_dataframe)
    year_tipo_df = count_occurrences_by_tipo_and_year(original_dataframe)
    tipo_average_df = calculate_average_quantity_by_tipo_and_year(original_dataframe)
    
    # new_df = group_by_codigo_and_tgl(dataframe)
    # count_TGL = sum_counts_by_tgl(new_df)
    # print_unique_values(dataframe, "CODIGO")

    print(year_tipo_df)
    print(tipo_average_df)

    # Assuming your DataFrame is named 'your_dataframe'
    # Specify the file path where you want to store the Excel file
    # excel_file_path = 'path/to/your/output_file.xlsx'

    # Use the to_excel method to save the DataFrame to an Excel file
    hospital_year_purchases_df.to_excel("excels/hospital_year_purchases.xlsx", index=False)
    year_money_df.to_excel("excels/year_money.xlsx", index=False)
    year_purchases_df.to_excel("excels/year_purchases.xlsx", index=False)
    codigo_origen_df.to_excel("excels/codigo_origen_df.xlsx", index=False)
    year_tipo_df.to_excel("excels/year_tipo.xlsx", index=False)
    tipo_average_df.to_excel("excels/year_tipo_average.xlsx", index=False)
    # print(count_TGL)


if __name__ == "__main__":
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    main()