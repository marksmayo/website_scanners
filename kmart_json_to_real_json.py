import json

# Load data from foo.txt
with open('foo.txt', 'r') as file:
    data = json.load(file)

# Initialize a list to hold the product dictionaries
products = []

# Clean up data
#entries = data.split('},')

for entry in data["response"]["results"]:
    #print(entry)
    print("----")
    print(entry["data"])
    products.append({
        "name": entry["value"],
        "url": "https://www.kmart.co.nz" + entry["data"]["url"],
        "price": f"${float(entry['data']['price']):.2f}"
    })
    if '"value":' in entry and '"url":' in entry and '"price":' in entry:
        try:
            # Extract name
            name_start = entry.index('"value":"') + len('"value":"')
            name_end = entry.index('"', name_start)
            name = entry[name_start:name_end]
            print(name)

            # Extract url
            url_start = entry.index('"url":"') + len('"url":"')
            url_end = entry.index('"', url_start)
            url = entry[url_start:url_end]

            # Extract price
            price_start = entry.index('"price":') + len('"price":')
            price_end = entry.find(',', price_start)
            if price_end == -1:
                price_end = entry.find('}', price_start)
            price = float(entry[price_start:price_end].strip().strip('"'))

            # Append to products list
            products.append({
                "name": name,
                "url": url,
                "price": price
            })
        except ValueError as e:
            print(f"Error processing entry: {entry}\nError: {e}")

# Save the JSON data to a new file
with open('products.json', 'w') as json_file:
    json.dump(products, json_file, indent=4)

print("Data successfully transformed and saved to products.json")
