import argparse
import analysis.data_treatment as dt

def main():
    parser = argparse.ArgumentParser(description="Read an Excel dataset using Pandas.")
    parser.add_argument("file_path", type=str, help="Path to the Excel file")
    parser.add_argument("--sheet_name", type=str, default="Sheet1", help="Name of the sheet to read (default is 'Sheet1')")

    args = parser.parse_args()

    file_path = args.file_path
    sheet_name = args.sheet_name

    print(file_path)

    data_frame = dt.read_excel_dataset(file_path, sheet_name)

    if data_frame is not None:
        print("Successfully read the Excel dataset:")
        print(data_frame.head())

if __name__ == "__main__":
    main()
