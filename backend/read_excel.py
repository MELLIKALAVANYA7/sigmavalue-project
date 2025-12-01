import pandas as pd

# Path to your Excel file
file_path = 'real_estate_data.xlsx'

# Read the Excel file
df = pd.read_excel(file_path)

# Print the first 5 rows
print(df.head())
