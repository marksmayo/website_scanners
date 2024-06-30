import json

# Load data from foo.txt
with open('products.json', 'r') as file:
    data = file.read()

# Ensure data is parsed as JSON
try:
    products = json.loads(data)
except json.JSONDecodeError:
    print("Error: Failed to parse JSON data.")
    exit(1)

# Check if the data is a list
if not isinstance(products, list):
    print("Error: JSON data is not a list of products.")
    exit(1)

# Sort the products by price in ascending order
try:
    sorted_products = sorted(products, key=lambda x: float(x['price']))
except (TypeError, KeyError) as e:
    print(f"Error: Failed to sort products - {e}")
    exit(1)

# Generate markdown table
markdown = "| Product Name | URL | Price |\n"
markdown += "|--------------|-----|-------|\n"

for product in sorted_products:
    markdown += f"| {product['name']} | [link](https://www.kmart.co.nz/product/{product['url']}) | ${product['price']:.2f} |\n"

# Print the markdown code
print(markdown)
