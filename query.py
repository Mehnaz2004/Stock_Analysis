import pandas as pd

# Read the CSV file and process the data
def process_csv(input_file, output_file):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(input_file, delimiter=',', encoding='utf-8')

    # Debug: Print column names to verify
    print("Column names:", df.columns)

    # Strip any extra spaces from column names
    df.columns = df.columns.str.strip()
    
    print(df.head())
    print("Column names:", df.columns)
    

    # Check if 'SERIES' exists
    if 'SERIES' not in df.columns:
        print("Error: 'SERIES' column not found!")
        return

    # Filter rows where SERIES equals "EQ"
    filtered_df = df[df['SERIES'] == "EQ"]
    print(filtered_df.head())

    # Sort the filtered DataFrame by the 'SYMBOL' column alphabetically
    sorted_df = filtered_df.sort_values(by='SYMBOL')

    # Save the sorted DataFrame to a new CSV file
    sorted_df.to_csv(output_file, index=False)
    print(f"Filtered and sorted data saved to {output_file}")

# Specify input and output file names
input_file = 'C:\\Users\\mehna\\OneDrive\\Desktop\\Stock_Analysis\\sec_bhavdata_full_20012025.csv'  # Replace with your input file name
output_file = 'base.csv'      # The name of the output file

# Process the file
process_csv(input_file, output_file)
