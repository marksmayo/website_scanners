import pandas as pd

# Set the display option to show all rows
pd.set_option('display.max_rows', None)

# Function to parse markdown table and convert it to a list of dictionaries
def parse_markdown_table(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    headers = [h.strip() for h in lines[0].split('|')[1:-1]]
    data = []
    for line in lines[2:]:  # Skipping the header and the separator lines
        row_data = [cell.strip() for cell in line.split('|')[1:-1]]
        if len(row_data) == len(headers):  # Ensure the row has the correct number of columns
            row_dict = dict(zip(headers, row_data))
            data.append(row_dict)
    return data

# Function to convert discount percentages to float and format as a string with a percentage sign
def format_discount(discount_str):
    try:
        return f"{float(discount_str.replace('%', '')):.1f}%"
    except ValueError:
        return "0.0%"

# Path to your markdown file
file_path = 'json.txt'

# Parsing the markdown file to get data
data = parse_markdown_table(file_path)

# Convert the list of dictionaries to DataFrame
df = pd.DataFrame(data)

# Format the discount column
df['Discount'] = df['Discount'].apply(format_discount)

# Sort the DataFrame by discount in descending order, converting to float temporarily for sorting
df['Discount_Float'] = df['Discount'].apply(lambda x: float(x.strip('%')))
df_sorted = df.sort_values(by='Discount_Float', ascending=False)
df_sorted.drop('Discount_Float', axis=1, inplace=True)

# Function to print DataFrame in Markdown format
def print_dataframe_in_markdown(df):
    markdown_str = "| " + " | ".join(df.columns) + " |\n"
    markdown_str += "|---" * len(df.columns) + "|\n"
    for _, row in df.iterrows():
        markdown_str += "| " + " | ".join(str(x) for x in row) + " |\n"
    print(markdown_str)

# Print the sorted DataFrame in Markdown format
print_dataframe_in_markdown(df_sorted)
