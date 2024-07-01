import json

# Load the JSON data
with open('products.json') as f:
    products = json.load(f)

# Function to sort products by price
def sort_products_by_price(products):
    # Extract numeric value from price and sort
    return sorted(products, key=lambda x: float(x['price'].replace('$', '')))

# Function to generate markdown table
def generate_markdown_table(products):
    markdown = "| Name | Price |\n"
    markdown += "|------|-------|\n"
    for product in products:
        name = product['name']
        url = product['url']
        price = product['price']
        markdown += f"| [{name}]({url}) | {price} |\n"
    return markdown

# Sort the products by price
sorted_products = sort_products_by_price(products)

# Generate and print the markdown table
markdown_table = generate_markdown_table(sorted_products)
print(markdown_table)
