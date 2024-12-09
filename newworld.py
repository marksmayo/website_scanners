import json

# Load the JSON data from the file
with open('json.txt') as file:
    data = json.load(file)

# Extract the relevant data
products = data['products']
product_list = []
for product in products:
    name = product['name']
    brand = product.get('brand', '')
    productid = product['productId']
    display_name = product.get('displayName', '')
    units = product['singlePrice'].get('comparativePrice', {}).get('unitQuantityUom', '')
    old_price = product['singlePrice'].get('price', 0)
    sale_price = product['promotions'][0].get('rewardValue', 0)
    cost_per_unit = product['singlePrice'].get('comparativePrice', {}).get('pricePerUnit', 0)
    discount = (old_price-sale_price) / old_price
    
    # Append data tuple
    product_list.append((name, display_name, units, sale_price, old_price, cost_per_unit, productid, brand, discount))

# Sort the list by cost per unit    
sorted_products = sorted(product_list, key=lambda x: x[8], reverse=True)


# Create markdown table
markdown_table = "| Brand | Product Name | Units | Sale Price | Cost per Unit |\n"
markdown_table += "|--------------|--------------|-------|------------|---------------|\n"
for product in sorted_products:
#for product in product_list:
    markdown_table += f"| {product[7]} | [{product[0]}](https://www.newworld.co.nz/shop/product/{product[6]}) | {product[2]} | ${product[3] / 100:.2f} | ${product[4] / 100:.2f} | {product[8]*100:.1f}%|\n"

print(markdown_table)
