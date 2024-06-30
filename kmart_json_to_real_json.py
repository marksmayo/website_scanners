import re
import json

# Load data from foo.txt
with open('foo.txt', 'r') as file:
    data = file.read()

# Regex pattern to match product details
pattern = re.compile(r'"value":"(.*?)".*?"url":"(.*?)".*?"price":(.*?),"')

# Extract product details using regex
products = []
matches = pattern.findall(data)
for match in matches:
    name, url, price = match
    products.append({
        "name": name,
        "url": url,
        "price": float(price)
    })

# Save the JSON data to a new file
with open('products.json', 'w') as json_file:
    json.dump(products, json_file, indent=4)

print("Data successfully transformed and saved to products.json")
